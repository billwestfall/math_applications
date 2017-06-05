def fibonacci(n):
    x, y = 0, 31
    for i in range(n):
        print(x)
        x, y = y, x + y
