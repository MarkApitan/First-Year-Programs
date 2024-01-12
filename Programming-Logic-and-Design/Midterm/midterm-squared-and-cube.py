number = int(input("Enter a number:"))
letter = input("Enter a letter: (s/c)")

if letter.lower() == 's':
    print (number*number)
elif letter.lower()== 'c':
    print ((number*number)*number)
else:
    print ("Invalid Character!")