from person import Person
from father import Father
from son import Son
# Testing Person class
person = Person("Alice", 30, "F")
print(person)  # Alice - 30 - F
print(person.is_minor())  # False
person.set_age(17)
print(person.is_minor())  # True

# Testing Father class
father = Father("John", 45)
print(father)  # John - 45 - M
father.introduce_with_style(4)
# I am your father
#  I am your father
#   I am your father
#    I am your father

# Testing Son class
son = Son("Jack", 15)
print(son)  # Jack - 15 - M
son.introduce_with_style(4)
#    I am your son
#   I am your son
#  I am your son
# I am your son

# Testing Son class with default name
unknown_son = Son()
print(unknown_son)  # Unknown - 0 - M