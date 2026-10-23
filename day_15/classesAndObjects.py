class Employee:
    company="HP"
    def get_salary(self):  
        # self is important here because self is a way to reference the object to the class which is being created
        return 27000



e1=Employee()  
# an object of class employee is created here 
print(e1.get_salary())  
# employee e's get salary method is called


e2=Employee()
print(e2.get_salary())

print(e2.company)
