# Relational Database is a database in which data is organised in tables which are related to one another
#non-relational dataase is document oriented which means all data is organised in a laundry list format.
import sqlite3 
database = "database.sqlite"
conn = sqlite3.connect(database)
print("database connected successfully")

import pandas as pd
tables = pd.read_sql ("SELECT * FROM sqlite_master WHERE type='table';", conn )
print(tables)
