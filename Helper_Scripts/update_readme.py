#!/usr/bin/env python3

# Libraries
import sys
import os.path

# My libraries
from globals import print_v
from readme_file import ReadmeFile

# If script is run directly
if __name__ == '__main__':

    # Readme file path
    readme_file_path = "README.md"

    # When testing, look one folder higher for README instead
    if 'test' in sys.argv:
        readme_file_path = os.path.join("..", readme_file_path)
    
    # Print start message
    print_v("###### Update README by David ######", False)

    # Create ReadmeFile from path and exit with outcome
    sys.exit(ReadmeFile(readme_file_path))