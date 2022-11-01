from packages import database, list

def delete_habit_by_id(connection):
    #print list of all available habits in database
    list.all_habit(connection)
    try:

        ids = database.Database.get_ids(connection)
        ask_habit_id = int(input('\nHabit ID to Delete: '))
        
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
            print('\n!!! Invalid ID !!!\n')
	


