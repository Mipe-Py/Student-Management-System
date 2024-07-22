import sqlite3
import os

class Administration():
    """ 
	Class representing the logic of passing information to the database 
	
	Attributes: 
	---------- 
	student : str 
		Student name 
	subject : str 
		Subject 
	grade : str 
		Grade 
    rating : str
        Rating
	"""
    def __init__(self, student, subject, grade, rating):
        self.student = student
        self.subject = subject
        self.grade = grade
        self.rating = rating
    

    def add(self):
        """Takes data from the class Administration attributes and inserts it into the database."""

        # Getting an absolute path to the "management" folder
        current_dir = os.path.dirname(__file__)  

        # Create a path to the database in the "data" folder
        db_path = os.path.join(current_dir, '..', 'data', 'database.db')

        # Connecting to database
        conn = sqlite3.connect(db_path)  

        # Create cursor
        cursor = conn.cursor()  

        # Inserting student, subject, grade, rating into table
        cursor.execute('''
        INSERT INTO students (student, subject, grade, rating) VALUES (?, ?, ?, ?)
        ''', (self.student, self.subject, self.grade, self.rating))

        # Save changes, close cursor and close connection with database
        conn.commit()
        cursor.close()
        conn.close()