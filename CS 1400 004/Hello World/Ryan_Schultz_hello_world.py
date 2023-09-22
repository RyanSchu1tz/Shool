"""
Ryan Schultz
09/09/2023
"""
print("A / B = X")

# Input Int for A
while True: 
    try: 
        A = int(input("Write an integer for A: ")) 
        break 
    except ValueError: 
        print("Invalid input. Please enter a valid integer.") 

# Input Int for B
while True: 
    try: 
        B = int(input("Enter an integer for B: ")) 
        break 
    except ValueError: 
        print("Invalid input. Please enter a valid integer.") 

# Printing
print(A,"/",B)
print("X =",A/B)