# Credit Score Prediction 💳

This project develops a predictive machine learning model to calculate customer credit scores based on their socioeconomic and asset profiles. The primary goal is to automate financial risk analysis to support credit approval decision-making. This repository is part of my Data Science portfolio.

## 🛠️ Tech Stack & Tools

*   **Language:** Python
*   **Data Manipulation:** Pandas, NumPy
*   **Data Visualization:** Seaborn, Matplotlib
*   **Machine Learning:** Scikit-Learn

## 📊 Data Structure

The dataset contains **10,474 records** with no missing values, featuring the following variables:

*   `UF`: Customer's state of residence.
*   `IDADE` / `FAIXA_ETARIA`: Customer's age and age group.
*   `ESCOLARIDADE` / `ESTADO_CIVIL`: Sociodemographic information.
*   `QT_FILHOS`: Number of dependents.
*   `CASA_PROPRIA` / `QT_IMOVEIS` / `VL_IMOVEIS`: Real estate asset data.
*   `OUTRA_RENDA` / `OUTRA_RENDA_VALOR`: Existence and value of secondary income sources.
*   `TEMPO_ULTIMO_EMPREGO_MESES` / `TRABALHANDO_ATUALMENTE`: Professional stability history.
*   `ULTIMO_SALARIO`: Customer's primary income.
*   `QT_CARROS` / `VALOR_TABELA_CARROS`: Automotive asset data.
*   `SCORE` (**Target Variable**): Numerical credit risk score.

## 📈 Methodology & Performance

The project followed the standard Data Science development workflow:

1.  **Exploratory Data Analysis (EDA):** Score distribution analysis and outlier treatment.
2.  **Preprocessing:** Data type validation and structuring of numerical and categorical variables already encoded into integer and float formats.
3.  **Modeling:** Application of the **Linear Regression** algorithm for continuous credit score prediction.

### Model Performance

The model demonstrated a solid predictive capability for the business scenario:

*   **Coefficient of Determination (R² Score):** **79.5%**

This result indicates that 79.5% of the credit score variability is explained by the demographic, professional, and asset features integrated into the model.
