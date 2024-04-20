#Lab Assignment No 4: Problem No. 4
#Programmed by: Montanez, Andrei Chayne D.:
#Course, Year and Section: BSCpE 1-3
#Instructor: Engr. Julius S. Cansino
#Date Submitted: April 20, 2024


def capitalize_last_name():
    try:
        name = input("Please enter your name: ")
        name_splitted = name.split()
        if len(name_splitted) != 2:
            raise ValueError
        else:
            if name_splitted[0].isalpha() == True or name_splitted[1].isalpha() ==True:
                raise TypeError
            else:
                first_name = f'{name_splitted[0][0].upper()}{name_splitted[0][1:].lower()}'
                last_name = f'{name_splitted[1].upper()}'
    except (ValueError, TypeError) as e:
        print(e)
    else:
        print(f'{first_name} {last_name}')

capitalize_last_name()