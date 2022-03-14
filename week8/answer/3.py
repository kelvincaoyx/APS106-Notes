# binary search

import random

def binary_search(numbers, num):
    ''' (list of int, int) -> int
    Returns the index of num in numbers or -1 if num is not in the list
    numbers is a sorted list
    '''
    min_index = 0
    max_index = len(numbers) - 1
    while(min_index <= max_index):
        #print(min_index, max_index)
        
        middle = (min_index + max_index)//2
        
        if numbers[middle] > num:
            max_index = middle - 1
        elif numbers[middle] < num:
            min_index = middle + 1
        else:
            return middle

    return -1
    
size = int(input("How large a list: "))

# create a sorted list of random numbers
numbers = []
for i in range(size):
    numbers.append(random.randint(0, 10000))

numbers.sort()
print(numbers)

# choose a random index and search for the corresponding value
rand_index = random.randint(0,size-1)
index = binary_search(numbers,numbers[rand_index]) 

if rand_index == index:
    print("Found it! rand_index:", rand_index, "\t index:", index)
else:
    print("*** Problem! rand_index:", rand_index, "\t index:", index)

# Test for case when the value isn't there
num = numbers[rand_index]
print("Removing", num)
numbers.remove(num)

index = binary_search(numbers,num) 
if index == -1:
    print(num,"is no longer in the list")
else:
    print("*** Problem!", num, "is still there. index: ", index)

