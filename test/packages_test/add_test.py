# Adding new habit in database
import sqlite3
from packages_test import database_test
from datetime import datetime, timedelta

def add_habit(connection):
    try:
        Created_at = datetime.today().date()
        Name = input('\nHabit Name:  ').title().strip()
        while len(Name) < 1:
            print('\nHabit cannot be empty!\n')

        Start_Date = datetime.today().date()
        Period = input("\n** Choose Period **\n1 for Daily\n2 for Weekly\n>>> ")

        # Add Daily Habit Creation
        start_selection = True
        while start_selection:
            if Period == '1':
                Period = 'Daily'
                Due_Date = Start_Date + timedelta(days=1)
                start_selection = False

        
        
        # Add Weekly Habit Creation
            elif Period == '2':
                Period = 'Weekly'
                Due_Date = Start_Date + timedelta(days=7)
                start_selection = False

            else:
                print('**Invalid Selection, Please Try Again**\n')
                Period =  input("\n**Choose Period**\n1 for Daily\n2 for Weekly\n>>> ")
               
        database_test.Database.insert_habit(connection, Name, Period, Created_at, Start_Date, Due_Date, 0 , 0 , 0)
        print(f'\n***Your habit **{Name}** as {Period} with checkoff due date {Due_Date} successfully added***\n')
                    
    except sqlite3.IntegrityError:
        print(f'\nHabit **{Name}** is already exist!\n')


