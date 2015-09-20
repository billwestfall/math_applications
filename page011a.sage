x = var('x')
print ("[2*x + 1 == 19], x)")
print solve([2*x + 1 == 19], x)

x = var('x')
print ("[5*x - 3 == 12], x)")
print solve([5*x - 3 == 12], x)

x = var('x')
print ("[2*x + 3(x - 4) == 2*(x-3)], x)")
print solve([2*x + 3*(x - 4) == 2*(x-3)], x)

x = var('x')
print ("[(42.19*x + 121.34) == (16.83*x) + 19.15], x)")
print find_root((42.19*x+121.34)==(16.83*x)+19.15,-100,100)
