import sqlite3

import pandas as pd

db_conn = sqlite3.connect("database/kittybase.sqlite3")

# convert db conn to dataframe
df = pd.read_sql_query("SELECT * FROM consumed", db_conn)
print(df)
