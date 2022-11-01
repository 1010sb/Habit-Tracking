#Auto reseting due dates for all active habits in database
from packages import database
from time import sleep

from datetime import datetime, timedelta

def auto_reset(connection):

    delta = timedelta(days=-1)
    day_befor = datetime.today().date() + delta

    new_start_date = datetime.today().date()

    daily_period = 1
    delta_daily = timedelta(days=1)
    new_daily_due_date = new_start_date + delta_daily

    weekly_period = 7
    delta_weekly = timedelta(days=7)
    new_weekly_due_date = new_start_date + delta_weekly

    
   
    # Add break to all over due dated habits in database
    # Check if habit is over due dated add Break +1
    with connection:
        connection.execute('UPDATE habit SET Break = +1 WHERE Break=Break AND Due_Date <= ?', 
        (day_befor,))
        # Update Streak and reset to 0
        connection.execute('UPDATE habit SET Streak = ? WHERE Streak = Streak AND Due_Date <= ?', 
        (0, day_befor))
        # Reset Start_Date with new_start_date from where onward count the deu date.
        connection.execute('UPDATE habit SET Start_Date = ? WHERE Start_Date = Start_Date AND Due_Date <= ?',
        (new_start_date, day_befor))
        # Reset Daily Period Due_Date with new_daily_due_date
        connection.execute('UPDATE habit SET Due_Date = ? WHERE Due_Date = Due_Date AND Period = "Daily" AND Due_Date <= ?',
        (new_daily_due_date, day_befor))
        # Reset Weekly Period Due_Date with new_weekly_due_date
        connection.execute('UPDATE habit SET Due_Date = ? WHERE Streak = Streak AND Period = "Weekly" AND Due_Date <= ?',
        (new_weekly_due_date, day_befor))

        print("\n!! Auto Reset successfully completed !!\n")
        sleep(0.01)