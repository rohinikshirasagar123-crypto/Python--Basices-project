class Student:

    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.marks=[]

    def add_mark(self,mark):
        self.marks.append(mark)

    def get_average(self):
        return sum(self.marks)/len(self.marks)

    def display_info(self):
        print(self.name)
        print(self.roll)
        print(self.marks)
        print(self.get_average())


s=Student("Rohini",1)

s.add_mark(80)
s.add_mark(90)
s.add_mark(70)

s.display_info()
