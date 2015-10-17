# sage: load ("page318a.sage")
# sage: z - a
# {2, 4, 6}
# sage: z - b
# {1, 2, 5, 7}
# sage: z - []
# {1, 2, 3, 4, 5, 6, 7}
# sage: a
# [1, 3, 5, 7]
# sage:

a = [1,3,5,7]
b = [3,4,6]
u = [1,2,3,4,5,6,7]
x = Set(a)
y = Set(b)
z = Set(u)
