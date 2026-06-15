print("\n-----WELCOME TO THE BASIC CALCULATOR-----\n")

Num1 = float(input("Enter The First Number:"))
Num2 = float(input("Enter The Second Number:"))

operation = input("Enter The Operation To Perform (+, -, *, /, %): ")

if operation == "+":
    print("Result:", Num1 + Num2)

elif operation == "-":
    print("Result:", Num1 - Num2)

elif operation == "*":
    print("Result:", Num1 * Num2)
    
elif operation == "/":
    if Num2 == 0:
        print("Invalid")
    else:
        print("Result:", Num1 / Num2)

elif operation == "%":
    if Num2 == 0:
        print("Invalid")
    else:
        print("Result:", Num1 % Num2)

else:
    print("Invalid")