#Function with no argument & no return value.

def printLine():
    print("*"*50)
printLine()
print("Welcome To User Defined Function In Python")
printLine()

#Function with argument & no return value.

def add(a,b):
    print("Addition : ",a+b)

printLine()
x=int(input("Enter Value : "))
y=int(input("Enter Value : "))
add(x,y)
printLine()

#Function with argument & return value.

def sub(a,b):
    return a-b

printLine()
x=int(input("Enter Value : "))
y=int(input("Enter Value : "))
#ans=sub(x,y)
print("Subtraction : ",sub(x,y))
printLine()
