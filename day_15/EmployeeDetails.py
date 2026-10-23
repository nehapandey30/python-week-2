class Employee:
    company="Accenture"
    def __init__(self,name,salary,company="acenture"):
        self.name=name
        self.salary=salary
        self.company=company
    def display_details(self):
        print("name",self.name)
        print("salary",self.salary)
        print("Company:", self.company)
e1 = Employee("Neha", 67000,"google")
e2 = Employee("Rahul", 35000)

e1.display_details()
e2.display_details()        
