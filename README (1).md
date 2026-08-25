# 🏢 Riyadh Apartments Price Prediction App

مشروع متكامل للتنبؤ بأسعار العقارات (الشقق) في مدينة الرياض باستخدام تقنيات تعلم الآلة (Machine Learning)، مع واجهة تفاعلية لتسهيل الاستخدام.

🔗 **تطبيق الويب المباشر (Live Demo):** [https://hishamksu-apartment-prices.lovable.app](https://hishamksu-apartment-prices.lovable.app)

---

## 📌 نبذة عن المشروع (Project Overview)

يهدف هذا المشروع إلى تقديم نموذج ذكاء اصطناعي دقيق لتوقع أسعار الشقق في الرياض بناءً على الميزات المختلفة للمواصفات العقارية (مثل المنطقة، الحي، المساحة، عدد الغرف، وغيرها).

تم تدريب النموذج وتطويره بالكامل وتضمينه داخل تطبيق ويب تفاعلي حديث تم تطوير واجهته الأمامية باستخدام أدوات الذكاء الاصطناعي (Lovable AI) لربطها بخادم التنبؤ وإتاحة تجربة سهلة وسريعة للمستخدمين.

---

## 🛠️ التقنيات المستخدمة (Tech Stack)

### **Machine Learning & Data Processing**
* **Python 3.10+** - لغة البرمجة الأساسية للمشروع.
* **Pandas & NumPy** - لمعالجة البيانات وتنظيفها واستخراج الميزات.
* **Scikit-Learn** - لبناء وتدريب خط معالجة البيانات ونموذج تعلم الآلة (`RandomForestRegressor`, `Pipeline`, `ColumnTransformer`, `GridSearchCV`).
* **Joblib** - لحفظ واستدعاء النموذج المدرب (`rf_model.pk1`).

### **Frontend & Web Hosting**
* **Lovable / AI-Generated Web UI** - واجهة مستخدم تفاعلية وحديثة تم تطويرها واستضافتها لتقديم تجربة استخدام سلسة.
* **Flask / Python Backend** - خادم تطبيق الويب لمعالجة طلبات التنبؤ البرمجية.

---

## 📊 دقة وأداء النموذج (Model Performance & Architecture)

تم ضبط الفائقات (Hyperparameters Tuning) للنموذج باستخدام **GridSearchCV** للحصول على أعلى كفاءة وأقل نسبة خطأ:

* **الخوارزمية:** `RandomForestRegressor` داخل Scikit-Learn Pipeline.
* **الدقة (R² Score):** **`94.24%`** على بيانات الاختبار.
* **أفضل المعاملات (Best Parameters):**
  * `max_depth`: `10`
  * `min_samples_split`: `10`
  * `n_estimators`: `200`

---

## 📥 المتغيرات والميزات المدخلة (Features Schema)

| الميزة (Feature) | النوع (Type) | الوصف الشروط |
| :--- | :--- | :--- |
| `Region` | Categorical | المنطقة (North, South, East, West, Central) |
| `Neighborhood` | Categorical | الحي (مثل: Al-Malqa, Hittin, Al-Yasmeen... إلخ) |
| `Area (sqm)` | Numerical | المساحة بالمتر المربع |
| `Bedrooms` | Numerical | عدد غرف النوم |
| `Bathrooms` | Numerical | عدد دورات المياه |
| `Floor Number` | Numerical | رقم الطابق |
| `Elevator` | Categorical | توفر مصعد (`Yes` / `No`) |
| `Property Age (years)` | Numerical | عمر العقار بالسوات |
| `Furnished` | Categorical | هل الشقة مؤثثة (`Yes` / `No`) |

---

## 🚀 طريقة التشغيل وتجربة التطبيق (Getting Started & Demo)

### 🔗 التجربة المباشرة (Live Demo)
يمكنك تجربة التطبيق مباشرة عبر الرابط التالي دون الحاجة لتثبيت أي مكتبات:
👉 [https://hishamksu-apartment-prices.lovable.app](https://hishamksu-apartment-prices.lovable.app)

---

### 💻 التشغيل المحلي (Local Setup)

1. **استكشاف المستودع (Clone Repository):**
   ```bash
   git clone https://github.com/your-username/riyadh-apartments-prediction.git
   cd riyadh-apartments-prediction
   ```

2. **تثبيت المكتبات (Install Dependencies):**
   ```bash
   pip install -r requirements.txt
   ```

3. **تدريب النموذج (Training Script):**
   ```bash
   python train_model.py
   ```

4. **تشغيل التطبيق محلياً (Run Web App):**
   ```bash
   python app.py
   ```

---

## 📁 هيكل المشروع (Project Structure)

```text
├── data/
│   └── riyadh_apartments_data.csv   # مجموعة البيانات
├── train_model.py                     # كود معالجة البيانات وتدريب النموذج
├── rf_model.pk1                        # ملف النموذج المحفوظ لـ Scikit-Learn
├── app.py                             # ملف خادم التطبيق (Backend API / App)
├── static/ & templates/               # واجهة المستخدم (AI-Generated Frontend)
├── requirements.txt                   # متطلبات المشروع
└── README.md                          # ملف التعريف بالمشروع
```

---

## 📝 رخصة المشروع (License)

هذا المشروع متاح بموجب رخصة [MIT License](LICENSE).
