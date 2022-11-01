#creating databse with sqlite 
#define a databse connection and cursor
#create table habit with sqlite3

import sqlite3

CREATE_HABIT_TABLE = """CREATE TABLE IF NOT EXISTS 'habit'(
            'ID' INTEGER NOT NULL,
            'Name' TEXT UNIQUE,
            'Period' TEXT,
            'Created_at' INTEGER,
            'Start_Date' INTEGER,
            'Due_Date' INTEGER,
            'Streak' INTEGER,
            'Max_Streak' INTEGER,
            'Break' INTEGER,
            PRIMARY KEY("ID" AUTOINCREMENT)
        )"""

class Database:
    # Initilizing databse class and connecting with habit.db database
    def connect():
        return sqlite3.connect('habit.db')

    # Creating table in database
    def create_table(conncection):
        with conncection:
            conncection.execute(CREATE_HABIT_TABLE)

    # inserting habit in habit table with given parameters
    def insert_habit(connection, Name, Period, Created_at, Start_Date, Due_Date, Streak, Max_Streak, Break):
        with connection:
            connection.execute("""INSERT INTO habit (Name, Period, Created_at, Start_Date, Due_Date, Streak, Max_Streak, Break ) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (Name, Period, Created_at, Start_Date, Due_Date, Streak, Max_Streak, Break))

    # retrieving list of all habit in database
    def get_all_habit(connection):
        with connection:
            return connection.execute("SELECT * FROM habit").fetchall()

    # retrieving list of all habit in database filter by given period
    def get_habit_by_period(connection, Period):
        with connection:
            return connection.execute("SELECT * FROM habit WHERE Period = ?", (Period,)).fetchall()
    # retrieving list of all avaiable habit IDS from database
    def get_ids(connection):
        with connection:
            available_ids = []
            for ids in connection.execute("SELECT ID from habit"):
                available_ids.append(ids[0])
            return available_ids
                
            
            



#Predefined habit i am leaving open to decide later 
#Insert 5 predefined habits into habit.db






