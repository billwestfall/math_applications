import random
z = random.randint(1, 2)
w = random.sample(random.randint(1, 2), 2)
v = random.sample(random.randint(1, 2), 2)
u = random.sample(random.randint(1, 2), 2)
t = random.sample(random.randint(1, 2), 2)

A = [[w], [v]]
B = [A[0][1]]
print(A)
print(B)
