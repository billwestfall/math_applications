# collatz number in Python

doors = 100
prize = (random.randint(1,100))
while (doors > 0):
   if doors == prize:
      print ("The prize is begind door "), print(prize)
      break
   else:
doors = doors - 1