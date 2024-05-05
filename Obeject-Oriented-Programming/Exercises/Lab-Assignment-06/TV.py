# Lab Exercise No 6
# Programmed by: Mark Justine L. Apitan
# Course, Year and Section: BSCpE 1-3
# Instructor: Engr. Julius S. Cansino
# Date Submitted: May 5, 2024

class TV:

    def __init__(self, channel=1, volumeLevel=1, on=False):
        # Construct TV Object
        if 1 <= channel <= 120:
            self.channel = channel
        else:
            self.channel = 1
        if 1 <= volumeLevel <= 7:
            self.volumelevel = volumeLevel
        else:
            self.volumelevel = 1
        self.on = on

    def turnOn(self):
        # Turn on the TV
        self.on = True

    def turnof(self):
        # Turn off the TV
        self.on = False

    def getChannel(self):
        # Get the current channel
        return self.channel

    def setChannel(self, channel):
        # Set the channel to a new value if within the valid range (1 to 120)
        if channel >= 1 and channel <= 120:
            self.channel = channel

    def getVolume(self):
        # Get the current volume level
        return self.volumelevel

    def setVolume(self, volumeLevel):
        # Set the volume level to a new value if within the valid range (1 to 7)
        if volumeLevel >= 1 and volumeLevel <= 7:
            self.volumelevel = volumeLevel

    def channelUp(self):
        # Increase the channel by 1, wrapping around to 1 if it exceeds 120
        if self.channel < 120:
            self.channel += 1
        else:
            self.channel = 1

    def channelDown(self):
        # Decrease the channel by 1, wrapping around to 120 if it goes below 1
        if self.channel > 1:
            self.channel -= 1
        else:
            self.channel = 120

    def VolumeUp(self):
        # Increase the volume level by 1, maxxed at 7
        if self.volumelevel < 7:
            self.volumelevel += 1
        else:
            self.volumelevel = 7

    def VolumeDown(self):
        # Decrease the volume level by 1, maxxed at 1
        if self.volumelevel < 1:
            self.volumelevel -= 1
        else:
            self.volumelevel = 1