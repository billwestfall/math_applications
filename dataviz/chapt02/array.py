nums = range(10)

odd_squares = [x * x for x in nums if x%2]
d = sum(odd_squares)
print(d)
