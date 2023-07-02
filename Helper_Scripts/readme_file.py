#!/usr/bin/env python3

# Libraries
import sys

# My libraries
from globals import *
from replay_line import ReplayLine

# Defines a class that represents the repo's README file
class ReadmeFile:
    def __init__(self, readme_file_path):
            
        # Create new ReplayLine
        newReplayLine = ReplayLine()
        printV("\nGenerated new line: " + newReplayLine.to_string())

        # New content holder
        updatedContent = ""

        # Flag to track if the replay line was found
        replayLineFound = False

        # Open README file in read mode
        with open(readme_file_path, "r") as readmeFile:

            # Iterate over lines, processing each
            for line in readmeFile:
                replayLineFound, updatedContent = process_line(line, newReplayLine, replayLineFound, updatedContent)

        # If the replay line was found
        if replayLineFound:

            # Open README file in write mode and write new content
            with open(readme_file_path, "w") as readmeFile:
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
    if ReplayLine.is_replay_line(line):

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