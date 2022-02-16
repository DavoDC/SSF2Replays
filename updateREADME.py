#!/usr/bin/env python3

# Name: Update README
# Authors: David 
# Last Update: 02 FEB 2022
# Requirements: Python 3.8
# Run using: clear && python3 updateREADME.py
# Run in: SSF2Replays folder/repo


# Import modules
import os
import sys
from pathlib import Path


# Main function
def main(arguments):

    # Print
    print("###### UPDATE README by David ######")

    # Get directory that script is running in
    runPath = os.path.abspath(os.path.dirname(__file__))

    # Get file and folder paths there
    paths = [os.path.abspath(x) for x in os.listdir(runPath)]

    # Replay directories holder
    replayDirs = list()

    # For each file/folder path
    for curPath in paths:

        # Convert to string
        curPathS = str(curPath)

        # Check that path is not an un-needed path
        check1 = 'README' not in curPathS
        check2 = '.git' not in curPathS

        # If directory passes checks (i.e. it is needed)
        if(check1 and check2):

            # Add to replay directories list
            replayDirs.append(curPathS)

    # Replay count holder
    replayCount = 0

    # For each replay directory
    for replayPathS in replayDirs:

        # Iterate that directory
        for root, dirs, files in os.walk(replayPathS):

            # For each file found
            for file in files:

                    # If has replay extension
                    if file.endswith('.ssfrec'):

                            # Add to replay count
                            replayCount += 1


    # Open readme file for reading and writing
    readmeFile = open("README.md", "r+")

    # test
    for line in readmeFile.readlines():
        print(line)

    # get lines
    # get replay line index
    # regenerate that line
    # put back
    # write back

    # Close readme file
    readmeFile.close()
    



# If file is run from the command line:
if __name__ == '__main__':

    # Run main function with arguments then exit
    sys.exit(main(sys.argv[1:]))