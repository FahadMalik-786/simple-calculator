def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."
    
def modulus(x, y):
    return x % y


print("Welcome to the Calculator! ✨")
print("Available operations: +, -, *, /")


while True:
    x=   float(input ("Enter the value of x = "))
    op= input("Enter the oprator i.e + , -, * , / = ")
    y=   float(input( "Enter the value of y = "))

    if op=="+" :
        print("Result : " , add(x,y))
    elif op=="-":
        print("Result : " , subtract(x,y))
    elif op=="*":
        print("Result : " , multiply(x,y))
    elif op=="/":
        if y==0:
            print("Error! Division by zero")
        else:
            print("Result : " , divide(x,y))
    elif op=="%": 
         print("Result : " , modulus(x,y))
    else:
        print("Invalid Operation")
    

    again = input("Do you want to calculate again? (y/n): ")
    if again != 'y':
            break



