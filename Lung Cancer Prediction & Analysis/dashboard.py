import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load model and scaler
model = joblib.load("Assets/Models/logistic_regression.pkl")
scaler = joblib.load("Assets/Models/scaler.pkl")

# Define numerical and categorical columns
categorical_cols = ['SMOKING', 'EXPOSURE_TO_POLLUTION', 'LONG_TERM_ILLNESS', 
                    'FAMILY_HISTORY', 'SMOKING_FAMILY_HISTORY', 'ALCOHOL_CONSUMPTION']

numerical_cols = ['AGE', 'OXYGEN_SATURATION', 'ENERGY_LEVEL', 'STRESS_IMMUNE']

# Load dataset for visualization
df = pd.read_csv("Assets/Data/Modified Lung Cancer Dataset.csv")

# ---- Streamlit Layout ----
st.set_page_config(page_title="Lung Disease Dashboard", layout="wide")
st.title("Lung Disease Analysis & Prediction Dashboard")

# ---- Sidebar Filters ----
st.sidebar.header("Visualization Settings")
show_correlation = st.sidebar.checkbox("Show Correlation Analysis", value=True)
show_smoking = st.sidebar.checkbox("Show Smoking Analysis", value=True)

# ---- Define common plot settings ----
plot_settings = {'figsize': (10, 5), 'palette': "coolwarm"}

# ---- ROW 1: Age & Gender Distribution ----
col1, col2 = st.columns(2)

# 1️⃣ **Distribution of Pulmonary Disease by Age Groups**
with col1:
    st.subheader("Age Group vs. Pulmonary Disease")
    fig, ax = plt.subplots(figsize=plot_settings['figsize'])
    sns.countplot(data=df, x='AGE_GROUP', hue='PULMONARY_DISEASE', palette=plot_settings['palette'], ax=ax)
    for container in ax.containers:
        ax.bar_label(container, fmt='%d', label_type='edge', fontsize=8)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# 2️⃣ **Distribution by Gender**
with col2:
    st.subheader("Pulmonary Disease by Gender")
    fig, ax = plt.subplots(figsize=plot_settings['figsize'])
    sns.countplot(data=df, x='PULMONARY_DISEASE', hue='GENDER', palette=plot_settings['palette'], ax=ax)
    for container in ax.containers:
        ax.bar_label(container, fmt='%d', label_type='center', fontsize=8)
    plt.legend(title="Gender", labels=["Female", "Male"])
    st.pyplot(fig)

# ---- ROW 2: Overall Disease Distribution ----
st.subheader("Overall Pulmonary Disease Distribution")
fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(data=df, x='PULMONARY_DISEASE', hue='PULMONARY_DISEASE', palette=plot_settings['palette'], legend=False, ax=ax)
for container in ax.containers:
    ax.bar_label(container, fmt='%d', label_type='edge', fontsize=8)
st.pyplot(fig)

# ---- Expandable Sections ----
if show_correlation:
    with st.expander("📊 Correlation Analysis"):
        st.subheader("Correlation of Features with Pulmonary Disease")
        df_numeric = df.select_dtypes(include=['number'])
        correlations = df_numeric.corrwith(df_numeric['PULMONARY_DISEASE']).sort_values(ascending=False)
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(x=correlations.index, y=correlations.values, palette=plot_settings['palette'], ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

if show_smoking:
    with st.expander("🚬 Smoking & Lung Disease Proportion"):
        st.subheader("Lung Disease Proportion Among Smokers and Non-Smokers")
        proportions = df.groupby('SMOKING')['PULMONARY_DISEASE'].value_counts(normalize=True).unstack() * 100
        fig, ax = plt.subplots(figsize=(10, 5))
        proportions.plot(kind='bar', colormap="coolwarm", edgecolor='black', ax=ax)
        for container in ax.containers:
            ax.bar_label(container, fmt='%.1f%%', label_type='center')
        plt.xticks(ticks=[0, 1], labels=["Non-Smoker", "Smoker"], rotation=45)
        st.pyplot(fig)



