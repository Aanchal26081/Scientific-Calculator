import math

def add(a,b):
    return a + b
def subt(a,b):
    return a - b
def div(a,b):
    return a / b
def mult(a,b):
    return a * b
def sqrt(a):
    result = math.sqrt(a)
    return result
def exp(a):
    return a ** 2
def sin(x):
    result = math.sin(x)
    return result
def cos(x):
    result = math.cos(x)
    return result
def tan(x):
    result = math.tan(x)
    return result

print('''
Choose a number for the following operation
1. Addition(x,y)
2. Subtraction(x,y)
3. Divide(x,y)
4. Multiplication(x,y)
5. Square(x)
6. Square root(x)
7. sin(x)
8. cos(x)
9. tan(x)
''')

option = int(input("Which operation do u want to perform:\n"))

while option < 10:
    if option == 1:
        print("Enter the Parameters:\n")
        a1 = int(input("Enter a: "))
        b1 = int(input("Enter b: "))
        res1 = add(a1,b1)
        print("Addition = ", res1)

    elif option == 2:
        print("Enter the Parameters:\n")
        a2 = int(input("Enter a: "))
        b2 = int(input("Enter b: "))
        res2 = subt(a2,b2)
        print("Subtraction = ", res2)

    elif option == 3:
        print("Enter the Parameters:\n")
        a3 = int(input("Enter a: "))
        b3 = int(input("Enter b: "))
        res3 = div(a3,b3)
        print("Division = ", res3)

    elif option == 4:
        print("Enter the Parameters:\n")
        a4 = int(input("Enter a: "))
        b4 = int(input("Enter b: "))
        res4 = mult(a4,b4)
        print("Multiplication = ", res4)

    elif option == 5:
        print("Enter the Parameters:\n")
        a5 = int(input("Enter a: "))
        b5 = int(input("Enter b: "))
        res5 = exp(a5)
        print("Square = ", res5)

    elif option == 6:
        print("Enter the Parameters:\n")
        a6 = int(input("Enter a: "))
        res6 = sqrt(a6)
        print("Square root = ", res6)

    elif option == 7:
        print("Enter the Parameters:\n")
        a7 = int(input("Enter a: "))
        res7 = sin(a7)
        print("sin(x) = ", res7)

    elif option == 8:
        print("Enter the Parameters:\n")
        a8 = int(input("Enter a: "))
        res8 = cos(a8)
        print("cos(x) = ", res8)

    elif option == 9:
        print("Enter the Parameters:\n")
        a9 = int(input("Enter a: "))
        res9 = tan(a9)
        print("tan(x) = ", res9)

    else: 
        print("Choose another operation")
    
    new = int(input("Do you want to continue - (yes - 1) , (No - 0)\n"))
    if new  == 1:
        option = int(input("Enter the option"))
    elif new == 0:
        print("Thanks for using our scientific calculator")
        break
        