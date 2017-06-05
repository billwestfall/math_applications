f = open("data.txt")
for line in f:
  print(line)
  
lines = f.readlines("data.txt")
data = f.read("data.txt")

print(data)
print(lines)
