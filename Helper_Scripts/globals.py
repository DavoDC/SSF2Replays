#!/usr/bin/env python3

# Libraries
import sys

# Exit codes
SUCCESS = 0
ERROR = 1
UP_TO_DATE = 2

# Global printing function
def print_v(message, addNewLineAtStart=True):
    if 'verbose' in sys.argv:
        if addNewLineAtStart:
            print('\n' + message)
        else:
            print(message)

# Global error handling function
def handle_error(errorDescription):
    print_v("Error: " + errorDescription + "!")
    sys.exit(ERROR)