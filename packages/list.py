from packages import database

# retrieving list of all habit from database and print 
def all_habit(connection):
    
    print("\n\t+----List of All Habits----+\n")
	
    print('+------------------------------------------------+')
	
    print('ID','\t','|','\t','Habit ','\t','|','\t','Period',)
	
    print('+------------------------------------------------+')

    for habit in database.Database.get_all_habit(connection):
        print(habit[0],'\t','|','\t',habit[1],'\t','|','\t',habit[2],'\n')
  
# retrieving list of all habit in database filter by given period

def daily_habit_list(connection):
    Period = 'Daily'
    print(f"\n\t+---- {Period} List of Habits ----+\n")
	
    print('+------------------------------------------------+')
	
    print('ID','\t','|','\t','Habit ','\t','|','\t','Period',)
	
    print('+------------------------------------------------+')

    for habit in database.Database.get_habit_by_period(connection, Period):
        print(habit[0],'\t','|','\t',habit[1],'\t','|','\t',habit[2],'\n')

def weekly_habit_list(connection):
    Period = 'Weekly'
    print(f"\n\t+---- {Period} List of Habits ----+\n")
	
    print('+------------------------------------------------+')
	
    print('ID','\t','|','\t','Habit ','\t','|','\t','Period',)
	
    print('+------------------------------------------------+')

    for habit in database.Database.get_habit_by_period(connection, Period):
        print(habit[0],'\t','|','\t',habit[1],'\t','|','\t',habit[2],'\n')

