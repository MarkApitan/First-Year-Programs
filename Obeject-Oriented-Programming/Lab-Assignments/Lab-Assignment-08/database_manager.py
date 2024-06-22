#Lab Activity No 7
#Programmed by: Mark Justine L. Apitan
#Course, Year and Section: BSCpE 1-3
#Instructor: Engr. Julius S. Cansino
#Date Submitted: June 22, 2024
import sqlite3
class MovieHouseDatabaseManager:
    def __init__ (self, database_file:str):
        self.__database_file = database_file

    def get_connection(self):
        # Establish a connection to the SQLite database
        conn = sqlite3.connect(f"{self.__database_file}")
        return conn
    
    def register_movie (self, title, genre, cost):
        try:
            conn = self.get_connection()
            c = conn.cursor()
            # Insert a new movie record into the 'movie' table
            c.execute("INSERT INTO movie (title, genre, cost) VALUES (?, ?, ?)", (title, genre, cost))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error registering movie: {e}")
            return False
        finally:
            if conn:
                conn.close()

    def remove_movie (self, id):
        conn = self.get_connection()
        c = conn.cursor()
        # Mark a movie as deleted in the 'movie' table
        c.execute("UPDATE movie SET is_deleted = 1 WHERE oid = ?", (id,))
        conn.commit()
        conn.close()

    def retrieve_movies(self, genres:list [str]):
        try:
            conn = self.get_connection()
            c = conn.cursor()
            if genres:
                # Retrieve movies from the 'movie' table based on specified genres
                query = "SELECT * FROM movie WHERE genre IN ({seq}) AND is_deleted = 0".format(seq=','.join(['?']*len(genres)))
                c.execute(query, genres)
            else:
                # Retrieve all movies from the 'movie' table
                c.execute("SELECT * FROM movie WHERE is_deleted = 0")
            movies = c.fetchall()
            return movies
        except sqlite3.Error as e:
            print(f"Error retrieving movies: {e}")
            return []
        finally:
            if conn:
                conn.close()
    
    def retrieve_rooms(self):
        conn = self.get_connection()
        c = conn.cursor()
        # Retrieve all rooms from the 'room' table
        c.execute ("SELECT * FROM room")
        rooms = c.fetchall()
        conn.close()
        return rooms
    
    def retrieve_record(self, room_id):
        try:
            conn = self.get_connection()
            c = conn.cursor()
            # Retrieve the latest room record for a specific room from the 'room_record' table
            c.execute("SELECT * FROM room_record WHERE room_id = ? AND is_finished = 0 ORDER BY id DESC LIMIT 1", (room_id,))
            record = c.fetchone()
            if record:
                # Retrieve the movies associated with the room record from the 'movie' table
                c.execute("SELECT m.* FROM movie m JOIN room_movie_record r ON m.id = r.movie_id WHERE r.room_record_id = ?", (record[0],))
                movies = c.fetchall()
                return {'record': record, 'movies': movies}
            return {'record': None, 'movies': []}
        except sqlite3.Error as e:
            print(f"Error retrieving record: {e}")
            return {'record': None, 'movies': []}
        finally:
            if conn:
                conn.close()        

    def check_in(self, room_id, movies):
        try:
            conn = self.get_connection()
            c = conn.cursor()
            # Calculate the total cost of the movies
            total_cost = sum(movie.get_cost() for movie in movies)
            # Insert a new room record into the 'room_record' table
            c.execute("INSERT INTO room_record (room_id, total_cost, is_finished) VALUES (?, ?, 0)", (room_id, total_cost))
            record_id = c.lastrowid
            for movie in movies:
                # Associate the movies with the room record in the 'room_movie_record' table
                c.execute("INSERT INTO room_movie_record (movie_id, room_record_id) VALUES (?, ?)", (movie.get_id(), record_id))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error during check-in: {e}")
            return False
        finally:
            if conn:
                conn.close()
    
    def check_out(self, id: int) -> bool:
        try:
            conn = self.get_connection()
            c = conn.cursor()
            # Mark a room record as finished in the 'room_record' table
            c.execute("UPDATE room_record SET is_finished = 1 WHERE id = ?", (id,))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error during check-out: {e}")
            return False
        finally:
            if conn:
                conn.close()