import random

print("Choose which die you want to roll (sides); 4,6,8,10,12,20:")

w = input()

x = int(w)

y = random.randint(1, x)

print(y)
