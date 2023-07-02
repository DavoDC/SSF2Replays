#!/usr/bin/env python3

# Libraries
import sys
import os.path

# My libraries
from globals import printV
from readme_file import ReadmeFile

# Readme file path
readme_file_path = "README.md"

def main():
    # Print start message
    printV("###### Update README by David ######")

    # Create ReadmeFile from path
    ReadmeFile(readme_file_path)

if __name__ == '__main__':

    # When running directly for testing, look one folder higher for README instead
    if 'test' in sys.argv:
        readme_file_path = os.path.join("..", readme_file_path)
    
    sys.exit(main())