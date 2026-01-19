import os
import pandas as pd
from .engine import con

def load_csv(path):
    table_name = os.path.splitext(os.path.basename(path))[0]
    con.execute(f"CREATE TABLE {table_name} AS SELECT * FROM read_csv_auto('{path}')")
    return table_name

def load_parquet(path):
    table_name = os.path.splitext(os.path.basename(path))[0]
    con.execute(f"CREATE TABLE {table_name} AS SELECT * FROM read_parquet('{path}')")
    return table_name

def load_xlsx(path):
    table_name = os.path.splitext(os.path.basename(path))[0]
    df = pd.read_excel(path)
    con.register('temp_df', df)
    con.execute(f"CREATE TABLE {table_name} AS SELECT * FROM temp_df")
    return table_name