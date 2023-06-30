import random

print("Enter first two digits of batter's batting average (no decimal):")

a = input()
d = int(a)

print("Enter the pitcher's ERA (no decimal):")

c = input()
b = int(c)

bat_avg = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
bat = random.choice(bat_avg)

if b in range(0,100):
    roll = random.randint(1, 20)

elif b in range(101,200):
    roll = random.randint(1, 12)

elif b in range(201,300):
    roll = random.randint(1, 8)

elif b in range(301,350):
    roll = random.randint(1, 4)

elif b in range(351,400):
    roll = random.randint(-4, -1)

elif b in range(401,500):
    roll = random.randint(-1, -8)

elif b in range(501,600):
    roll = random.randint(-1, -12)

elif b in range(601,700):
    roll = random.randint(-1, -20)

else:
    roll = -20

print("Pitcher dice roll is: ")
print(roll)

mss = roll + d
print("MSS value is: ")
print(mss)
