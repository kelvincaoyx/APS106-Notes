# A variation on Q1 from p. 219 of Gries book
# Write a function called find_multiples at takes a list and an integer, k, 
# as its input and returns a set of the list element that occur k or more times
# in the list.


def find_multiples(L, k):
    """ (list) -> set
    Return the a set containing the elements of L that occur k or more times.
    """ 

    dups_set = set()

    # for each entry in the list, if it appears k or more times
    # then add it to the dups_set
    for entry in L:
        if L.count(entry) >= k:
            dups_set.add(entry)

    return dups_set


# An alternative implementation using a dictionary
def find_multiples_dict(L, k):
    """ (list) -> set
    Return the a set containing the elements of L that occur k or more times.
    """ 

    dups_set = set()
    counts = {}
    
    # for each entry in the list, count its occurences and add to the
    # dups if it occurs k times
    for entry in L:
        if entry in counts:
            counts[entry] += 1
        else:
            counts[entry] = 1

        if counts[entry] == k:   # Bonus question: why is this == and not >=?
            dups_set.add(entry)

    return dups_set

print(find_multiples([1,2,3,3,4,19,0,1,3,0,0], 3))
print(find_multiples(['Smith', 'O\'Brien', 'Smith', 'Mansour', 'Bryant', 'Smith'], 2))

print(find_multiples_dict([1,2,3,3,4,19,0,1,3,0,0], 3))
print(find_multiples_dict(['Smith', 'O\'Brien', 'Smith', 'Mansour', 'Bryant', 'Smith'], 2))
