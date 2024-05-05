#Lab Exercise No 6
#Programmed by: Mark Justine L. Apitan
#Course, Year and Section: BSCpE 1-3
#Instructor: Engr. Julius S. Cansino
#Date Submitted: May 5, 2024

# Import the TV class from the TV.py file
from TV import TV

# Create a TV object named tv1
tv1 = TV(30, 2, True)

# Display the current channel and volume level of tv1
print(f"tv1's channel is {tv1.getChannel()} and volume level is {tv1.getVolume()}")

# Create a TV object named tv2
tv2 = TV(8, 7, True)

# Display the current channel and volume level of tv2
print(f"tv2's channel is {tv2.getChannel()} and volume level is {tv2.getVolume()}")