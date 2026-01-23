# Solution placeholder for Task 9: The Path Builder
import os

base_dir = "/var/log"
app_name = "nginx"
filename = "access.log"

# Use os.path.join to intelligently combine them
# It automatically adds the correct separator (/ for Linux, \ for Windows)
full_path = os.path.join(base_dir, app_name, filename)

print(f"Constructed Path: {full_path}")