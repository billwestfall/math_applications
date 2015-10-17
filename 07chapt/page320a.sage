# sage: load ("page320a.sage")
# sage: zz - x
# {'ATT', 'Hershey', 'Pepsi', 'GenMills'}
# sage: x.intersection(z)
# {'IBM'}
# sage: x.union(y)
# {'IBM', 'Chevron', 'Hershey'}
# sage:


a = ["Chevron","IBM"]
b = ["Chevron", "Hershey"]
c = ["ATT", "IBM"]
u = ["ATT", "Chevron", "GenMills", "Hershey", "IBM", "Pepsi"]
x = Set(a)
y = Set(b)
z = Set(c)
zz = Set(u)
