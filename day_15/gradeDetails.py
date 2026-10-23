class Students:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    def display_details(self):
        print("name",self.name)
        print("marks",self.marks)
    def is_pass(self):
        if self.marks>=33:
          return "pass"
        else:
            return "fail"
    def get_grade(self):
        if self.marks>=90:
            return "A"
        elif self.marks>=75:
                    return "B"
        elif self.marks>=55:
                    return "c"
        elif self.marks>=35:
                    return "D"
        else:
              return"Fail"
            
e1=Students("neha",90)
e2=Students("Nitya",80)
e3=Students("megha",87)
e4=Students("Aman",33)
e1.display_details()
print("result",e1.is_pass())
print("grade",e1.get_grade())
e2.display_details()
print("result",e2.is_pass())
print("grade",e2.get_grade())
e3.display_details()
print("result",e3.is_pass())
print("grade",e3.get_grade())
e4.display_details()
print("result",e4.is_pass())
print("grade",e4.get_grade())




