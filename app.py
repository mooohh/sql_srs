# pylint: disable=missing-module-docstring
import ast
import io
import  os
import logging
import duckdb
import streamlit as st


if "data" not in os.listdir():
    logging.error(os.listdir())
    logging.error("create the data folder")
    os.mkdir("data")

if 'exercises_sql_tables.duckdb' not in os.listdir("data"):
    exec(open("init_db.py").read())

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review",
        ("cross_joins", "GroupBy", "window_functions"),
        index=None,
        placeholder="Select contact method...",
    )
    exercise_df = con.execute(f"SELECT * FROM exercises_list_df WHERE theme='{theme}'").df().sort_values(by='last_reviewed', ascending=True ).reset_index()

    st.write("You selected : ", exercise_df)

st.write(
    """
    # SQL SRS 
    Spaced Repetition System SQL practice
    """
)

request = st.text_area(label="Votre code SQL ici")

try:
    ANSWER_FILE = exercise_df.loc[0, "exercises_name"]
    with open(f"answers/{ANSWER_FILE}.sql", "r") as f:
        ANSWER_STR = f.read()
    st.write(ANSWER_STR)
    
    if request != "":
        user_answer_df = con.execute(query=request).df()
        st.write(user_answer_df)
        real_answer_df = con.execute(ANSWER_STR).df()
        try:
            comparison_result = user_answer_df.compare(real_answer_df[user_answer_df.columns])
            if comparison_result.empty:
                st.write("You Succeed")
            else:
                st.write("You did not succeed")
                st.write(comparison_result)
        except (ValueError, KeyError) as e:
            st.write("the result is not identical")
    else:
        st.write("Your should write a request")

    tables_tab, solution_tab = st.tabs(["Tables", "Solution"])
    with tables_tab:
        exercise_tables = exercise_df.loc[0, 'tables']
        for table in exercise_tables:
            table_df = con.execute(f"SELECT * FROM {table}").df()
            st.write(f"{table}", table_df)

    with solution_tab:
        st.write(ANSWER_STR)
except (ValueError, KeyError):
    st.write("You should choose an exercise please ")
con.close()
