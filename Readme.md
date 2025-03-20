# 🩺 Lung Cancer Risk Analysis & Prediction  

## 📌 Project Overview  
Lung cancer is a leading cause of death worldwide, often diagnosed in late stages, making early detection crucial for improving survival rates. This project explores key risk factors associated with pulmonary disease, using data-driven insights to aid in early diagnosis and prevention.  

Through exploratory data analysis (EDA), statistical testing, and predictive modeling, we investigate the impact of age, gender, smoking, pollution exposure, and other factors on lung disease occurrence.  

---

## 🎯 Objectives of the Analysis  
✔ **Understand Disease Distribution**  
- Analyze the prevalence of pulmonary disease cases across different demographics.  
- Detect imbalances in the dataset that may impact conclusions.  

✔ **Identify Key Risk Factors**  
- Assess the significance of smoking, pollution exposure, and stress in disease development.  
- Determine whether age and gender play a role in lung disease prevalence.  

✔ **Perform Statistical Tests**  
- Use **Chi-Square Tests** to check relationships between categorical variables (e.g., smoking & lung disease).  
- Apply **T-Tests and Mann-Whitney U Tests** to compare affected and non-affected individuals.  

✔ **Explore Patterns & Trends**  
- Generate **bar charts, heatmaps, and correlation plots** to uncover meaningful insights.  
- Compare disease rates between different population groups to highlight disparities.  

✔ **Prepare for Predictive Modeling**  
- Convert categorical variables into numerical format for machine learning models.  
- Identify the most important predictive features using **correlation analysis & logistic regression**.  

---

## 📊 Dataset Information  
The dataset contains **demographic, lifestyle, and medical history** data related to pulmonary disease, including:  

- **Demographics**: Age, Gender  
- **Lifestyle Factors**: Smoking Status, Alcohol Consumption, Stress Levels  
- **Environmental & Medical Conditions**: Pollution Exposure, Immune Weakness, Long-Term Illness  
- **Symptoms**: Breathing Issues, Oxygen Saturation, Chest Tightness  
- **Target Variable**: Pulmonary Disease Diagnosis (Yes/No)  

### **Data Preprocessing**  
✔ Removed missing values to ensure consistency.  
✔ Categorized age into groups for better trend analysis.  
✔ Converted categorical features into numerical format for statistical tests and modeling.  

---

## 🔍 Key Questions to Answer  
✅ How does smoking influence the likelihood of developing pulmonary disease?  
✅ Are there significant gender differences in disease prevalence?  
✅ Are older individuals at higher risk than younger populations?  
✅ Which factors (e.g., pollution, stress, oxygen saturation) are the strongest predictors of pulmonary disease?  
✅ Can statistical tests confirm relationships between key variables?  

---

## 📊 Exploratory Data Analysis (EDA)  
📌 **Step 1: Pulmonary Disease Distribution**  
- How common is pulmonary disease in this dataset?  
- Is the dataset balanced or skewed toward healthy individuals?  

📌 **Step 2: Age Group Analysis**  
- Are older people more likely to have pulmonary disease?  
- Do specific age brackets require more medical screening?  

📌 **Step 3: Gender-Based Analysis**  
- Does gender impact disease prevalence?  
- Could lifestyle factors explain any disparities?  

📌 **Step 4: Correlation Analysis**  
- Which features are most strongly linked to pulmonary disease?  
- Are there unexpected correlations that should be explored further?  

📌 **Step 5: Smoking vs. Lung Disease**  
- Do smokers have a significantly higher risk of pulmonary disease?  
- Are there non-smokers with the disease, suggesting other risk factors?  

---

## 🧪 Statistical Testing  
We conduct **hypothesis tests** to confirm which factors significantly influence pulmonary disease:  

📌 **Chi-Square Test**  
✔ Tests the relationship between smoking & lung disease.  
✔ Determines if gender differences are statistically significant.  

📌 **T-Test**  
✔ Compares average age of affected vs. non-affected individuals.  

📌 **Mann-Whitney U Test**  
✔ Compares oxygen saturation levels between healthy and diseased individuals.  

📌 **Logistic Regression**  
✔ Identifies the top predictors of pulmonary disease.  

---

## 📈 Key Findings & Insights  
🔹 **Smoking** is a major risk factor for pulmonary disease.  
🔹 **Older individuals** are more likely to be affected.  
🔹 **Gender differences** exist, but further testing is needed.  
🔹 **Pollution exposure, stress, and oxygen levels** are strong predictors.  
🔹 **Predictive models** can be used to assess individual risk factors.  

---

## 🚀 Next Steps & Future Work  
✅ **Expand Statistical Testing:**  
- Conduct additional hypothesis tests (**e.g., ANOVA** for multiple group comparisons).  
- Test for interaction effects (e.g., how **smoking & pollution combined** affect risk).  

✅ **Enhance Exploratory Data Analysis (EDA):**  
- Include **geographical or genetic** data to uncover hidden risk factors.  
- Analyze **time-series trends** if historical data is available.  

✅ **Build Predictive Models:**  
- Train **Logistic Regression, Decision Trees, and Random Forests** for risk prediction.  
- Use **feature selection techniques** to optimize model performance.  

✅ **Improve Data Representation:**  
- Address **potential class imbalance** in disease cases using **oversampling/undersampling**.  
- Include **real-world patient data** for validation.  

✅ **Provide Actionable Recommendations:**  
- Use findings to improve **screening programs for high-risk individuals**.  
- Develop **health interventions** based on top risk factors.  

---

## 📌 Summary  
This project provides **data-driven insights** into lung disease risk factors, aiming to improve **prevention, screening, and early diagnosis**. By conducting:  

✔ **Exploratory Data Analysis (EDA)** – Identifying trends and correlations.  
✔ **Statistical Testing** – Confirming relationships between variables.  
✔ **Predictive Modeling** – Developing ML models for early detection.  

As the **next phase**, we will conduct **advanced statistical tests**, refine **predictive models**, and explore **additional factors** (e.g., pollution, genetics, and environmental conditions). 🚀  

---

## 📌 How to Use This Repository  

### **1️⃣ Clone the Repository**

git clone https://github.com/Ukandu20/Health-Analytics.git
cd Lung-Cancer-Risk-Analysis

### **2️⃣ Install Dependencies**
To install the required packages, run the following command:  


pip install -r requirements.txt

### 3️⃣ Run the Jupyter Notebook


jupyter notebook


### 4️⃣ Follow the steps in the notebook to:
✔ Explore the dataset
✔ Perform EDA & hypothesis testing
✔ Visualize trends & correlations
✔ Build predictive models

📌 Contributing
💡 Ideas for improvement? Feel free to submit a pull request or open an issue!

📌 Data Source
(https://www.kaggle.com/datasets/shantanugarg274/lung-cancer-prediction-dataset)

🚀 Contact & Support
For any inquiries, reach out via:
📩 Email: (mailto:okechiukandu@gmail.com)
💼 LinkedIn: (https://www.linkedin.com/in/okechiukandu/)