# Solution placeholder for Task 4: The Fleet Inventory


servers = ["web01", "db01", "app01", "web02"]

# Goal: Get the first and last items using slicing
# servers[:1]  -> Gets the first item as a list ['web01']
# servers[-1:] -> Gets the last item as a list ['web02']
web_servers = servers[:1] + servers[-1:]

print(f"Full Fleet: {servers}")
print(f"Target Servers: {web_servers}")