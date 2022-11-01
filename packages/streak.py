#retrieve the longest streak for all available habits in database
from packages import list, database

def streak_all_habit(connection):
    print("\n\t+---- All Habits Streak ----+\n")
	
    print('+-----------------------------------------------------------+')
	
    print('Habit','\t''\t','|','\t','Streak','\t','|','\t','Period')
	
    print('+-----------------------------------------------------------+')
    # name period and max streak of all habit will print out
    command = """SELECT Name, Max_Streak, Period FROM habit ORDER BY Max_Streak DESC"""
    with connection:
        for habit in connection.execute(command):
            print(habit[0],'\t','|','\t',habit[1],'\t' '\t','|','\t',habit[2],'\n')


def longest_streak_habit(connection):
    print("\n\t+---- Longest Streak Habit ----+\n")
	
    print('+-----------------------------------------------------------+')
	
    print('Habit','\t''\t','|','\t','Streak','\t','|','\t','Period')
	
    print('+-----------------------------------------------------------+')
    #data will filter with streak only max streak will print on screan
    command = """SELECT Name, MAX(Max_Streak), Period FROM habit"""
    with connection:
        for habit in connection.execute(command):
            print(habit[0],'\t','|','\t',habit[1],'\t' '\t','|','\t',habit[2],'\n')


def shortest_streak_habit(connection):
    print("\n\t+---- Shortest Streak Habit ----+\n")
	
    print('+-----------------------------------------------------------+')
	
    print('Habit','\t''\t','|','\t','Streak','\t','|','\t','Period')
	
    print('+-----------------------------------------------------------+')
    #data will filter with streak only min streak will print on screan
    command = """SELECT Name, MIN(Max_Streak), Period FROM habit"""
    with connection:
        for habit in connection.execute(command):
            print(habit[0],'\t','|','\t',habit[1],'\t' '\t','|','\t',habit[2],'\n')


def streak_by_period(connection):
    # give user option to choose between daily or weekly period data
    Period = input("\n---Your Period Selection---\n1 for Daily\n2 for Weekly\n>>> ")

    start_selection = True
    while start_selection:
        if Period == '1':
            Period = 'Daily'
            start_selection = False
        elif Period == '2':
            Period = 'Weekly'
            start_selection = False
        else:
            print('\nInvalid Selection, Please Try Again!!\n')
            Period = input("\n---Your Period Selection---\n1 for Daily\n2 for Weekly\n>>> ")
         
    print(f"\n\t+---- {Period} Habits Streak ----+\n")
	
    print('+-----------------------------------------------------------+')
	
    print('Habit','\t''\t','|','\t','Streak','\t','|','\t','Period')
	
    print('+-----------------------------------------------------------+')
    #data will be filtered by period selection
    command = """SELECT Name, Max_Streak, Period FROM habit WHERE Period = ? ORDER BY Max_Streak DESC"""
    with connection:
        for habit in connection.execute(command,(Period,)):
            print(habit[0],'\t','|','\t',habit[1],'\t' '\t','|','\t',habit[2],'\n')


def streak_by_habit(connection):

    list.all_habit(connection)
    try:
        ids = database.Database.get_ids(connection)
        ask_habit_id = int(input('\nHabit ID: '))

        if ask_habit_id in ids:
            #if given id is available in database it will process further to extract data
            
            print("\n\t+-------- Habit Streak -------+\n")
	
            print('+-----------------------------------------------------------+')
	
            print('Habit','\t''\t','|','\t','Streak','\t','|','\t','Period')
	
            print('+-----------------------------------------------------------+')
            command = "SELECT Name, Max_Streak, Period FROM habit where ID = ?"
            with connection:
                for habit in connection.execute(command, (ask_habit_id,)):
                    print(habit[0],'\t','|','\t',habit[1],'\t' '\t','|','\t',habit[2],'\n')
            
        else: 
            print('\n***ID dose not Exist***\n')

    except ValueError:
            print('\n***Invalid ID***\n')
    
