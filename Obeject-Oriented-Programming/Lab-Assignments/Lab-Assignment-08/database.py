#Lab Activity No 7
#Programmed by: Mark Justine L. Apitan
#Course, Year and Section: BSCpE 1-3
#Instructor: Engr. Julius S. Cansino
#Date Submitted: June 22, 2024
import sqlite3

# Connect to the database file
conn = sqlite3.connect('moviehouse.db')

# Create a cursor object to execute SQL commands
c = conn.cursor()

# Create the 'room' table with columns 'id' and 'cost'
c.execute('''
    CREATE TABLE room (
        id INTEGER PRIMARY KEY,
        cost REAL
    )
''')

# Create the 'movie' table with columns 'id', 'title', 'genre', 'is_deleted', and 'cost'
c.execute('''
    CREATE TABLE movie (
        id INTEGER PRIMARY KEY,
        title VARCHAR,
        genre VARCHAR,
        is_deleted TINYINT DEFAULT 0,
        cost REAL
    )
''')

# Create the 'room_record' table with columns 'id', 'room_id', 'total_cost', and 'is_finished'
c.execute('''
    CREATE TABLE room_record (
        id INTEGER PRIMARY KEY,
        room_id INTEGER FOREIGN KEY,
        total_cost REAL,
        is_finished TINYINT DEFAULT 0
    )
''')

# Create the 'room_movie_record' table with columns 'id', 'movie_id', and 'room_record_id'
c.execute('''
    CREATE TABLE room_movie_record (
        id INTEGER PRIMARY KEY,
        movie_id INTEGER FOREIGN KEY,
        room_record_id INTEGER FOREIGN KEY
    )
''')

# Commit the changes to the database
conn.commit()

# Close the connection to the database
conn.close()