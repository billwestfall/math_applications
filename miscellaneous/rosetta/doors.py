# my take on the 100 doors challege in Python

import random

doors = 100
prize = (random.randint(1,100))
while (doors > 0):
   if doors == prize:
      print ("The prize is begind door "), print(prize)
   else:
      doors = doors - 1
