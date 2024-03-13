import duckdb

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

test = con.execute("SELECT * FROM exercises_list_df").df()

print("je suis la")
print(test)
