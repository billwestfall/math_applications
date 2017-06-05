from collections import Counter, defaultdict, OrderedDict

items = ['F', 'C', 'C', 'A', 'B', 'A', 'C', 'E', 'F']

cntr = Counter(items)
print(cntr)
#cntr('C') -=1
#print(cntr)

d = defaultdict(int)

for item in items:
    d[item] += 1

d

OrderedDict(sorted(d.items(), key=lambda i: i[1]))
