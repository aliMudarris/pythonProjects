# Simple Calculator by Ali Mudarris 2022

#This function adds two numbers
def add(x, y):
    return x + y
#This function substarcs two numbers
def subtract(x, y):
    return x - y
#This function multiplies two numbers
def multiply(x, y):
    return x * y
#This function divides two numbers
def divide(x, y):
    return x / y

print("Select operation: 1. ADD 2. SUB 3. MUL 4. DIV")

while True:
    #User choice
    choice = input("Enter choice [1,2,3,4]: ")

    #check choice
    if choice in('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        #Ask the user if they want to do another calculation

        next_cal = input("Want to do another calculation? y/n ")
        if next_cal =='y':
            continue
        
        else:
            break
