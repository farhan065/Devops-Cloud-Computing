# A tuple: immutable and efficient for lookups
DANGEROUS_PORTS = (21, 23, 445)

def check_ports(active_ports):
    print("--- Starting Port Audit ---")
    for port in active_ports:
        if port in DANGEROUS_PORTS:
            print(f"WARNING: Dangerous port {port} is active!")
        else:
            print(f"Safe: Port {port} is clear.")
    print("--- Audit Complete ---")