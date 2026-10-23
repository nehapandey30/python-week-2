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
e1=Students("neha",90)
e2=Students("Nitya",80)
e3=Students("megha",87)
e1.display_details()
print("result",e1.is_pass())
e2.display_details()
print("result",e2.is_pass())
e3.display_details()
print("result",e3.is_pass())



