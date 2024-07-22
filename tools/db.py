import sqlite3
import os

def create_database(db_name="database.db"):
    """Check and create folder, database, table (if not created before)"""

    # Getting an absolute path to the "data" folder
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
    
    # Make sure that "data" folder already exists
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # Making path to the database
    db_path = os.path.join(base_dir, db_name)
    
    # Connection with database (create new database, if it does not exist)
    con = sqlite3.connect(db_path)

    # Create cursor for executing SQL commands
    cursor = con.cursor()

    # SQL statement to create a table
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student TEXT NOT NULL,
        subject TEXT NOT NULL,
        grade TEXT NOT NULL,
        rating TEXT NOT NULL
    );
    '''
    
    # Create table
    cursor.execute(create_table_query)
    
    # Save changes and close connection
    con.commit()
    con.close()