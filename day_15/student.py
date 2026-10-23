class Student:
    
  
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display_details(self):
        print("Name", self.name)
        print("MArks",self.marks)
e1=Student("Neha",88)
e2=Student("Rahul",98)


e1.display_details()        
e2.display_details() 