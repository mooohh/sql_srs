import pandas as pd
import streamlit as st
import duckdb

st.write("Hello World")

data = {"a": [1, 2, 3.], "b": [4, 5, 6]}

df = pd.DataFrame(data)

tab2, tab1 = st.tabs(["sql", "Others"])

with tab2:
    st.write(df)
    input_text = st.text_area(label="Entrez vote request: ")
    st.write(input_text)
    if input_text != "":
        sql_result = duckdb.sql(input_text)
        st.dataframe(sql_result.df())

with tab1:
    st.write(df)