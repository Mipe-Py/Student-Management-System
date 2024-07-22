import sys
import os
import time
import sqlite3
from management import Administration

def clear_console():
    """Clear terminal so the text will not be repeated"""

    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Unix (Linux, macOS)
    else:
        os.system('clear')

def timer():
    """Countdown for 3 second, then exit program"""

    timer = 3
    while timer != 0:
        print(f"Exit in.. {timer}")
        time.sleep(1)
        timer -= 1
        if timer == 0:
            sys.exit()

def view_list():  
    """Prints the selected items from the database table"""

    # Getting an absolute path to the "interface" folder
    current_dir = os.path.dirname(__file__)

    # Making path to the database in "data" folder
    db_path = os.path.join(current_dir, '..', 'data', 'database.db')

    # Connection with database
    conn = sqlite3.connect(db_path)

    # Create cursor
    c = conn.cursor()

    # Select all columns from table students
    c.execute('SELECT * FROM students' )

    # Load all results
    results = c.fetchall()

    # Title
    print("[ID][NAME][SUBEJCT[GRADE][RATING]")

    # Print our results
    for line in results:
        print(f"{line[0]} | {line[1]} | {line[2]} | {line[3]} | {line[4]}")

    # Close cursor and connection
    c.close()
    conn.close()

def select():
    """Allows input and interaction"""

    select = input("--> ").lower()
    print()

    if select == "1" or select == "add":
        x = input("Student: ")
        y = input("Subject: ")
        z = input("Grade: ")
        f = input("Rating: ")
        register = Administration(x, y, z, f)
        register.add()
        print()

    elif select == "2" or select == "show":
        view_list()
        print()

    elif select == "3" or select == "exit":
        timer()

    else:
        print("Error - Type a number or write text.")
        print()

    x = input("Return to menu? (y/n): ")
    if x == "y":
        clear_console()
    else:
        timer()
