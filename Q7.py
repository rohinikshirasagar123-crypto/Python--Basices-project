square=lambda x:x**2

numbers=range(1,21)

result=[]

for i in numbers:
    result.append(square(i))

print(result)

for i in result:

    if i%2==0:
        print(i)
