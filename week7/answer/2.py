# Write a function that takes a sorted list of integers (see Q1) and returns 
# the median. If the list has odd length, the median is the middle number. 
# If the list is even length, the median is the mean of the two middle numbers.

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

def get_median(num_list):
    '''
    (list of num) -> num
    Returns the median entry in the sorted list num_list
    '''
    mid_pt = len(num_list)//2
    #print(mid_pt)
    if len(num_list) % 2 == 0:   
        return (num_list[mid_pt-1] + num_list[mid_pt]) /2
    
    return num_list[mid_pt] # why do I not need an else here?

list1 = gen_sorted_list_sample(10)
list2 = gen_sorted_list_sample(11)

print(list1,get_median(list1),sep="\n")
print(list2,get_median(list2),sep="\n")


