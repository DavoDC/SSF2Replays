#!/usr/bin/env python3

import subprocess
import globals

# Execute the update_readme.py script
exit_code = subprocess.call(['python', './update_readme.py', 'verbose', 'test'])

# Print the exit code
print(f"\nExit Code: {exit_code}")

# Print the meaning of the exit code
if exit_code == globals.SUCCESS:
    print("SUCCESS")
elif exit_code == globals.ERROR:
    print("ERROR")
elif exit_code == globals.UP_TO_DATE:
    print("UP_TO_DATE")
else:
    print("Unknown exit code")