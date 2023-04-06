import streamlit as st 
import plotly.express as px 
import pandas as pd 

st.set_page_config(layout="wide",page_title='Data describtion',page_icon='📉')
df = pd.read_csv("Superstore - Superstore.csv")
#drop column
df.drop("Order ID" , axis= 1 , inplace=True)

#change type column order date from object to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

#creat new column
df["year"] = df["Order Date"].apply(lambda x : x.year)
df["year"] = df["year"].astype(str)
df["month_name"] = df["Order Date"].apply(lambda x : x.month_name())
df["day_name"] = df["Order Date"].apply(lambda x : x.day_name())

#shortcuts
numerical_data = df.describe()
categorical_data = df.describe(include = 'O')

st.markdown('<h1 style="text-align: center; color : red;">📄 Page 1</h1>', unsafe_allow_html=True)
tab, tab1 = st.tabs(["💻 Data Fram",'🧮 Describtive Stats'])

with tab :
    st.markdown('<h3 style="text-align: center; color : blue;">Data Fram</h3>', unsafe_allow_html=True)
    st.dataframe(df.copy())
with tab1 :
    co1 ,co2 = st.columns([3,4])
    with co1 :
        st.subheader('Numerical Describtive Statistics')
        st.dataframe(numerical_data)
    with co2 :
        st.subheader("Categorical Describtive Statistics")
        st.dataframe(categorical_data)
    
    
