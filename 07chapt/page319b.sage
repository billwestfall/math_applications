# sage: load ("page319b.sage")
# sage: Set(x).union(Set(y))
# {1, 3, 5, 6, 7, 9, 11, 12}
# sage: j = Set(x).union(Set(y))
# sage: k = zz - z
# sage: j.intersection(k)
# {9, 11, 12, 6, 7}
# sage:


a = [1,3,5,7,9,11]
b = [3,6,9,12]
c = [1,2,3,4,5]
u = [0..12]
x = Set(a)
y = Set(b)
z = Set(c)
zz = Set(u)
