# python -m pytest test.py

from packages_test.database_test import Database
from packages_test.streak_test import longest_streak_habit, shortest_streak_habit, streak_all_habit
from packages_test.list_test import all_habit, daily_habit_list, weekly_habit_list
from packages_test.reset_due_date_test import auto_reset

connection = Database.connect()


#habits = [('Reading', 'Daily', '2022-09-25', '2022-10-22', '2022-10-23', 6, 14, 8),
#              ('Programming', 'Daily', '2022-09-27', '2022-10-22', '2022-10-23', 5, 11, 10),
#              ('Running', 'Daily', '2022-09-30', '2022-10-22', '2022-10-23', 7, 8, 6),
#              ('Swimming', 'Weekly', '2022-10-07', '2022-10-21', '2022-11-04', 1, 1, 0),
#              ('Exercise', 'Weekly', '2022-10-21', '2022-10-21', '2022-10-28', 0, 0, 0),
#              ('Testing', 'Weekly', '2022-10-07', '2022-10-21', '2022-11-04', 0, 0, 0)
#              ]
#with connection:
#    connection.executemany("INSERT OR REPLACE INTO habit ('Name','Period','Created_at','Start_Date','Due_Date','Streak','Max_Streak','Break') VALUES (?,?,?,?,?,?,?,?)", habits)

def test_create_table():
    """Table was created with 6 data entries"""
    Database.create_table(connection)  
    for row in connection.execute("SELECT * FROM habit").fetchall():
        return row
        
    lenrecord =  len(row)
    assert lenrecord == 6

def test_add():
    """Initially 6 Habit was added as table has been created"""
    for habit in connection.execute("SELECT Name FROM habit").fetchall():
        return habit
    habit_list = habit
    assert habit_list == [('Reading',),
             ( 'Programming',),
             ( 'Running',),
             ( 'Swimming',),
             ( 'Exercise',),
             ( 'Testing',)
             ]


def test_longest_streak_habit():
     """Print out longest streak habits"""
     longest_streak_habit(connection)
     habit_list = connection.execute('SELECT Name, MAX(Max_Streak) FROM habit')
     assert list(habit_list) == [('Reading',14)]

def test_short_streak_habit():
    """Print out shortest streak from all habits"""
    shortest_streak_habit(connection)
    habit_list = connection.execute('SELECT Name, MIN(Max_Streak) FROM habit')
    assert list(habit_list) == [('Exercise',0)]

def test_streak_all_habit():
    """Print out streak from all habits"""
    streak_all_habit(connection)
    habit_list = connection.execute('SELECT Name, Max_Streak FROM habit')
    assert list(habit_list) == [('Reading', 14),('Programming',  11),('Running',  8),
                                ('Swimming',  1), ('Exercise',  0),('Testing',  0)]

def test_daily_habit_list():
    daily_habit_list(connection)
    habit_list = connection.execute("SELECT Name FROM habit WHERE Period = 'Daily'")
    assert list(habit_list) == [
             ('Reading',),
             ( 'Programming',),
             ( 'Running',)]

def test_weekly_habit():
    weekly_habit_list(connection)
    habit_list = connection.execute("SELECT Name FROM habit WHERE Period = 'Weekly'")
    assert list(habit_list) == [('Swimming',),
             ('Exercise',),
             ('Testing',)]


def test_all_habit():
    """Print out all habit list available in database"""
    all_habit(connection)
    habit_list = connection.execute("SELECT Name FROM habit ORDER BY ID")
    assert list(habit_list.fetchall()) == [('Reading',),
             ( 'Programming',),
             ( 'Running',),
             ( 'Swimming',),
             ( 'Exercise',),
             ( 'Testing',)
             ]

def test_auto_test():
    """Testing auto reset function"""
    auto_reset(connection)
    habit_list = connection.execute("SELECT Name FROM habit ORDER BY ID")
    assert list(habit_list.fetchall()) == [('Reading',),
             ( 'Programming',),
             ( 'Running',),
             ( 'Swimming',),
             ( 'Exercise',),
             ( 'Testing',)
             ]



