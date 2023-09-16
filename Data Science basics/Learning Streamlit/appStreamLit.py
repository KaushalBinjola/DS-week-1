# # This app is for educational purpose only. Insights gained is not financial advice. Use at your own risk!
import streamlit as st
import pandas as pd
import requests
import json

st.title('Calculator App')
st.markdown("""Basic Calculator App!""")

st.sidebar.title("Calculator Inputs")
a = st.sidebar.number_input("Enter First Number",value=1)
b = st.sidebar.number_input("Enter Second Number",value=1)

operators = ["+","-","/","*"]

    
op = st.sidebar.selectbox("Select Operator",operators)


@st.cache
def performOperation():
    answer = ""
    if(op=='/' and b==0):
        return ("Cannot divide by zero")
    else:
        if op == '+':
            answer =  (a+b)
        if op == '-':
            answer =  (a-b)
        if op == '/':
            answer =  (a/b)
        if op == '*':
            answer =  (a*b)
            
    first = pd.Series([a],name = "First Number")
    operator = pd.Series([op],name = "Operator")
    second = pd.Series([b],name = "Second Number")
    ans = pd.Series([answer],name = "Answer")
    df = pd.concat([first,operator,second,ans],axis=1)
    return df
    

data = performOperation()
st.write("Answer is",data)