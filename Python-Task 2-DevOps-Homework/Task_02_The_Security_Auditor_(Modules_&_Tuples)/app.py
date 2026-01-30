import scanner

# Our list of ports to scan
current_ports = [22, 80, 21, 443, 23, 8080]

# Call the function using the module prefix
scanner.check_ports(current_ports)