import random, string
y = random.randint(5, 16)
x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in y)
print(x)
