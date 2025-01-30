import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset from Seaborn
titanic = sns.load_dataset("titanic")

st.title("Data Visualization with Streamlit")

# Histogram of Passenger Ages
st.subheader("Age Distribution of Titanic Passengers")
plt.figure(figsize=(10, 6))
sns.histplot(titanic['age'].dropna(), bins=30, kde=True)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Distribution of Ages on the Titanic")
st.pyplot(plt)

# Bar chart of Survival by Class
st.subheader("Survival Rates by Passenger Class")
survival_by_class = titanic.groupby('class')['survived'].mean().reset_index()
plt.figure(figsize=(8, 5))
sns.barplot(x='class', y='survived', data=survival_by_class)
plt.ylabel("Survival Rate")
plt.xlabel("Passenger Class")
plt.title("Survival Rates by Class on the Titanic")
st.pyplot(plt)

# Scatter plot of Age vs Fare
st.subheader("Age vs Fare Paid")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=titanic, x='age', y='fare', hue='class')
plt.xlabel("Age")
plt.ylabel("Fare")
plt.title("Age vs Fare Paid by Passengers")
st.pyplot(plt)
