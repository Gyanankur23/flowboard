import duckdb

con = duckdb.connect(':memory:')

def execute(sql):
    return con.execute(sql).fetchall()