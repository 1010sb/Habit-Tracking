# Main Menu Habit Tracking Application
# Program starting point
from packages import database, add, list, delete, checkoff, reset_due_date, streak



MENU_PROMPT = """----Habit Tracker Application----

Please choose one of these options:

1: Add
2: Delete
3: Checkoff
4: List
5: Streak Analysis
6: Exit

\nYour Selection: """

def main():
    connection = database.Database.connect()
    database.Database.create_table(connection)
    reset_due_date.auto_reset(connection)
    
    while (user_input := input(MENU_PROMPT)) != "6":
        if user_input == '1':
            add.add_habit(connection)
        elif user_input == '2':
            delete.delete_habit_by_id(connection)
        elif user_input == '3':
            checkoff.checkoff_habit(connection)
            
        elif user_input == '4':
            print("\n----Habit List----\n")
   
            user_selection = ""
            while user_selection != "6":
                print('1: All Habits\n2: Daily Habits\n3: Weekly Habits\n6: Exit')
                user_selection = input("\nYour Selection: ")
                

                if user_selection == '1':
                    list.all_habit(connection)
                elif user_selection == '2':
                    list.daily_habit_list(connection)
                elif user_selection == '3':
                    list.weekly_habit_list(connection)
                else:
                    print('\n!!! Invalid Selection, Please Try Again !!!\n')
        
            
            
            
        elif user_input == '5':
            print("\n----Streak Analysis----\n")
   
            user_selection = ""
            while user_selection != "6":
                print('1: Streak for All Habits\n2: Streak for Habits by Period\n3: Streak By Habit\n4: Longest Streak Habit\n5: Shortest Streak Habit\n6: Exit')
                user_selection = input("\nYour Selection: ")
                if user_selection == '1':
                    streak.streak_all_habit(connection)
                elif user_selection == '2':
                    streak.streak_by_period(connection)
                elif user_selection == '3':
                    streak.streak_by_habit(connection)
                elif user_selection == '4':
                    streak.longest_streak_habit(connection)
                elif user_selection == '5':
                    streak.shortest_streak_habit(connection)
                else:
                    print('\n!!! Invalid Selection, Please Try Again !!!\n')
            

        else:
            print('\n!!! Invalid Selection, Please Try Again !!!\n')

if __name__ == "__main__":
    main()


