# ❤️ Heart Disease Prediction Project

This project builds an end-to-end machine learning pipeline to predict the risk of heart disease, visualize results, and deploy a user-friendly Streamlit web app.

## 📦 Dataset
- Source: [UCI Heart Disease dataset](https://archive.ics.uci.edu/ml/datasets/heart+Disease)
- Preprocessed: handled missing values, encoded categoricals, scaled features
- Applied PCA to reduce dimensionality

---

## 🧪 Project Steps

✅ **Step 1: Data preprocessing**
- Checked data quality, scaled features  
- Saved clean dataset

✅ **Step 2: PCA**
- Reduced dimensionality to keep ~95% variance

✅ **Step 3: Feature Selection**
- Used Random Forest importance, RFE, Chi2 test

✅ **Step 4: Supervised Learning**
- Trained Logistic Regression, Decision Tree, Random Forest, and SVM  
- Evaluated with accuracy, precision, recall, F1, ROC curve and AUC

✅ **Step 5: Unsupervised Learning**
- Applied K-Means clustering and hierarchical clustering  
- Visualized clusters & dendrogram

✅ **Step 6: Hyperparameter Tuning**
- Used GridSearchCV / RandomizedSearchCV to tune Random Forest and other models
- Saved best models

✅ **Step 7: Streamlit UI**
- Built interactive app where users can enter data and get predictions
- Display risk probability

✅ **Step 8: Deployment**
- Used Ngrok to deploy and generate public link

---

## 🖥 **How to Run Locally**
1. Clone this repo:
```bash
git clone https://github.com/yourusername/heart-disease-prediction.git
cd heart-disease-prediction
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Start Streamlit app:
```bash
cd ui
streamlit run app.py
```

---
## 🌍 **Demo**
If running, the app will be live here:  
`https://xxxx-xxxx-xxxx.ngrok.io`

---

## 📊 **Project Files**
| Folder     | Purpose                                    |
|-----------|---------------------------------------------|
| data/     | Raw & cleaned data                          |
| models/   | Saved trained & tuned models (.pkl)         |
| ui/       | Streamlit app (`app.py`)                    |
| results/  | Evaluation metrics, plots                   |
| notebooks/| Jupyter notebooks for each step             |

---

## ✏ **Author**
- **Ahmed Kamal** – [GitHub Profile](https://github.com/ahmedkamal14)

Built as part of a portfolio / learning project

