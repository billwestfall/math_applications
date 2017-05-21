# Babbage problem in Python

i = 1
babbage = i * i
while (i > 0):
   string = str(babbage)
   substring = "269696"
   if substring in string:
#   if str(babbage).find("269696") == 1:
      print ("The Babbage number is "), print(i), print(" and the root is "), print(babbage)
      break
   else:
      i = i + 1
