# Playlist - Python
# by CodeChum Admin

# Create a class called Music having the following details:

# Class - Music:

# Public Properties:
# duration (type: int): Represents the duration of the music track in minutes.
# genre (type: str): Specifies the genre of the music.

# Constructor:
# __init__(self, duration: int = 0, genre: str = "Unknown", duration_type: str = "m"):
# This constructor can be used in two ways:
# When called with no parameters, it initializes duration to 0 and genre to "Unknown". 
# This provides a standard default state for the Music object when no specific details are given.
# When called with parameters, it sets the duration and genre properties based on the provided values. 
# Additionally, it accepts a duration_type string to indicate whether the duration is in minutes ('m'), hours ('h'), or days ('d'). 
# If duration_type is 'm' or not provided, the duration is assumed to be in minutes. 
# If duration_type is 'h', it converts hours to minutes, and if duration_type is 'd', it converts days to minutes before setting the duration property.

# Start typing your code
class Music:
    def __init__ (self, duration: int = 0, genre: str = "Unknown", duration_type: str = "m"):
        # Initialize the genre property with the provided genre value
        self.genre = genre
        # Initialize the duration_type property with the provided duration_type value
        self.duration_type = duration_type
        # Check the value of duration_type to determine how to set the duration property
        if duration_type == "h":
            # If duration_type is 'h', convert hours to minutes and set the duration property
            self.duration = duration * 60
        elif duration_type == "d":
            # If duration_type is 'd', convert days to minutes and set the duration property
            self.duration =  duration * 1440
        else:
            # If duration_type is not 'h' or 'd', assume duration is already in minutes and set the duration property
            self.duration = duration