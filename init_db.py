import io
import pandas as pd
import duckdb

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

# --------------------------------------------------------------------------
# EXERCISES LIST
# --------------------------------------------------------------------------

exercises_list = {
                  "theme": ["cross_joins", "cross_joins","cross_joins","cross_joins"],
                  "exercises_name": ["beverages_and_food", "sizes_and_trademarks","s","s"],
                  "tables": [["beverages", "food_items"], ["sizes", "trademarks"], ["s"],["s"]],
                  "last_reviewed": ["1990-01-01", "1970-01-01", "1980-01-01" , "2000-01-01"],
                  }

exercises_list_df = pd.DataFrame(exercises_list)
con.execute("CREATE TABLE IF NOT EXISTS exercises_list_df AS SELECT * FROM exercises_list_df")

# ------------------------------------------------------------------------
# CROSS JOIN EXERCISES
# ------------------------------------------------------------------------

# FIRST EXERCISE

CSV = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""

beverages = pd.read_csv(io.StringIO(CSV))
con.execute("CREATE TABLE IF NOT EXISTS beverages AS SELECT * FROM beverages")

CSV2 = """
food_item,food_price
cookie juice,2.5
chocolate,2
muffin,3
"""

food_items = pd.read_csv(io.StringIO(CSV2))
con.execute("CREATE TABLE IF NOT EXISTS food_items AS SELECT * FROM food_items")

# SECOND EXERCISE
CSV3 = '''
size
XS
M
L
XL
'''

sizes = pd.read_csv(io.StringIO(CSV3))
con.execute("CREATE TABLE IF NOT EXISTS sizes AS SELECT * FROM sizes")

CSV4 = '''
trademark
Nike
Asphalte
Abercrombie
Lewis
'''

trademarks = pd.read_csv(io.StringIO(CSV4))
con.execute("CREATE TABLE IF NOT EXISTS trademarks AS SELECT * FROM trademarks")
