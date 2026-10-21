while True:
    try:
        a=int(input("Enter a number: "))
        b=int(input("Enter another number: "))
        print("the result is : " ,a+b)
    except Exception as e:
        print("Error: Please enter valid numbers.",e)