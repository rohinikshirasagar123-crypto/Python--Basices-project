import math

text=input()

words=set(text.split())

print(sorted(words))

print(math.pow(len(words),2))
