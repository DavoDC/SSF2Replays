#!/usr/bin/env python3

# Requirements: Python 3.8
# Run using: clear && python3 updateREADME.py 'verbose'

# Imports
import os
import sys
from ReplayLine import ReplayLine

# Exit codes
SUCCESS = 0
ERROR = 1
UP_TO_DATE = 2

# Readme file path
README_FILE_PATH = "README.md"


def main():
    # Start message
    printV("###### Update README by David ######")

    # Create new ReplayLine
    newReplayLine = ReplayLine()
    printV("\nGenerated new line: " + newReplayLine.to_string())

    # New content holder
    updatedContent = ""

    # Flag to track if the replay line is found
    replayLineFound = False

    # Open README file in read mode
    with open(README_FILE_PATH, "r") as readmeFile:

        # Iterate over lines, processing each
        for line in readmeFile:
            replayLineFound, updatedContent = process_line(line, newReplayLine, replayLineFound, updatedContent)

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


def process_line(line, newReplayLine, replayLineFound, updatedContent):

    # If the given line is the replay line of the README file
    if ReplayLine.isReplayLine(line):

        # If the replay line matches the new one
        if ReplayLine(line) == newReplayLine:

            # Notify and exit with up-to-date code
            printV("\nReplay line is already up to date!")
            sys.exit(UP_TO_DATE)
        else:
            # Else if replay line needs updating:
            # Convert new line to string
            newReplayLineS = newReplayLine.to_string()

            # Always print out new line
            print("New line: " + newReplayLineS)

            # Append new line to content instead of old line
            updatedContent += newReplayLineS + "\n"

            # Set the flag to indicate that the replay line is found
            replayLineFound = True
    else:
        # For normal lines, just append as-is
        updatedContent += line

    return replayLineFound, updatedContent


# Helper function to print message if 'verbose' is given as an argument
def printV(message):
    if 'verbose' in sys.argv:
        print(message)


# If file is run from the command line:
if __name__ == '__main__':
    # Run main and exit
    sys.exit(main())