#Lab Activity No 7
#Programmed by: Mark Justine L. Apitan
#Course, Year and Section: BSCpE 1-3
#Instructor: Engr. Julius S. Cansino
#Date Submitted: June 22, 2024

# Define the Movie class
class Movie:
    def __init__(self, id, title, genre, cost):
        self.__id = id
        self.__title = title
        self.__genre = genre
        self.__cost = cost

    def get_oid(self):
        return self.__id

    def set_oid(self, id):
        self.__id = id

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_genre(self):
        return self.__genre

    def set_genre(self, genre):
        self.__genre = genre

    def get_cost(self):
        return self.__cost

    def set_cost(self, cost):
        self.__cost = cost

    def __str__(self):
        return f"{self.__id} - {self.__title}"

# Define the Room class
class Room:
    def __init__(self, id, cost):
        self.__id = id
        self.__cost = cost

    def get_oid(self):
        return self.__id

    def set_oid(self, id):
        self.__id = id

    def get_cost(self):
        return self.__cost

    def set_cost(self, cost):
        self.__cost = cost

# Define the Record class
class Record:
    def __init__(self, id, room_id, total_cost, movies):
        self.__id = id
        self.__room_id = room_id
        self.__total_cost = total_cost
        self.__movies = movies

    def get_oid(self):
        return self.__id

    def set_oid(self, id):
        self.__id = id

    def get_room_id(self):
        return self.__room_id

    def set_room_id(self, room_id):
        self.__room_id = room_id

    def get_total_cost(self):
        return self.__total_cost

    def set_total_cost(self, total_cost):
        self.__total_cost = total_cost

    def get_movies(self):
        return self.__movies

    def set_movies(self, movies):
        self.__movies = movies