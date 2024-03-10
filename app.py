# pylint: disable=missing-module-docstring

import io

import duckdb
import pandas as pd
import streamlit as st

CSV = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""

beverages = pd.read_csv(io.StringIO(CSV))

CSV2 = """
food_item,food_price
cookie juice,2.5
chocolate,2
muffin,3
"""

food_items = pd.read_csv(io.StringIO(CSV2))

TRUE_REQUEST = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

solution_df = duckdb.sql(TRUE_REQUEST).df()

st.write(
    """
    # SQL SRS 
    Spaced Repetition System SQL practice
    """
)

with st.sidebar:
    option = st.selectbox(
        "What would you like to review",
        ("Joins", "GroupBy", "Windows Functions"),
        index=None,
        placeholder="SEelect contact method...",
    )

    st.write("You selected : ", option)

request = st.text_area(label="Votre code SQL ici")

# Write the request
st.write(request)

if request != "":
    result_df = duckdb.sql(request).df()
    st.dataframe(result_df)

    if len(result_df.columns) != len(solution_df.columns):
        st.write("Some columns are missing")

    n_lines_difference = result_df.shape[0] - solution_df.shape[0]

    if n_lines_difference != 0:
        st.write(
            f"Your request has a {n_lines_difference} lines difference with the solution_df"
        )

    try:
        comparision_result = result_df.compare(solution_df[result_df.columns])
        if comparision_result.empty:
            st.write("You Succeed")
        else:
            st.write("You did not succeed")
            st.write(comparision_result)
    except ValueError as e:
        st.write("the result is not identical")

else:
    st.write("Your should write a request")

tables_tab, solution_tab = st.tabs(["Tables", "Solution"])

with solution_tab:
    st.write(TRUE_REQUEST)

with tables_tab:
    st.write("beverages: ", beverages)
    st.write("food_items: ", food_items)
    st.write("Expected: ", solution_df)
    st.write("Result: ", solution_df)

