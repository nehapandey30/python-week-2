try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    print("result is: ", a/b)
except Exception as e:
    print(e)
# this is always executed whether exception occurs or not
finally:
    print("This will always execute.")
    