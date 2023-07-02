#!/usr/bin/env python3

# Libraries
import sys

# Exit codes
SUCCESS = 0
ERROR = 1
UP_TO_DATE = 2

# Global printing function
def printV(message):
    if 'verbose' in sys.argv:
        print(message)