import random

print("Enter first two digits of batter's batting average (no decimal):")

a = input()
d = int(a)

print("Enter the pitcher's ERA (no decimal):")

c = input()
b = int(c)

bat_avg = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
bat = random.choice(bat_avg)

if b in range(0,101):
    roll = random.randint(1, 20)

elif b in range(101,201):
    roll = random.randint(1, 12)

elif b in range(201,301):
    roll = random.randint(1, 8)

elif b in range(301,351):
    roll = random.randint(1, 4)

elif b in range(351,401):
    roll = random.randint(-4, -1)

elif b in range(401,501):
    roll = random.randint(-8, -1)

elif b in range(501,601):
    roll = random.randint(-12, -1)

elif b in range(601,701):
    roll = random.randint(-20, -1)

else:
    roll = -20

print("Pitcher dice roll is: ")
print(roll)

mss = roll + d
print("MSS value is: ")
print(mss)

e = mss + 1
f = mss + 5

if (mss <= d):
    print("It's a hit!")

elif (mss in range(e,f)):
    print("It's a walk")

else:
    print("Batter is out")
