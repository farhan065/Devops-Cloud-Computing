# A list of various URLs to process
urls = [
    "https://api.github.com/v3",
    "http://www.google.com/search",
    "https://jenkins.internal.company.net/login",
    "ftp://fileserver.local/shared",
    "https://aws.amazon.com"
]

print(f"{'RAW URL':<45} | {'EXTRACTED DOMAIN'}")
print("-" * 65)

for url in urls:
    # 1. Split by "://" to remove protocol (https, http, ftp)
    # We use [-1] to ensure we get the part after the protocol, 
    # or the whole string if no protocol exists.
    stripped_protocol = url.split("://")[-1]
    
    # 2. Split by "/" to remove the path/route
    hostname = stripped_protocol.split("/")[0]
    
    # 3. Split by "." to analyze the parts of the domain
    domain_parts = hostname.split(".")
    
    # 4. Extract the Base Domain
    # Logic: If there are more than 2 parts (e.g. api.github.com), take the last 2.
    # If there are 2 or fewer (e.g. localhost), take the whole thing.
    if len(domain_parts) > 2:
        base_domain = ".".join(domain_parts[-2:])
    else:
        base_domain = hostname

    # Print formatted output
    print(f"{url:<45} | {base_domain}")