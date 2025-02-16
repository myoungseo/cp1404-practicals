'''
import random

print(random.randint(5, 20))
# line 1
# Returns a random integer between 5 and 20 inclusive.
# The smallest number is 5, and the largest number is 20.

print(random.randrange(3, 10, 2))
# line 2
# Returns one of [3, 5, 7, 9] randomly.
# The smallest number is 3, and the largest number is 9.
# In range(3, 10, 2), 4 is not included, so it cannot be selected.

print(random.uniform(2.5, 5.5))
# line 3
# Returns a random float between 2.5 and 5.5 inclusive.
# The smallest number is 2.5, and the largest number is 5.5.

print(random.randint(1, 100))
'''
import random

print(random.randint(5, 20))
# line 1
# Returns a random integer between 5 and 20 inclusive.
# The smallest number is 5, and the largest number is 20.
print(random.randrange(3, 10, 2))
# line 2
# Returns one of [3, 5, 7, 9] randomly.
# The smallest number is 3, and the largest number is 9.
# In range(3, 10, 2), 4 is not included, so it cannot be selected.
print(random.uniform(2.5, 5.5))
# line 3
# Returns a random float between 2.5 and 5.5 inclusive.
# The smallest number is 2.5, and the largest number is 5.5.

print(random.randint(1, 100))