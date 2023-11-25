print("What operation")

print("1 Add")

print("2 Subtract")

print("3 Multiply")

print("4 Divide")

operation =  input("")

if operation == "1":
    Num1 = input("Whats number 1: ")
    Num2 = input("Whats number 2: ")
    print("The sum is " +str(int(Num1) + int(Num2) ))
elif operation == "2":
    Num1 = input("Whats number 1: ")
    Num2 = input("Whats number 2: ")
    print("The difference is " +str(int(Num1) - int(Num2) ))
elif operation == "3":
    Num1 = input("Whats number 1: ")
    Num2 = input("Whats number 2: ")
    print("The product is " +str(int(Num1) * int(Num2) ))
elif operation == "4":
    Num1 = input("Whats number 1: ")
    Num2 = input("Whats number 2: ")
    print("The quotient is " +str(int(Num1) / int(Num2) ))


