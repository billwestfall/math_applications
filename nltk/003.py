e1 = read_expr('exists x.P(x)')
print(e1)
e2 = e1.alpha_convert(Variable('z'))
print(e2)
print(e1 == e2)

l = read_expr(r'\X.\X.X(X)(1)').simplify()
id = read_expr(r'\X.X(X)')
print(l == id)
