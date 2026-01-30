# Solution placeholder for Task 10: The Secret Masker
api_key = "AKIA1234567890EXAMPLE"

# Step 1: Slice the first 4 characters
# [:4] starts at 0 and stops before 4 (indices 0, 1, 2, 3)
visible_part = api_key[:4]

# Step 2: Create the mask
# Multiply the asterisk string by 10 to repeat it
mask = "*" * 10

# Step 3: Combine them
masked_key = visible_part + mask

print(f"Original: {api_key}")
print(f"Safe Log: {masked_key}")