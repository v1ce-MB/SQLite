# Relational Database is a database in which data is organised in tables which are related to one another
#non-relational dataase is document oriented which means all data is organised in a laundry list format.
import sqlite3 
database = "database.sqlite"
conn = sqlite3.connect(database)
print("database connected successfully")

import pandas as pd
tables = pd.read_sql ("SELECT * FROM sqlite_master WHERE type='table';", conn )
print(tables)

teams = pd.read_sql("SELECT * FROM Team;", conn)
print(teams) 
players = pd.read_sql("SELECT Match_Id, team_id from player_match WHERE Team_id == 8;",conn)
#print(players)
GLwins = pd.read_sql("select * from match WHERE Match_winner == 13 AND Season_Id ==9;",conn)
print(GLwins)