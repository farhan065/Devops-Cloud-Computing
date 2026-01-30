# Solution placeholder for Task 8: The Threshold Alert
cpu_load = 0.88

# Method 1: Basic Math + F-String
# Multiply by 100 first, then convert to int to drop decimals
percent_str = f"{int(cpu_load * 100)}%"
print(f"CPU Load (Basic): {percent_str}")

# Method 2: The "Pro" F-String Formatter
# Python f-strings have built-in percentage formatting!
# :.0% -> Format as percentage with 0 decimal places
formatted_alert = f"CPU Load is {cpu_load:.0%}"

print(f"Alert: {formatted_alert}")