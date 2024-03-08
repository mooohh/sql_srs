import pandas as pd
import streamlit as st
import duckdb
import io


csv = '''
beverage,price
orange juice,2.5
Expresso,2
Tea,3
'''

beverages = pd.read_csv(io.StringIO(csv))

csv2 = '''
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
'''

food_items = pd.read_csv(io.StringIO(csv2))

query_beverages = """
SELECT * FROM beverages
"""

st.write("""
    # SQL SRS 
    Spaced Repetition System SQL practice
    """)


with st.sidebar:
    option = st.selectbox(
        "What would you like to review",
        ("Joins", "GroupBy", "Windows Functions"),
        index=None,
        placeholder="SEelect contact method...",
    )

    st.write("You selected : ", option)

input_text = st.text_area(label="Entrez vote request: ")
st.write(input_text)

if input_text != "":
    sql_result = duckdb.sql(input_text)
    st.dataframe(sql_result.df())

tab1, tab2 = st.tabs(["Tables", "Solution"])

with tab2:
    st.write(query_beverages)

with tab1:
    result = duckdb.sql(query_beverages).df()

    st.write("beverages: ", beverages)
    st.write("food_items: ", food_items)
    st.write("Expected: ", result)
    st.write("Result: ", result)
    #teste