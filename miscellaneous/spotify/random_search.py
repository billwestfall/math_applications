import random, string
x = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
print(x)
