# Solution placeholder for Task 3: The Port Validator

port_str = "8080"

# Step 1: Convert the string input to an integer
# We assume the input contains digits. If it contains letters, this line will error.
port_num = int(port_str)

# Step 2: Check if the number is within the standard port range (1 to 65535)
if 1 <= port_num <= 65535:
    print(f"Port {port_num} is Valid.")
else:
    print(f"Port {port_num} is Invalid (Out of range).")