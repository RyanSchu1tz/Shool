while True:
    print("x ? y = z")
    print("'1' for addition,")
    print("'2' for subtraction")
    print("'3' for multiplication")
    print("'4' for division")
    print("'5' to exit program")
    choice = input()
    choice = int(choice)
    if choice == 1:
        print("x + y = z")
        print("Enter the number for x:")
        one = input()
        one = int(one)
        print("Enter the number for y:")
        two = input()
        two = int(two)
        three = (one + two)
        print("z = ",three)
    elif choice == 2:
        print("x - y = z")
        print("Enter the number for x:")
        one = input()
        one = int(one)
        print("Enter the number for y:")
        two = input()
        two = int(two)
        three = (one - two)
        print("z = ",three)
    elif choice == 3:
        print("x * y = z")
        print("Enter the number for x:")
        one = input()
        one = int(one)
        print("Enter the number for y:")
        two = input()
        two = int(two)
        three = (one * two)
        print("z = ",three)
    elif choice == 4:
        print("x / y = z")
        print("Enter the number for x:")
        one = input()
        one = int(one)
        print("Enter the number for y:")
        two = input()
        two = int(two)
        three = (one / two)
        print("z = ",three)
    else:
        break
    
    print("would you like repeat yes or no")
    rep = input()
        
    if rep == "no":
        break
    else:
        print("repeat")
        

