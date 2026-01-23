# Solution placeholder for Task 6: The Log File Duplicator

import shutil
import os

# 0. Setup: Let's create a dummy 'app.log' so this script actually runs for me.
# In a real scenario, this file would already exist.
with open("app.log", "w") as f:
    f.write("2023-10-27 ERROR: Connection timeout\n")

# Main Logic
original_file = "app.log"

# Check if the file exists to avoid errors
if os.path.exists(original_file):
    print(f"Found {original_file}. Starting duplication...")

    # Loop 5 times (1 to 5)
    for i in range(1, 6):
        # Create the new filename dynamically (e.g., app_1.log)
        new_filename = f"app_{i}.log"
        
        # Copy the file
        # shutil.copy(source, destination) preserves content
        shutil.copy(original_file, new_filename)
        
        print(f"Created: {new_filename}")
else:
    print(f"Error: {original_file} not found!")