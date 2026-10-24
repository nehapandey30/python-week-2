class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(self.name,"is earting")
class Dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed=breed 
    def show_details(self):
        print("name",self.name)
        print("breed",self.breed) 


d=Dog("Tommy","Labrador")    
d.eat()
d.show_details()
                  