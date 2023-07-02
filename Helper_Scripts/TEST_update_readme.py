#!/usr/bin/env python3

# Libraries
import subprocess
import globals

# Execute README script
exit_code = subprocess.call(['python', './update_readme.py', 'verbose', 'test'])

# Print the exit code
print(f"\nExit Code: {exit_code} -> ", end="")

# Print the meaning of the exit code
if exit_code == globals.SUCCESS:
    print("SUCCESS")
elif exit_code == globals.ERROR:
    print("ERROR")
elif exit_code == globals.UP_TO_DATE:
    print("UP_TO_DATE")
else:
    print("Unknown exit code")