#!/usr/bin/env python3

# Imports
import datetime

# Constants
COUNT_PLACEHOLDER = "NUM"
DATE_PLACEHOLDER = "DATE"
TEMPLATE_STRING = f"### Replay Count = {COUNT_PLACEHOLDER} (as of {DATE_PLACEHOLDER})"

# Defines a class that represents a replay count line in the README file
class ReplayLine:

    # Construct a replay line from a string or number
    def __init__(self, replayLine=None, replayCount=None):

        # If string provided
        if replayLine:
            # Split into parts and save
            parts = replayLine.split("= ")[1].split(" (as of ")
            self.replayCount = int(parts[0])
            self.date = parts[1].rstrip(")\n")
        elif replayCount:
            # Else if number provided, save it and use current date as date.
            self.replayCount = replayCount
            self.date = datetime.datetime.today().strftime('%d/%m/%y')

    # Get the replay count number
    def get_count(self):
        return self.replayCount
    
    # Get a string representation of the object
    def to_string(self):
        result = TEMPLATE_STRING
        result = result.replace(COUNT_PLACEHOLDER, str(self.replayCount))
        result = result.replace(DATE_PLACEHOLDER, str(self.date))
        return result

    # Override equality operator to compare using replay count number only
    def __eq__(self, other):
        if isinstance(other, ReplayLine):
            return self.replayCount == other.replayCount
        return False

    # Returns true if the given string is in the replay line format
    @staticmethod
    def isReplayLine(replayLineS):
        return replayLineS.startswith(TEMPLATE_STRING.split(" = ")[0])
