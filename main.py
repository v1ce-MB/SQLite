# Relational Database is a database in which data is organised in tables which are related to one another
#non-relational dataase is document oriented which means all data is organised in a laundry list format.
import sqlite3 
database = "database.sqlite"
conn = sqlite3.connect(database)
print("database connected successfully")

import pandas as pd
tables = pd.read_sql ("SELECT * FROM sqlite_master WHERE type='table';", conn )
#print(tables)

teams = pd.read_sql("SELECT * FROM Team;", conn)
#print(teams) 
players = pd.read_sql("SELECT Match_Id, team_id from player_match WHERE Team_id == 8;",conn)
#print(players)
GLwins = pd.read_sql("select * from match WHERE Match_winner == 13 AND Season_Id ==9;",conn)
#print(GLwins)
# Distinct is used to select unique values.
mvps = pd.read_sql ("SELECT DISTINCT (Man_of_the_Match)from Match;", conn)
#print(mvps)
ordered_players = pd.read_sql("SELECT * from Player ORDER BY Player_Name DESC;", conn)
#print(ordered_players)
#Count is used to get the total numberof rows that satisfy a given condition. 
GL_total_wins = pd.read_sql("SELECT COUNT(Match_Id) from Match WHERE Match_Winner == 13;", conn)
print(GL_total_wins)
#sum it returns the total sum value of a numerical value
extra_runs = pd.read_sql("Select sum(Extra_Runs) from Extra_Runs ;", conn)
print(extra_runs)
#average returns the average value of a numeric value
GL_avg_wm = pd.read_sql("SELECT AVG (win_Margin) from Match WHERE Match_Winner == 13;", conn)
print(GL_avg_wm)
# Group_by converts all the summary values in groups of the same values
result = pd.read_sql("SELECT COUNT (Player_Id), Country_Name  from Player GROUP BY Country_Name;", conn)
print(result)