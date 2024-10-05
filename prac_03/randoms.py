import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
line 1: 13, smallest number is 5, largest number is 20
line 2: 7, smallest number is 3, largest number is 9
line 3: 3.0824153545585355, smallest number is 2.5, largest number is 5.5
"""

print(random.randint(1, 101))