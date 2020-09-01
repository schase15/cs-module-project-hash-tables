# Imports 

import math
import random

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

# Create a cache to store the calculations we already did for easy lookup
    # Store the x and y as a tuple key
    # The solution as the value
cache = {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Check to see if the answer is in the cache
        # If it isn't calculate and store it 
    if (x,y) not in cache.keys():
        cache[(x,y)] = slowfun_too_slow(x,y)
    
    return cache[(x,y)]
    

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
