# Relational Database is a database in which data is organised in tables which are related to one another
#non-relational dataase is document oriented which means all data is organised in a laundry list format.
import sqlite3 
database = "database.sqlite"
conn = sqlite3.connect(database)

print("database connected successfully")

conn.execute("""
CREATE TABLE IF NOT EXISTS example 
( s_number INT PRIMARY KEY NOT NULL, 
Name TEXT NOT NULL, 
age INT DEFAULT(18) );

""")
print("table created successfully")

# conn.execute("""
# INSERT INTO example 
# (s_number,Name, age ) values (11028, "Timothy", 24 );
# """)

# conn.execute("""
# INSERT INTO example 
# (s_number,Name, age ) values (27733, "Terry", NULL  );
# """)
# conn.commit()

import pandas as pd
tables = pd.read_sql ("SELECT * FROM sqlite_master WHERE type='table';", conn )
print(tables)

example = pd.read_sql("SELECT * FROM example;",conn )
print(example)

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
#print(GL_total_wins)
#sum it returns the total sum value of a numerical value
extra_runs = pd.read_sql("Select sum(Extra_Runs) from Extra_Runs ;", conn)
#print(extra_runs)
#average returns the average value of a numeric value
GL_avg_wm = pd.read_sql("SELECT AVG (win_Margin) from Match WHERE Match_Winner == 13;", conn)
#print(GL_avg_wm)
# Group_by converts all the summary values in groups of the same values
result = pd.read_sql("SELECT COUNT (Player_Id), Country_Name  from Player GROUP BY Country_Name;", conn)
#print(result)


null_player_match = pd.read_sql("""
SELECT * 
FROM example 
WHERE  age IS NOT NULL;
""", conn)
print(null_player_match)

#Inner joint only returns records that are in both tables.
result2 = pd.read_sql ("""
SELECT Match_Id, Match_Winner, Team_Name
FROM match 
LEFT JOIN Team                     
ON Match.Match_Winner == Team.Team_Id
;
""" ,  conn)
print(result2)

result3 = pd.read_sql("""
SELECT Team_Name, Match_Id, Match_Winner
FROM Team 
LEFT JOIN Match                      
ON Team.Team_Id == Match.Match_Winner
WHERE Season_Id == 8
;""", conn)


#print(result3)
# Left Join returns every row on the left table and if the join condition is not met then NULL values are used to fill the columns from the right table
# right Join returns every row on the right table and if the join condition is not met then NULL values are used to fill the columns from the left table

Union = pd.read_sql("""
SELECT Player_Name FROM Player
UNION 
SELECT Team_name FROM Team
UNION
SELECT Name FROM example
;
""" ,conn)
print(Union)
# Union combines two results that appear from multiple select statements. 