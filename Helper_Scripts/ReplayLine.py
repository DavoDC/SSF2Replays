#!/usr/bin/env python3

# Imports
import os
import sys
import datetime

# Constants
COUNT_PLACEHOLDER = "NUM"
DATE_PLACEHOLDER = "DATE"
TEMPLATE_STRING = f"### Replay Count = {COUNT_PLACEHOLDER} (as of {DATE_PLACEHOLDER})"

# Defines a class that represents a replay count line in the README file
class ReplayLine:

    # Construct a replay line from a string or nothing
    def __init__(self, replayLine=None):

        # If string provided
        if replayLine:
            # Split into parts and save
            parts = replayLine.split("= ")[1].split(" (as of ")
            self.replayCount = int(parts[0])
            self.date = parts[1].rstrip(")\n")
        else:
            # Else if nothing provided, generate current values and save
            self.date = datetime.datetime.today().strftime('%d/%m/%y')
            
            ### Scan repo to get replay count
            # Get parent folder of script folder
            scriptPath = os.path.abspath(os.path.dirname(__file__))
            replayPath = os.path.dirname(scriptPath)

            # Get all file paths with the .ssfrec extension
            # in the current directory and its subdirectories,
            # excluding the .git folder
            replayFiles = [
                os.path.join(root, file)
                for root, dirs, files in os.walk(replayPath)
                if '.git' not in root
                for file in files
                if file.endswith('.ssfrec')
            ]

            # The replay count is the number of .ssfrec paths
            self.replayCount = len(replayFiles)

            # If none found, notify and stop
            if self.replayCount == 0:
                print("\nERROR! No replays found!")
                sys.exit(1)

    # Get a string representation of the object
    def to_string(self):
        result = TEMPLATE_STRING
        result = result.replace(COUNT_PLACEHOLDER, str(self.replayCount))
        result = result.replace(DATE_PLACEHOLDER, str(self.date))
        return result

    # Returns true if the given string is in the replay line format
    @staticmethod
    def is_replay_line(replayLineS):
        return replayLineS.startswith(TEMPLATE_STRING.split(" = ")[0])
    
    # Override equality operator to compare using replay count number only
    def __eq__(self, other):
        if isinstance(other, ReplayLine):
            return self.replayCount == other.replayCount
        return False

