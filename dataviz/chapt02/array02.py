x = range(10)

def is_odd(x):
    return x%2

def sq(x):
    return x * x

d = sum([sq(x) for x in l if is_odd(x)])
print(d)
