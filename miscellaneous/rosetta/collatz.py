# collatz number in Python

my_no = input('Enter a positive integer: ')
my_number = int(my_no)
while (my_number != 1):
   if my_number % 2 == 0:
      my_number = my_number / 2
      my_val = int(my_number)
      print(my_val)
   else:
      my_number = (3 * my_number) + 1
      my_val = int(my_number)
      print(my_val)
