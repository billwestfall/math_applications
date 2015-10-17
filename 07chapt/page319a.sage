# sage: load ("page319a.sage")
# sage: X = Set(x).intersection(y)
# sage: X
# {6}
# sage: X = Set(x).intersection(z-y)
# sage: X
# {9, 3}
# sage:


a = [3,6,9]
b = [2,4,6,8]
u = [0..10]
x = Set(a)
y = Set(b)
z = Set(u)
