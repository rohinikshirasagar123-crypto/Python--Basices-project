import random
import math

nums=set()

for i in range(10):

    nums.add(int(input()))

t=tuple(nums)

print(t)

print(random.sample(t,3))

print(math.sqrt(sum(t)))
