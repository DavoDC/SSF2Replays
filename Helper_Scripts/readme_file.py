#!/usr/bin/env python3

# Libraries
import sys

# My libraries
from globals import *
from replay_line import ReplayLine

# Defines a class that represents the repo's README file
class ReadmeFile:
    def __init__(self, readme_file_path):
            
        # Create a new ReplayLine and notify
        new_replay_line = ReplayLine()
        printV("\nGenerated new line: " + new_replay_line.to_string())

        # Open README file in read mode
        with open(readme_file_path, "r") as readme_file:

            # Read all lines from the README file
            lines = readme_file.readlines()

        # Process the lines to find and update the replay line
        replay_line_updated, updated_content = self.process_lines(lines, new_replay_line)

        # If the replay line was found and updated
        if replay_line_updated:

            # Open README file in write mode and write the updated content
            with open(readme_file_path, "w") as readme_file:
                readme_file.writelines(updated_content)

            # Notify about success and exit with a success code
            printV("\nSuccessfully updated README!")
            sys.exit(SUCCESS)
        else:
            # Else if not found, notify and exit with an error code
            printV("\nERROR! Replay line not found in README.")
            sys.exit(ERROR)

    @staticmethod
    def process_lines(lines, new_replay_line):
        # Content holder for updated README content
        updated_content = []

        # Flag to track if the replay line was found and updated
        replay_line_updated = False

        # Iterate over lines, processing each
        for line in lines:

            # If this is the replay line
            if ReplayLine.is_replay_line(line):

                # If equivalent to new one
                if ReplayLine(line) == new_replay_line:

                    # Notify and exit with an up-to-date code
                    printV("\nReplay line is already up to date!")
                    sys.exit(UP_TO_DATE)
                else:
                    # Else if the replay line needs updating:
                    # Convert the new line to a string
                    new_replay_line_str = new_replay_line.to_string()

                    # Always print out the new line
                    print("New line: " + new_replay_line_str)

                    # Append the new line to the content instead of the old line
                    updated_content.append(new_replay_line_str + "\n")

                    # Set the flag to indicate that the replay line is found and updated
                    replay_line_updated = True
            else:
                # For normal lines, just append as-is
                updated_content.append(line)

        return replay_line_updated, updated_content