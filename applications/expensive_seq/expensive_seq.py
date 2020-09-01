# Compute expensive sequence
# Use a cache to reduce redundant calculations

cache = {}

def expensive_seq(x, y, z):
    '''
    Given the formula, similar to fibonacci
    Use recursion
    '''
    # Base case
    if x <= 0:
        return y + z

    # If x is greater than 0
    if x >  0: 
        # Check to see if the calculation has already been done
        if (x,y,z) not in cache:
            # Add the tuple into the cache
            cache[x, y, z] = expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)
        
        # If we get here, the tuple was either already in the cache, or we just added it 
        return cache[(x,y,z)]


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
