# sage: load ("page317a.sage")
# sage: list(x.subsets())
# [{},
#  {3},
#  {4},
#  {5},
#  {6},
#  {7},
#  {3, 4},
#  {3, 5},
#  {3, 6},
#  {3, 7},
#  {4, 5},
#  {4, 6},
#  {4, 7},
#  {5, 6},
#  {5, 7},
#  {6, 7},
#  {3, 4, 5},
#  {3, 4, 6},
#  {3, 4, 7},
#  {3, 5, 6},
#  {3, 5, 7},
#  {3, 6, 7},
#  {4, 5, 6},
#  {4, 5, 7},
#  {4, 6, 7},
#  {5, 6, 7},
#  {3, 4, 5, 6},
#  {3, 4, 5, 7},
#  {3, 4, 6, 7},
#  {3, 5, 6, 7},
#  {4, 5, 6, 7},
#  {3, 4, 5, 6, 7}]
# sage: list(y.subsets())
# [{},
#  {2},
#  {3},
#  {4},
#  {5},
#  {6},
#  {12},
#  {14},
#  {-1},
#  {2, 3},
#  {2, 4},
#  {2, 5},
#  {2, 6},
#  {2, 12},
#  {2, 14},
#  {2, -1},
#  {3, 4},
#  {3, 5},
#  {3, 6},
#  {3, 12},
#  {3, 14},
#  {3, -1},
#  {4, 5},
#  {4, 6},
#  {12, 4},
#  {4, 14},
#  {4, -1},
#  {5, 6},
#  {12, 5},
#  {5, 14},
#  {5, -1},
#  {12, 6},
#  {14, 6},
#  {-1, 6},
#  {12, 14},
#  {12, -1},
#  {-1, 14},
#  {2, 3, 4},
#  {2, 3, 5},
#  {2, 3, 6},
#  {2, 3, 12},
#  {2, 3, 14},
#  {2, 3, -1},
#  {2, 4, 5},
#  {2, 4, 6},
#  {12, 2, 4},
#  {2, 4, 14},
#  {2, 4, -1},
#  {2, 5, 6},
#  {2, 12, 5},
#  {2, 5, 14},
#  {2, 5, -1},
#  {2, 12, 6},
#  {2, 14, 6},
#  {2, -1, 6},
#  {2, 12, 14},
#  {2, 12, -1},
#  {2, -1, 14},
#  {3, 4, 5},
#  {3, 4, 6},
#  {12, 3, 4},
#  {3, 4, 14},
#  {3, 4, -1},
#  {3, 5, 6},
#  {3, 12, 5},
#  {3, 5, 14},
#  {3, 5, -1},
#  {3, 12, 6},
#  {3, 14, 6},
#  {3, -1, 6},
#  {3, 12, 14},
#  {3, 12, -1},
#  {3, -1, 14},
#  {4, 5, 6},
#  {12, 4, 5},
#  {4, 5, 14},
#  {4, 5, -1},
#  {12, 4, 6},
#  {4, 14, 6},
#  {4, -1, 6},
#  {12, 4, 14},
#  {12, 4, -1},
#  {4, -1, 14},
#  {12, 5, 6},
#  {14, 5, 6},
#  {-1, 5, 6},
#  {12, 5, 14},
#  {12, 5, -1},
#  {-1, 5, 14},
#  {12, 14, 6},
#  {12, -1, 6},
#  {-1, 14, 6},
#  {12, -1, 14},
#  {2, 3, 4, 5},
#  {2, 3, 4, 6},
#  {12, 2, 3, 4},
#  {2, 3, 4, 14},
#  {2, 3, 4, -1},
#  {2, 3, 5, 6},
#  {2, 3, 12, 5},
#  {2, 3, 5, 14},
#  {2, 3, 5, -1},
#  {2, 3, 12, 6},
#  {2, 3, 14, 6},
#  {2, 3, -1, 6},
#  {2, 3, 12, 14},
#  {2, 3, 12, -1},
#  {2, 3, -1, 14},
#  {2, 4, 5, 6},
#  {12, 2, 4, 5},
#  {2, 4, 5, 14},
#  {2, 4, 5, -1},
#  {12, 2, 4, 6},
#  {2, 4, 14, 6},
#  {2, 4, -1, 6},
#  {12, 2, 4, 14},
#  {12, 2, 4, -1},
#  {2, 4, -1, 14},
#  {2, 12, 5, 6},
#  {2, 14, 5, 6},
#  {-1, 2, 5, 6},
#  {2, 12, 5, 14},
#  {2, 12, 5, -1},
#  {-1, 2, 5, 14},
#  {2, 12, 14, 6},
#  {2, 12, -1, 6},
#  {-1, 2, 14, 6},
#  {2, 12, -1, 14},
#  {3, 4, 5, 6},
#  {12, 3, 4, 5},
#  {3, 4, 5, 14},
#  {3, 4, 5, -1},
#  {12, 3, 4, 6},
#  {3, 4, 14, 6},
#  {3, 4, -1, 6},
#  {12, 3, 4, 14},
#  {12, 3, 4, -1},
#  {3, 4, -1, 14},
#  {3, 12, 5, 6},
#  {14, 3, 5, 6},
#  {-1, 3, 5, 6},
#  {3, 12, 5, 14},
#  {3, 12, 5, -1},
#  {-1, 3, 5, 14},
#  {3, 12, 14, 6},
#  {3, 12, -1, 6},
#  {-1, 3, 14, 6},
#  {3, 12, -1, 14},
#  {12, 4, 5, 6},
#  {14, 4, 5, 6},
#  {-1, 4, 5, 6},
#  {12, 4, 5, 14},
#  {12, 4, 5, -1},
#  {-1, 4, 5, 14},
#  {12, 4, 14, 6},
#  {12, 4, -1, 6},
#  {-1, 4, 14, 6},
#  {12, 4, -1, 14},
#  {14, 12, 5, 6},
#  {-1, 12, 5, 6},
#  {-1, 14, 5, 6},
#  {-1, 12, 5, 14},
#  {-1, 12, 14, 6},
#  {2, 3, 4, 5, 6},
#  {12, 2, 3, 4, 5},
#  {2, 3, 4, 5, 14},
#  {2, 3, 4, 5, -1},
#  {12, 2, 3, 4, 6},
#  {2, 3, 4, 14, 6},
#  {2, 3, 4, -1, 6},
#  {12, 2, 3, 4, 14},
#  {12, 2, 3, 4, -1},
#  {2, 3, 4, -1, 14},
#  {2, 3, 12, 5, 6},
#  {14, 2, 3, 5, 6},
#  {-1, 2, 3, 5, 6},
#  {2, 3, 12, 5, 14},
#  {2, 3, 12, 5, -1},
#  {-1, 2, 3, 5, 14},
#  {2, 3, 12, 14, 6},
#  {2, 3, 12, -1, 6},
#  {-1, 2, 3, 14, 6},
#  {2, 3, 12, -1, 14},
#  {12, 2, 4, 5, 6},
#  {2, 14, 4, 5, 6},
#  {-1, 2, 4, 5, 6},
#  {12, 2, 4, 5, 14},
#  {12, 2, 4, 5, -1},
#  {-1, 2, 4, 5, 14},
#  {12, 2, 4, 14, 6},
#  {12, 2, 4, -1, 6},
#  {-1, 2, 4, 14, 6},
#  {12, 2, 4, -1, 14},
#  {2, 14, 12, 5, 6},
#  {-1, 2, 12, 5, 6},
#  {-1, 2, 14, 5, 6},
#  {-1, 2, 12, 5, 14},
#  {-1, 2, 12, 14, 6},
#  {12, 3, 4, 5, 6},
#  {14, 3, 4, 5, 6},
#  {-1, 3, 4, 5, 6},
#  {12, 3, 4, 5, 14},
#  {12, 3, 4, 5, -1},
#  {-1, 3, 4, 5, 14},
#  {12, 3, 4, 14, 6},
#  {12, 3, 4, -1, 6},
#  {-1, 3, 4, 14, 6},
#  {12, 3, 4, -1, 14},
#  {14, 3, 12, 5, 6},
#  {-1, 3, 12, 5, 6},
#  {-1, 14, 3, 5, 6},
#  {-1, 3, 12, 5, 14},
#  {-1, 3, 12, 14, 6},
#  {12, 14, 4, 5, 6},
#  {12, -1, 4, 5, 6},
#  {-1, 14, 4, 5, 6},
#  {12, -1, 4, 5, 14},
#  {12, -1, 4, 14, 6},
#  {-1, 14, 12, 5, 6},
#  {2, 3, 4, 5, 6, 12},
#  {2, 3, 4, 5, 6, 14},
#  {2, 3, 4, 5, 6, -1},
#  {2, 3, 4, 5, 12, 14},
#  {2, 3, 4, 5, 12, -1},
#  {2, 3, 4, 5, 14, -1},
#  {2, 3, 4, 6, 12, 14},
#  {2, 3, 4, 6, 12, -1},
#  {2, 3, 4, 6, 14, -1},
#  {2, 3, 4, 12, 14, -1},
#  {2, 3, 5, 6, 12, 14},
#  {2, 3, 5, 6, 12, -1},
#  {2, 3, 5, 6, 14, -1},
#  {2, 3, 5, 12, 14, -1},
#  {2, 3, 6, 12, 14, -1},
#  {2, 4, 5, 6, 12, 14},
#  {2, 4, 5, 6, 12, -1},
#  {2, 4, 5, 6, 14, -1},
#  {2, 4, 5, 12, 14, -1},
#  {2, 4, 6, 12, 14, -1},
#  {2, 5, 6, 12, 14, -1},
#  {3, 4, 5, 6, 12, 14},
#  {3, 4, 5, 6, 12, -1},
#  {3, 4, 5, 6, 14, -1},
#  {3, 4, 5, 12, 14, -1},
#  {3, 4, 6, 12, 14, -1},
#  {3, 5, 6, 12, 14, -1},
#  {4, 5, 6, 12, 14, -1},
#  {2, 3, 4, 5, 6, 12, 14},
#  {2, 3, 4, 5, 6, 12, -1},
#  {2, 3, 4, 5, 6, 14, -1},
#  {2, 3, 4, 5, 12, 14, -1},
#  {2, 3, 4, 6, 12, 14, -1},
#  {2, 3, 5, 6, 12, 14, -1},
#  {2, 4, 5, 6, 12, 14, -1},
#  {3, 4, 5, 6, 12, 14, -1},
#  {2, 3, 4, 5, 6, 12, 14, -1}]
# sage: list(z.subsets())
# [{}]
# sage:

a = [3,4,5,6,7]
b = [-1,2,3,4,5,6,12,14]
c = []
x = Set(a)
y = Set(b)
z = Set(c)