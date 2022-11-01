# Habit Tracker Application

- Designed and implemented with Python 3.9.7 and Sqlite3 database



## Features
- User can 
	- Create and Delete habits
	- Choose period between Daily or Weekly
	- Checkoff existing habits
	- List of Habits
	- Analyze habit performence


## Installation Requirement

pip install pytest

## github link
application can be downloaded from https://github.com/1010sb/Habit-Tracking.git

## pytest (Tested)
test file is in Test folder test.py
Enter in Test folder then type in command line: python -m pytest test.py



## How to Use 

Run from habit folder app.py 
	- Enter in habit Folder then type in command line: python app.py
        
User will be presented with following screen and can choose from given options.

----Habit Tracker Application----

Please choose one of these options:

1: Add
2: Delete
3: Checkoff
4: List
5: Streak Analysis
6: Exit


Your Selection: 
      
User can add, delete, checkoff, List, Streak Analysis.

1: Add
   	To add a new habit, user need to input Habit's Name and choose Period between daily or weekly.

2: Delete
	To delete a habit, user need to input Habit's ID. All available habits with thier ID and NAME will be printed on screen to choose ID from this list.
	
3: Checkoff
   	To checkoff a habit a list of all avialble habits will be printed on screen to choose specific Habit ID. If user checkoff the task before the due date, 
	Streak will be added by 1, as well as Max_Streak. Start_Date and Due_date will be updated.Streak will be increased if user checkoff the task within period between Start_Date and Due_Date.
   	If user didn't checkoff within period, Streak will be reset to zero, but Max_Streak still remain the same, and Break will be increased by 1.
   	If Streak > Max_Streak, then Max_Streak will be changed become as equal to Streak.
4: List
	----Habit List----

	1: All Habits
	2: Daily Habits
	3: Weekly Habits
	6: Exit

	Your Selection:
	
	1: All Habits
		All available habits in databse will be printed on screen.
	2: Daily Habits
		Only daily habits from database will be printed on screen. Data will be filtered by Period = 'Daily'
	3: Weekly Habits
		Only weekly habits from databse will be printed on screen. Data will be filtered by Period = 'Weekly'
	6: Exit
		Go back to Main Menu

5. Streak Analysis
	----Streak Analysis----

	1: Streak for All Habits
	2: Streak for Habits by Period
	3: Streak By Habit
	4: Longest Streak Habit
	5: Shortest Streak Habit
	6: Exit

	Your Selection:
	
	1: Streak for All Habits
		All existing habits with thier Max_Streak and Period will be printed on screen.
	2: Streak for Habits by Period
		User can choose period between Daily of Weekly, only according to period selection habits with thier Max_Streak and Period will be printed on screen.
        3: Streak By Habit
		List of all habits will be printed on screen user can choose a habit ID which he wants to look for streak analysis.
	4: Longest Streak Habit
		Only habit will be printed on screen which have a longest streak among all existing habits in databse. Data filter by MAX(Max_Streak).
	5: Shortest Streak Habit
		Only habit will be printed on screen which have a shortes streak among all existing habits in databse. Data filter by MIN(Max_Streak).
	6: Exit
		Go back to Main Menu


6: Exit
	Exit from the application		


