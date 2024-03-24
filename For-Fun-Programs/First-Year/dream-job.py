from itertools import cycle
from time import sleep

# Ask for user input
first_name = input("Enter your First Name: ")
last_name = input("Enter your Last Name: ")
dream_job = input("Enter your Dream Job: ") 

# Print sfx
print("\nInitializing . . . . .")

def progress(percent=0, width=30):
    left = width * percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']',
          f' {percent:.0f}%',
          sep='', end='', flush=True)

for i in range(101):
    progress(i)
    sleep(0.1)
    
# Print user info
print(f"\n\nHello, I am {first_name} {last_name}! My dream job is to become a {dream_job}.")