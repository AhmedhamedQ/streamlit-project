import pandas as pd 
import plotly.express as px 
import plotly.figure_factory as ff
import streamlit as st
df = pd.read_csv("fifa_eda - fifa_eda.csv")
def page1():
    st.title("Data Description")
    st.header("Data Head")
    st.write(df.head(10))
    st.header("Decriptive Statstics")
    st.write(df.describe())
    st.header("Number of players for each club")
    st.write(df["Club"].value_counts())
    c1 ,c2  = st.columns([2,2])
    with c1 :
        st.subheader("Top 5 highest paid clubs")
        st.write(df.groupby("Club").sum()["Wage"].sort_values(ascending=False).reset_index().head(5))
    with c2 :
        st.subheader("Top 5 highest skils")
        st.write(df[df["Overall"] >90][["Name","Overall"]].head())
        
    st.subheader("Highest Value")
    st.write(df[df["Value"] == df["Value"].max()][["Name","Age" ,'Value']])

def page2():
    st.title("Numerical Charts")
    st.header("Histogram Charts")
    st.sidebar.subheader("Histogram Column")
    Histogram_column = st.sidebar.selectbox("Select Histogram Col" ,['Overall','Value', 'Wage'])
    fig = px.histogram(df , x = Histogram_column ,title = Histogram_column.capitalize() + " Distribution")
    st.plotly_chart(fig)
    st.sidebar.subheader("Scatter X Column")
    Sc_X_col =st.sidebar.selectbox("Select Scatter X Column" ,['Overall','Value', 'Wage'])
    st.sidebar.subheader("Scatter Y Column")
    Sc_Y_col =st.sidebar.selectbox("Select Scatter Y Column" , ['Overall','Value', 'Wage'])
    sca_color = st.sidebar.checkbox("Scatter with Color")
    if sca_color:
        st.sidebar.subheader("Scatter Color")
        Sc_Color_col =st.sidebar.selectbox("Select Scatter Color Col" ,['Preferred Foot', 'Age', 'Nationality','Position',"Club","Skill Moves"])    
        fig2 = px.scatter(df , x =Sc_X_col , y = Sc_Y_col ,color=Sc_Color_col, labels={Sc_X_col : Sc_X_col.capitalize() , Sc_Y_col :Sc_Y_col.capitalize()   })
        st.plotly_chart(fig2)
    else:
        fig3 = px.scatter(df , x =Sc_X_col , y = Sc_Y_col , labels={Sc_X_col : Sc_X_col.capitalize() , Sc_Y_col :Sc_Y_col.capitalize()   })
        st.plotly_chart(fig3)

def page3():
    st.title("Categorical Charts")
    st.header("Count Plot")
    st.sidebar.subheader("Count Plot Column")
    Count_Columns = st.sidebar.selectbox("Select Count Plot Col" ,['Preferred Foot', 'Age', 'Nationality','Position',"Club","Skill Moves"] )
    Color_Check = st.sidebar.checkbox("Count With Color")
    if Color_Check :
        st.sidebar.subheader("Count Color Col")
        Count_Color_Columns = st.sidebar.selectbox("Select Count Plot Color" , ['Preferred Foot', 'Age', 'Nationality','Position',"Club","Skill Moves"])
        Group_Mode = st.sidebar.radio("Select Bar Mode" , ["relative" , "group"]) 
        fig_4 = px.histogram(data_frame= df , x =Count_Columns , color= Count_Color_Columns , barmode=Group_Mode)
        st.plotly_chart(fig_4)
    else :
        fig_4 = px.histogram(data_frame= df , x =Count_Columns)
        st.plotly_chart(fig_4) 
    
    st.header("Bar Plot")
    st.sidebar.subheader("Bar X Col")
    barX_column =st.sidebar.selectbox("Select Bar X Col" ,['Preferred Foot', 'Age', 'Nationality','Position',"Club","Skill Moves"])
    st.sidebar.subheader("Bar Y Col")
    barY_column =st.sidebar.selectbox("Select Bar Y Col" ,['Overall','Value', 'Wage'])
    fig_5 = px.bar(data_frame=df , x = barX_column , y =barY_column )
    st.plotly_chart(fig_5)

Func_to_names = {
    "Data Describe" : page1 ,
    "Numerical" : page2 ,
    "Categorical" : page3
} 
User_Choice = st.sidebar.selectbox("Select Your Page" ,Func_to_names.keys() )
Func_to_names[User_Choice]()
