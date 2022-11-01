from packages_test import database_test, list_test


def delete_habit_by_id(connection, id: int):
    #print list of all available habits in database
    list_test.all_habit(connection)
    ask_habit_id = id
    ids = database_test.Database.get_ids(connection)
    ask_habit_id = int(input('\nHabit ID to Delete: '))
    try:

        
        
        if ask_habit_id in ids:
            #if given id is available in database will be deleted
            with connection:
                connection.execute("DELETE from habit where ID = ?", (ask_habit_id,))
                #Sort and Update ids after deletion
                connection.execute(f'''UPDATE habit SET ('ID') = (ID)-1  WHERE ID > {ask_habit_id} ;''')

                
            print(f'\n!!! Habit ID {ask_habit_id} deleted !!!\n')
        else:
            print('\n***ID dose not Exist***\n')
    
    except ValueError:
            print('\n***Invalid ID***\n')
	
#delete_habit_by_id(connection=any, id=7)