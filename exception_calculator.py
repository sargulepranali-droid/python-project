try:
    num1 = int(input("enter first number:"))
    num2 = int(input("enter second number:"))
    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")
    choice = int(input("enter choice:"))
    if choice == 1:
        print("answer = ", num1 + num2)
    elif choice == 2:
        print("answer =", num1 - num2)
    elif choice == 3:
        print("answer = ", num1 * num2)
    elif choice == 4:
        print("answer = ", num1 / num2)
    else:
        print("invalid choice")
except ValueError:
    print("please enter number only")        
except ZeroDivisionError:
    print("cannot divide by zero")
finally:
    print ("thank you")