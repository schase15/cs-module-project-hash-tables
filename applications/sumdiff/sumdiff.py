"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

'''
Plan:
    Create look up table or cache of all f(x) up to 200

    Make a addition dictionary that holds all of the possible additions
    and a subtraction dictionary that holds all the possible subtractions

    Use the answers as the keys, store a list of combinations that make that solution value

    See if the key from the subtraction table is in the addition table

    Return the values of each in a addition array and a subtraction array

    Every combination of these two array are the possible combinations that equal each other
'''

# Create a lookup table for f(x) calculations
lookup = {}

for i in range(1, 200):
    lookup[i] = f(i)

# Create an addition dictionary
add = {}

for a in q:
    for b in q:
        # If the solution is not is add dict, insert empty list
        if (lookup[a] + lookup[b]) not in add:
            add[lookup[a] + lookup[b]] = []

        # Store the values used to create the addition answer key
        add[lookup[a] + lookup[b]].append((a, b))

# Do the same thing for subtract dictionary
subtract = {}

for c in q:
    for d in q:
        # If the solution is not is subtract dict, insert empty list
        if (lookup[c] - lookup[d]) not in subtract:
            subtract[lookup[c] - lookup[d]] = []

        # Store the values used to create the solution answer key
        subtract[lookup[c] - lookup[d]].append((c, d))


# See if the keys of the subtract dictionary are in the add dictionary
# If they are, add the values of the add side to a add list
    # and values of the subtract side to a subtract list

subtract_list = []

add_list = []

for key in subtract.keys():
    if key in add:
        subtract_list.append(subtract[key])
        add_list.append(add[key])

print(f"SUBTRACT MATCHES: {subtract_list}\n")
print(f"ADD MATCHES: {add_list}\n")

# Each item in subtract_list[0] sublist gets matched to each item in add_list[0]
# And so on for each inner list of each
# Print out in the correct way


