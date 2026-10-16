a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
try:
    result=a/b
    print("the result is : " ,result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")