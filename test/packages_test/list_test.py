from packages_test import database_test

# retrieving list of all habit from database and print 
def all_habit(connection):
    
    print("\n\t+----List of All Habits----+\n")
	
    print('+------------------------------------------------+')
	
    print('ID','\t','|','\t','Habit ','\t','|','\t','Period',)
	
    print('+------------------------------------------------+')

    for habit in database_test.Database.get_all_habit(connection):
        print(habit[0],'\t','|','\t',habit[1],'\t','|','\t',habit[2],'\n')
  
# retrieving list of all habit in database filter by given period

def daily_habit_list(connection):
    Period = 'Daily'
    print(f"\n\t+---- {Period} List of Habits ----+\n")
	
    print('+------------------------------------------------+')
	
    print('ID','\t','|','\t','Habit ','\t','|','\t','Period',)
	
    print('+------------------------------------------------+')

    for habit in database_test.Database.get_habit_by_period(connection, Period):
        print(habit[0],'\t','|','\t',habit[1],'\t','|','\t',habit[2],'\n')

def weekly_habit_list(connection):
    Period = 'Weekly'
    print(f"\n\t+---- {Period} List of Habits ----+\n")
	
    print('+------------------------------------------------+')
	
    print('ID','\t','|','\t','Habit ','\t','|','\t','Period',)
	
    print('+------------------------------------------------+')

    for habit in database_test.Database.get_habit_by_period(connection, Period):
        print(habit[0],'\t','|','\t',habit[1],'\t','|','\t',habit[2],'\n')

#
#
#def habit_by_period(connection): 
#    
#    Period = input("\n---Your Period Selection---\n1 for Daily\n2 for Weekly\n>>> ")
#
#    start_selection = True
#    while start_selection:
#        if Period == '1':
#            Period = 'Daily'
#            start_selection = False
#        elif Period == '2':
#            Period = 'Weekly'
#            start_selection = False
#        else:
#            print('\n!!! Invalid Selection, Please Try Again !!!\n')
#            Period = input("\n---Your Period Selection---\n1 for Daily\n2 for Weekly\n>>> ")
#
#
#
#
#    print(f"\n\t+---- {Period} List of Habits ----+\n")
#	
#    print('+------------------------------------------------+')
#	
#    print('ID','\t','|','\t','Habit ','\t','|','\t','Period',)
#	
#    print('+------------------------------------------------+')
#
#    for habit in database.Database.get_habit_by_period(connection, Period):
#        print(habit[0],'\t','|','\t',habit[1],'\t','|','\t',habit[2],'\n')
#   