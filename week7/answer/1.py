# Write a function that takes an integer, n, as a parameter and returns a 
# sorted list of n random integers. 

import random

# If you found the random.sample function, this is the easiest way
def gen_sorted_list_sample(n):
    '''
    (int) -> list of int
    Return a sorted list of n random integers
    '''
    rand_list = random.sample(range(1000), n)
    rand_list.sort()
    return rand_list

# If you found the random.range function, this is the easiest way
def gen_sorted_list_range(n):
    '''
    (int) -> list of int
    Return a sorted list of n random integers
    '''
    rand_list = []
    for i in range(n):
        rand_list += [random.randrange(0,1000)]
    rand_list.sort()
    return rand_list

print(gen_sorted_list_sample(10))
print(gen_sorted_list_sample(20))

print(gen_sorted_list_range(10))
print(gen_sorted_list_range(20))
