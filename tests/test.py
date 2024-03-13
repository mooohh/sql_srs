import duckdb

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

test = con.execute("SELECT * FROM size").df()

print("je suis la")
print(test)
