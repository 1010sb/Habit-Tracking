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
application can be downloaded from following link
https://github.com/1010sb/Habit-Tracking.git



## pytest (Tested)
test file is in Test folder test.py
Enter in Test folder then type in command line: python -m pytest test.py



## How to Use 

Run from habit folder app.py 
	- Enter in habit Folder then type in command line: python app.py
        
User will be presented with following screen and can choose from given options.

![start](https://user-images.githubusercontent.com/96765388/199236524-db41d040-58aa-401e-afe1-e1144943c55c.png)


 

### Add
- To add a new habit, user need to input Habit's Name and choose Period between daily or weekly.

### Delete
- To delete a habit, user need to input Habit's ID. All available habits with thier ID and NAME will be printed on screen to choose ID from this list.
	
### Checkoff
- To checkoff a habit a list of all avialble habits will be printed on screen to choose specific Habit ID. If user checkoff the task before the due date, 
- Streak will be added by 1, as well as Max_Streak. Start_Date and Due_date will be updated.Streak will be increased if user checkoff the task within period 	   between Start_Date and Due_Date.
- If user didn't checkoff within period, Streak will be reset to zero, but Max_Streak still remain the same, and Break will be increased by 1.
- If Streak > Max_Streak, then Max_Streak will be changed become as equal to Streak.
### List
![list](https://user-images.githubusercontent.com/96765388/199237343-7ec486a8-b121-4c7e-97fb-55f23e3ddfe0.png)



### Streak Analysis
![analysis](https://user-images.githubusercontent.com/96765388/199237711-d399cf1a-af40-4d50-890c-e6a12b05243e.png)

- 1: Streak for All Habits: All existing habits with thier Max_Streak and Period will be printed on screen.
- 2: Streak for Habits by Period: User can choose period between Daily of Weekly, only according to period selection habits with thier Max_Streak and Period will be printed on screen.
- 3: Streak By Habit: List of all habits will be printed on screen user can choose a habit ID which he wants to look for streak analysis.
- 4: Longest Streak Habit: Only habit will be printed on screen which have a longest streak among all existing habits in databse. Data filter by MAX(Max_Streak).
- 5: Shortest Streak Habit: Only habit will be printed on screen which have a shortes streak among all existing habits in databse. Data filter by MIN(Max_Streak).
- 6: Exit: Go back to Main Menu


### Exit
	Exit from the application		







