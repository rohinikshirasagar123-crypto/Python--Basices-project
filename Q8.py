class Employee:

    def __init__(self,id,name,details):

        self.id=id
        self.name=name
        self.details=details

    def show_details(self):

        print(self.id)
        print(self.name)
        print(self.details)


emp={}

for i in range(3):

    id=input()
    name=input()
    dep=input()
    sal=input()

    emp[id]=Employee(
        id,
        name,
        (dep,sal)
    )

for i in emp.values():

    i.show_details()
