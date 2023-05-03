import random, string
x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in randrange(5, 16))
print(x)
