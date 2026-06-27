students={}

while True:

    print("1 Add")
    print("2 Search")
    print("3 Display")
    print("4 Exit")

    ch=input()

    if ch=="1":

        roll=input("Roll:")

        students[roll]={
            "name":input("Name:"),
            "age":input("Age:")
        }

    elif ch=="2":

        roll=input()

        print(students.get(roll,"Not Found"))

    elif ch=="3":

        print(students)

    elif ch=="4":

        break
