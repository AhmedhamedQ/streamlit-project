import streamlit as st 
import plotly.express as px 
import pandas as pd 
st.set_page_config( layout= "wide" , page_icon= "📊" , page_title = "Charts")

df = pd.read_csv("Superstore - Superstore.csv")

#drop column
df.drop("Order ID" , axis= 1 , inplace=True)

#change type column order date from object to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

#creat new column
df["year"] = df["Order Date"].apply(lambda x : x.year)
df["year"] = df["year"].astype(str)
df["month"] = df["Order Date"].apply(lambda x : x.month_name())
df["day"] = df["Order Date"].apply(lambda x : x.day_name())

#shortcuts 
num_columns =  ["Sales" , "Quantity" ,"Profit"]
color_columns = ["year" , "month" , "day"]
tab1 , tab2 , tab3 = st.tabs(["Numerical Charts" , "categorical Charts" , "Data filtering"])
cate_columns =['Segment','Category', 'City', 'State']



with tab1 :
    st.markdown('<h3 style="text-align: center; color : green;">Numerical charts</h3>', unsafe_allow_html=True)
    column = st.selectbox("select columns : " , num_columns)
    co1 , co2 = st.columns([2,2])
    check = st.checkbox("filteing by date")
    with co1 :
        col = st.selectbox("select Filter" , color_columns , key= 1)
        fig = px.histogram(df , x = column , color= col , color_discrete_sequence=px.colors.qualitative.Vivid )
        st.plotly_chart(fig)
    with co2 :
        col = st.selectbox("select Filter" , color_columns , key= 2)
        fig2 = px.box(df , x = column , color= col , color_discrete_sequence=px.colors.qualitative.Vivid )
        st.plotly_chart(fig2)
with tab2 :
    st.title("T")
with tab3 :
    st.title("p")
    
    
    
