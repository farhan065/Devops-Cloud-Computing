import json

def process_server_data(json_string):
    try:
        # Parse the JSON string into a Python dictionary
        data = json.loads(json_string)
        
        # Access the list of servers using the 'servers' key
        servers = data.get("servers", [])
        
        print("--- System Health Report ---")
        for server in servers:
            name = server.get("name", "Unknown")
            status = server.get("status", "Unknown")
            print(f"Server: {name} | Status: {status}")
            
    except json.JSONDecodeError:
        # This triggers if the input string is not valid JSON
        print("Error: Failed to parse JSON. Please check the data format.")

# --- Test Data ---
mock_api = '{"servers": [{"name": "web-01", "status": "up"}, {"name": "db-01", "status": "down"}]}'

# Running the function
process_server_data(mock_api)

# Test with invalid JSON to see the error handler in action:
#process_server_data('{"servers": [{"name": "broken"}')