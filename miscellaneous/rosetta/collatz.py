# collatz number in Python

my_number = raw_input('Enter a positive integer: ')
while (doors != 1):
   if my_number % 2 == 0:
      my_number = my_number / 2
      print my_number
      else:
         my_number = (3 * my_number) + 1
         print my_number
