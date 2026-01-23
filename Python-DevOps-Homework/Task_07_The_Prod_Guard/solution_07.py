# Solution placeholder for Task 7: The Prod Guard

# The current environment context
# Try changing this to "dev" or "staging" to see the other result
env = "production"

# Logic: Check if we are allowed to delete
# != means "Not Equal To"
if env != "production":
    print("Executing Delete...")
    # perform_deletion()
else:
    print("Access Denied: Cannot delete in Prod!")