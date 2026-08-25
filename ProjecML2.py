import pandas as pd
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import r2_score

data = pd.read_csv(r"C:\Users\Hisham\Downloads\riyadh_apartments_data.csv")
df = pd.DataFrame(data)
pd.set_option('display.max_columns', None)
df = df.drop(columns=['City', 'Property Type', 'Listing Type'])

X = df.drop(columns=['Selling Price (SAR)'])
y = df['Selling Price (SAR)']

num = X.select_dtypes(include='number').columns
cat = X.select_dtypes(exclude='number').columns

trans = ColumnTransformer(transformers=[
    ('num', StandardScaler(), num),
    ('cat', OneHotEncoder(), cat)
])

train_X, test_X, train_y, test_y = train_test_split(
X,
y,
random_state=42,
test_size=0.2
)

pipe = Pipeline([
    ('trans', trans),
    ('model', RandomForestRegressor(random_state=42))
])

prams = {
    'model__n_estimators':[100,200,300],
    'model__max_depth':[None,10,20],
    'model__min_samples_split':[2,5,10]
}

grid = GridSearchCV(
    pipe,
    prams,
    cv=5,
    verbose=2
)

test1 = pd.DataFrame([{
    'Region': 'North',             
    'Neighborhood': 'Al-Malqa',    
    'Area (sqm)': 300,             
    'Bedrooms': 6,               
    'Bathrooms': 2,               
    'Floor Number': 2,             
    'Elevator': 'Yes',             
    'Property Age (years)': 0, 
    'Furnished': 'No'
}])

grid.fit(train_X,train_y)
predictions = grid.predict(test_X)
rate = r2_score(test_y, predictions)

# print(test_y)
# print(predictions)
print(rate * 100)
# RATE = 94.24177009781327
print(grid.best_score_)
print(grid.best_params_)
print(grid.best_estimator_)

import joblib
from joblib import dump, load
joblib.dump(grid, 'rf_model.pk1')
# 94.24177009781327
# 0.9410915024728389
# {'model__max_depth': 10, 'model__min_samples_split': 10, 'model__n_estimators': 200}
# Pipeline(steps=[('trans',
#                  ColumnTransformer(transformers=[('num', StandardScaler(),
#                                                   Index(['Area (sqm)', 'Bedrooms', 'Bathrooms', 'Floor Number',
#        'Property Age (years)'],
#       dtype='str')),
#                                                  ('cat', OneHotEncoder(),
#                                                   Index(['Region', 'Neighborhood', 'Elevator', 'Furnished'], dtype='str'))])),
#                 ('model',
#                  RandomForestRegressor(max_depth=10, min_samples_split=10,
#                                        n_estimators=200, random_state=42))])
