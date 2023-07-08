#!/usr/bin/env python3

# Libraries
import sys

# My libraries
from globals import *
from replay_line import ReplayLine

# Defines a class that represents the repo's README file
class ReadmeFile:
    def __init__(self, readme_file_path):
        # Content holder for new README content
        new_content = []

        # Flags for tracking replay line status
        replay_line_found = False
        replay_line_updated = False

        # Open README file in read mode and read in lines
        with open(readme_file_path, "r", newline='') as readme_file:
            lines = readme_file.readlines()

        # For each README line
        for curLine in lines:

            # If the line is a replay line
            if ReplayLine.is_replay_line(curLine):

                # Set found as true
                replay_line_found = True

                # Process line
                processed_line = process_replay_line(curLine)

                # If didn't exit, and line was definitely changed
                if processed_line != curLine:

                    # Set updated as true
                    replay_line_updated = True

                    # Replace current line
                    curLine = processed_line

            # Append line to content
            new_content.append(curLine)

        # If replay line was not found, notify and exit
        if not replay_line_found:
            handle_error("Replay line not found in README")

        # If replay line was updated:
        if replay_line_updated:

            # Open README file in write mode and write the new content to it
            with open(readme_file_path, "w", newline='') as readme_file:
                readme_file.writelines(new_content)

            # Notify about success and exit with a success code
            print_v("Successfully updated README!")
            sys.exit(SUCCESS)


def process_replay_line(replay_line):

    # Create ReplayLine with current repo state and date
    new_replay_line = ReplayLine()
    new_replay_line_str = new_replay_line.to_string()
    print("\nGenerated new line: " + new_replay_line_str)

    # If the given replay line is equivalent
    if ReplayLine(replay_line.strip('\r\n')) == new_replay_line:

        # Notify that already up-to-date
        print_v("Replay line is already up to date!")
        sys.exit(UP_TO_DATE)
    else:
        # Else if not equivalent, return updated line
        return new_replay_line_str + "\n"