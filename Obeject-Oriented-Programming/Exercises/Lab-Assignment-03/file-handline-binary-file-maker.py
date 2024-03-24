#To import pickle
import pickle
#To define the students and their gwa
students = {
    "John": 1.25,
    "Alice": 3.00,
    "Bob": 2.00,
    "Emma": 2.0,
    "Michael": 2.25,
}

gwa={}
#To make the binary file
make = open('gwa.bin', 'wb')
pickle.dump(students, make)
make.close()