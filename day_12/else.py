try:
    num1=int(input("Enter a number: "))
    num2=int(input("Enter another number: "))
    a=num1/num2
    print("the result is: ", a)
except Exception as e:
    print(e)
    # this block will execute if there is no exception
else:
    print("No error occurred.")