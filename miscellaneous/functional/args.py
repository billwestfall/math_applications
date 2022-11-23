import math

def combine_2_and_3(func):
  return func(2, 3)
              
print(combine_2_and_3(math.fmod))
print(combine_2_and_3(math.gcd))
print(combine_2_and_3(math.remainder))
print(combine_2_and_3(math.prod))
