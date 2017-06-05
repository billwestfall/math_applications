f = open("data.txt")
for line in f:
  print(line)
  
lines = f.readlines()
data = f.read()

print(data)
print(lines)
