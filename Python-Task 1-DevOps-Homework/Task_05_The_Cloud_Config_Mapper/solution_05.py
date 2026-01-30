# Solution placeholder for Task 5: The Cloud Config Mapper
# Initial state of the Virtual Machine (VM)

vm_config = {
    "id": "i-0a1b2c3d4e",
    "ip": "192.168.1.50",
    "status": "running",
    "region": "us-east-1"
}

print(f"Before Update: {vm_config}")

# Step 1: Update the status value
# Dictionaries are mutable, so we can change values directly by referencing the key.
vm_config["status"] = "stopped"

# Step 2: Add a new key-value pair
# If the key doesn't exist, Python creates it automatically.
vm_config["instance_type"] = "t3.large"

print(f"After Update:  {vm_config}")