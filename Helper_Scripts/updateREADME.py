#!/usr/bin/env python3

# Name: Update README
# Author: David
# Requirements: Python 3.8
# Run using: clear && python3 updateREADME.py

import os
import sys
import datetime

# Constants for exit codes
SUCCESS = 0
ERROR = 1
UP_TO_DATE = 2

# String constants
REPLAY_COUNT_PLACEHOLDER = "NUM"
DATE_PLACEHOLDER = "DATE"
TEMPLATE_STRING = f"### Replay Count = {REPLAY_COUNT_PLACEHOLDER} (as of {DATE_PLACEHOLDER})"
README_FILE_PATH = "README.md"



def main():
    # Start message
    printV("###### Update README by David ######")

    # Get new replay count line
    newLine = getNewReplayCountLine()

    # Update current replay count line
    updateReplayCountLine(newLine)



def getNewReplayCountLine():
    # Initialize template
    newReplayLine = TEMPLATE_STRING

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
    replayCount = len(replayFiles)

    # If none found, notify and stop
    if replayCount == 0:
        printV("\nERROR! No replays found!")
        sys.exit(ERROR)

    # Replace replay count
    newReplayLine = newReplayLine.replace(REPLAY_COUNT_PLACEHOLDER, str(replayCount))

    # Replace date
    dateS = datetime.datetime.today().strftime('%d/%m/%y')
    newReplayLine = newReplayLine.replace(DATE_PLACEHOLDER, str(dateS))

    # Notify and return
    printV("\nGenerated new line: " + newReplayLine)
    return newReplayLine



def updateReplayCountLine(newReplayLine):
    # New content holder
    updatedContent = ""

    # Flag to track if the replay line is found
    replayLineFound = False

    # Open README file in read mode and iterate over lines
    with open(README_FILE_PATH, "r") as readmeFile:
        for line in readmeFile:

            # If the line starts with part of the template
            if line.startswith(TEMPLATE_STRING.split(" = ")[0]):

                # If line matches
                if line.strip() == newReplayLine:

                    # Notify and exit with up-to-date code
                    printV("\nReplay line is already up to date!")
                    sys.exit(UP_TO_DATE)
                
                # Else if replay line needs updating:

                # ALWAYS print out new line
                print("New line: " + newReplayLine)

                # Append the new replay line instead
                updatedContent += newReplayLine + "\n"

                # Set the flag to indicate that the replay line is found
                replayLineFound = True
            else:
                # For normal lines, just append
                updatedContent += line

    # If the replay line is found
    if replayLineFound:

        # Open README file in write mode and write new content
        with open(README_FILE_PATH, "w") as readmeFile:
            readmeFile.write(updatedContent)

        # Notify about success and exit with success code
        printV("\nSuccessfully updated README!")
        sys.exit(SUCCESS)
    else:
        # Else if not found, notify and exit with error code
        printV("\nERROR! Replay line not found in README.")
        sys.exit(ERROR)



# Helper function to print message if 'verbose' is given as an argument
def printV(message):
    if 'verbose' in sys.argv:
        print(message)



# If file is run from the command line:
if __name__ == '__main__':
    # Run main and exit
    sys.exit(main())