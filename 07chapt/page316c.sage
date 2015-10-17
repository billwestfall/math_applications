# sage: load ("page316c.sage")
# sage: list(x.subsets())
# [{}, {8}, {7}, {8, 7}]
# sage: list(y.subsets())
# [{}, {'a'}, {'c'}, {'b'}, {'a', 'c'}, {'a', 'b'}, {'c', 'b'}, {'a', 'c', 'b'}]
# sage:

a = [7,8]
b = ["a","b","c"]
x = Set(a)
y = Set(b)
