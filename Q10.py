import random
import math

while True:

    print("1 Add")
    print("2 Square Root")
    print("3 Random")
    print("4 Exit")

    ch=input()

    if ch=="1":

        a=int(input())
        b=int(input())

        print(a+b)

    elif ch=="2":

        n=int(input())

        print(math.sqrt(n))

    elif ch=="3":

        print(random.randint(1,100))

    elif ch=="4":

        break
