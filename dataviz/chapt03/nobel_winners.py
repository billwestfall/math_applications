nobel_winners = [
  {'category': 'Physics',
   'name': 'Albert Einstein',
   'nationality': 'Swiss',
   'sex': 'male',
   'year': 1921
 },
 {'category': 'Physics',
  'name': 'Paul Dirac',
  'nationality': 'British',
  'sex': 'male',
  'year': 1933
},
{'category': 'Chemistry',
 'name': 'Marie Curie',
 'nationality': 'Polish',
 'sex': 'female',
 'year': 1911
}
]

f = open('nobel_winners.csv', 'w')

cols = sorted(nobel_winners, key=lambda x:sorted(x.keys()))
cols.sort()

with open('nobel_winners.csv', 'w') as f:
    f.write(','.join(cols) + '\n')

    for o in nobel_winners:
        row = [str(o[col]) for col in cols]
        f.write(','.join(row) + '\n')

with open('nobel_winners.csv', 'w') as f:
    for line in f.readlines():
        print(line),
