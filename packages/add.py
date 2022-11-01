# Adding new habit in database
import sqlite3
from packages import database
from datetime import datetime, timedelta

def add_habit(connection):
    # getting name and period from user and instert habit with all other attributes into database
    try:
        Created_at = datetime.today().date()
        Name = input('\nHabit Name:  ').title().strip()
        while len(Name) < 1:
            print('\nHabit cannot be empty!\n')

        Start_Date = datetime.today().date()
        Period = input("\n--- Your Selection ---\n1 for Daily\n2 for Weekly\nYour Period Seleciton:  ")

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
                Period =  input("\n--- Your Selection ---\n1 for Daily\n2 for Weekly\n>>> ")
               
        database.Database.insert_habit(connection, Name, Period, Created_at, Start_Date, Due_Date, 0 , 0 , 0)
        print(f'\n***Your habit **{Name}** as {Period} with checkoff due date {Due_Date} successfully added***\n')
                    
    except sqlite3.IntegrityError:
        print(f'\nHabit **{Name}** is already exist!\n')

#def add_predefined(connection):
#    habits = [('Reading', 'Daily', '2022-09-25', '2022-10-22', '2022-10-23', 6, 14, 8),
#              ('Programming', 'Daily', '2022-09-27', '2022-10-22', '2022-10-23', 5, 11, 10),
#              ('Running', 'Daily', '2022-09-30', '2022-10-22', '2022-10-23', 7, 8, 6),
#              ('Swimming', 'Weekly', '2022-10-07', '2022-10-21', '2022-11-04', 1, 1, 0),
#              ('Exercise', 'Weekly', '2022-10-21', '2022-10-21', '2022-10-28', 0, 0, 0),
#              ]
#    with connection:
#       connection.executemany("INSERT OR REPLACE INTO habit ('Name','Period','Created_at','Start_Date','Due_Date','Streak','Max_Streak','Break') VALUES (?,?,?,?,?,?,?,?)", habits)

