def fizzbuzz_checker(limit):
    # Iterate from 1 up to (and including) the limit
    for i in range(1, limit + 1):
        
        # Rule 1: Check if divisible by BOTH 3 and 5 first
        # If we checked for 3 or 5 individually first, we'd miss the "FizzBuzz" cases
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            
        # Rule 2: Check if divisible by 3
        elif i % 3 == 0:
            print("Fizz")
            
        # Rule 3: Check if divisible by 5
        elif i % 5 == 0:
            print("Buzz")
            
        # Rule 4: If none of the above, print the number
        else:
            print(i)

# Take user input for the limit
user_limit = int(input("Enter a positive number to count up to: "))



