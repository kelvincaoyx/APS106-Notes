# Q1 from p. 219 of Gries book
# Write a function called find_dups that takes a list of integers as its input
# argument and returns a set of those integers that occur two or more times
#in the list.


def find_dups(L):
    """ (list) -> set

    Return a set containing the duplicated elements in L.

    >>> find_dups([1, 1, 2, 3, 4, 2])
    {1, 2}
    >>> find_dups([1, 2, 3, 4])
    set()
    """ 

    elem_set = set()
    dups_set = set()

    # for each entry in the list, if it doesn't make the set of elements bigger
    # then it is a duplicate
    for entry in L:
        len_initial = len(elem_set)
        elem_set.add(entry)
        len_after = len(elem_set)
        if len_initial == len_after:
            dups_set.add(entry)

    return dups_set

print(find_dups([1,2,3,3,4,19,0,1]))
print(find_dups(['Smith', 'O\'Brien', 'Smith', 'Mansour', 'Bryant', 'Smith']))
