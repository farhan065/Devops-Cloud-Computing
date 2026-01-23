# The raw user input with mixed case and extra spaces
raw_name = "  My Project Backup  "

# Step 1: Strip leading and trailing whitespace
# "  My Project Backup  " -> "My Project Backup"
stripped_name = raw_name.strip()

# Step 2: Convert to lowercase
# "My Project Backup" -> "my project backup"
lowercase_name = stripped_name.lower()

# Step 3: Replace spaces with hyphens
# "my project backup" -> "my-project-backup"
sanitized_name = lowercase_name.replace(" ", "-")

print(f"Original Input: '{raw_name}'")
print(f"Sanitized Name: '{sanitized_name}'")