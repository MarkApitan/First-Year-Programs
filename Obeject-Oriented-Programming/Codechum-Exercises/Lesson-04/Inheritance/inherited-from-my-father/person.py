class Person ():
    def __init__(self, name: str, age: int, gender: str):
        self.__name = name
        self.__age = age
        self.__gender = gender
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.__age = age
    def set_gender(self, gender):
        self.__gender = gender
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_gender(self):
        return self.__gender
    def is_minor(self):
        if self.__age < 18:
            return True
    def __str__(self):
        return f"{self.__name} - {self.__age} - {self.__gender}"