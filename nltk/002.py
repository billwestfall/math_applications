from nltk.sem import Expression
read_expr = Expression.fromstring
p1 = read_expr('man(socrates)')
p2 = read_expr('all x.(man(x) -> mortal(x))')
c  = read_expr('mortal(socrates)')
Prover9().prove(c, [p1,p2])

TableauProver().prove(c, [p1,p2])

ResolutionProver().prove(c, [p1,p2], verbose=True)
