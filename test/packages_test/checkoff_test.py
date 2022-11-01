#checkoff habit in database
import sqlite3
from packages_test import database_test, list_test
from datetime import datetime, timedelta




def checkoff_habit(connection):
    twoday = datetime.today().date()
    tmdelta = timedelta(days=-1)
    yestday = twoday + tmdelta
    twomorrow = twoday + timedelta(days=1)


    try:
        #print list of all available habits in database
        list_test.all_habit(connection)
        #collecting all available ids list
        ids = database_test.Database.get_ids(connection)

        ask_habit_id = int(input('\nHabit ID to Checkoff: '))
        if ask_habit_id in ids:
            #Adding in streak value +1
            with connection:
                connection.execute('UPDATE habit SET Streak = Streak + 1 WHERE Start_Date <=? AND ID = ? AND Due_Date > ?'
                ,(twoday, ask_habit_id, yestday))

                #Update due_date
                connection.execute('UPDATE habit SET Start_Date = Due_Date WHERE ID = ? AND Start_Date < ? AND Due_Date > ?',
                     (ask_habit_id, twomorrow, yestday))
                
                #Update Max_Streak value
                connection.execute('UPDATE habit SET Max_Streak = Streak WHERE ID = ? AND Max_Streak <= Streak',(ask_habit_id,))
                
                # After break start again and starting today
                new_start_date = datetime.today().date()
                # Daily Habit Period
                daily_delta = timedelta(days=2)
                new_daily_due_date = new_start_date + daily_delta
                connection.execute('UPDATE habit SET Due_Date = ? WHERE Due_Date=Due_Date AND Period=="Daily" AND ID = ? AND Due_Date > ?',
                                    (new_daily_due_date, ask_habit_id, yestday))

                # Weekly Habit Period
                weekly_delta = timedelta(days=14)
                new_weekly_deu_date = new_start_date + weekly_delta
                connection.execute('UPDATE habit SET Due_Date = ? WHERE Due_Date=Due_Date AND Period=="Weekly" AND ID = ? AND Due_Date > ?',
                                    (new_weekly_deu_date, ask_habit_id, yestday))
                

                   
            print(f'\n!!! Habit ID {ask_habit_id} successfully checkedoff !!!\n')

                
        
        else:
            print('\n***ID dose not Exist***\n')
            
        
    except ValueError:
        print('\n***Database connection error***\n')
        

  
