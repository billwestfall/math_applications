

x = var('p')
print ("[abs(p-4) == 2], p)")
print solve([(p-4) == 2], p)
print solve([abs(p-4) == 2], p)

x = var('x')
print ("[|(4*x - 3)| == |(x + 6)|], x)")
#print solve([(3*(a*x-5*a))+(4*b)==(4*x-2)], x)
print ((abs(4*(x)) - 3)==abs((x) + 6)).find_root(0,999,x)
print ((abs(4*(x)) - 3)==abs((x) + 6)).find_root(-999,0,x)
#print solve([(4*x)-3==(x + 6)], x)
#print solve([abs(4*(x)-3)==abs((x) + 6)], x)

x = var('x')
print ("[4*(x + 3) == 40+2*x], x)")
#print solve([(3*(a*x-5*a))+(4*b)==(4*x-2)], x)
print (4*(x + 3) == 40+2*x).find_root(0,999,x)
#print (4*(x + 3) == 40+2*x).find_root(-999,0,x)

x = var('x')
print ("[(80/x) == 180/(x + 50)], x)")
#print solve([(3*(a*x-5*a))+(4*b)==(4*x-2)], x)
print ((80/x) == 180/(x + 50)).find_root(-999,999,x)
#print (80 == x*(80/x)).find_root(-999,0,x)

x = var('x')
print ("[(0.06*x)+1260-(0.09*x) == 1005], x)")
print ((0.06*x)+1260-(0.09*x) == 1005).find_root(-9999,9999,x)

x = var('x')
print ("[((3*x)+5 == 20], x)")
print (((3*x)+5 == 20).find_root(-9999,9999,x))

x = var('x')
print ("[4-(5*x) == 9], x)")
print ((4-(5*x) == 9).find_root(-9999,9999,x))

x = var('x')
print ("[(0.06*(x))-0.3 == (0.5(x))+0.4], x)")
print (((0.06*(x))-0.3 == (0.5*(x))+0.4).find_root(-9999,9999,x))

x = var('x')
print ("[(2.5+5.04*(x)) == (8.5-0.06(x))], x)")
print (((2.5+5.04*(x)) == (8.5-0.06*(x))).find_root(-9999,9999,x))

x = var('x')
print ("[(((2/5)*x+(1/4)-(3*(x))) == (6/5))], x)")
print ((((2/5)*x+(1/4)-(3*(x))) == (6/5)).find_root(-9999,9999,x))

x = var('x')
print ("[(2/3)-((1/4)*x)==(3/2)+((1/3)*x)], x)")
print (((2/3)-((1/4)*x)==(3/2)+((1/3)*x)).find_root(-9999,9999,x))

x = var('x')
print ("[((2*x)-1)==(3*(x+1)+(7*x)+5)], x)")
print ((((2*x)-1)==(3*(x+1)+(7*x)+5)).find_root(-9999,9999,x))
