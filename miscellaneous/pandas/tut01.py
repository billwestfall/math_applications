#!/usr/local/bin/python

import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

s = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'], index=['A', 'Z', 'C', 'Y', 'E'])
d = {'Chicago': 1000, 'New York': 1300, 'Portland': 900, 'San Francisco': 1100, 'Austin': 450, 'Boston': None}
cities = pd.Series(d)
print s
print cities

less_than_1000 = cities < 1000
print(less_than_1000)
print('\n')
print(cities[less_than_1000])

# changing values using boolean logic
print(cities[cities < 1000])
print('\n')
cities[cities < 1000] = 750
print cities[cities < 1000]

# changing based on the index
print('Old value:', cities['Chicago'])
cities['Chicago'] = 1400
print('New value:', cities['Chicago'])

print('Seattle' in cities)
print('San Francisco' in cities)

# divide city values by 3
div = cities / 3
print div

# square city values
sq = np.square(cities)
print sq

print(cities[['Chicago', 'New York', 'Portland']] + cities[['Austin', 'New York']])

data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
football = pd.DataFrame(data, columns=['year', 'team', 'wins', 'losses'])
print football

from_csv = pd.read_csv('data/mariano-rivera.csv')
print from_csv.head()
