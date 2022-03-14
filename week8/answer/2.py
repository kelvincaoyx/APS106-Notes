import random
import timeit

# a helper function
def create_zero_matrix(size):
    ''' (int) -> 2Dlist
    Returns an size X size matrix initialized to 0
    '''
    # There is a more elegant way to do this with list comprehension but
    # that is a bit beyond this course
    matrix = []
    for x in range(size):
        row = []
        for y in range(size):
            row.append(0)
        matrix.append(row)
        
    return matrix

# A checking function that will help in debugging
def check_unique(matrix):
    ''' (2Dlist) -> bool
    Returns True if the size X size matrix contains only unique numbers
    from 1 to size**2
    '''
    size = len(matrix)
    count = []
    for i in range(size**2):
        count.append(0)
    
    for x in range(size):
        for y in range(size):
            index = matrix[x][y] - 1
            if count[index] == 0:
                count[index] += 1
            else:
                return False

    return True    

# Randomly generate each number and check if it has already been generated before
# If so, generate it again
def create_unique_matrix_gen(size):
    ''' (int) -> 2Dlist
    Returns a size X size matrix containing the numbers 1 to size**2 in random
    order.
    '''

    # start by filling a list with unique numbers in random order
    numbers = []
    while len(numbers) < size**2:
        rnd_num = random.randint(1,size**2)
        while rnd_num in numbers:
            rnd_num = random.randint(1,size**2)
        numbers.append(rnd_num)
    
    matrix = []    
    start = 0
    end = size
    index = 0  
    while end <= size**2:
        matrix.append(numbers[start:end])
        start = end
        end += size
            
    return matrix

# Create a matrix of zeros. For each number randomly generate a cell and put
# it there if the cell is empty. If not, generate a new cell
def create_unique_matrix_index(size):
    ''' (int) -> 2Dlist
    Returns a size X size matrix containing the numbers 1 to size**2 in random
    order.
    '''
    matrix = create_zero_matrix(size)
    num = 1
    while num <= size**2:
        # generate a random cell in the matrix
        i = random.randint(0, size - 1)
        j = random.randint(0, size - 1)
        
        # if the cell is empty, replace it with the number we want
        if matrix[i][j] == 0:
            matrix[i][j] = num
            num += 1
    
    return matrix

# Generate a ordered list and for each element swap it with a randomly chosen
# element
def create_unique_matrix_swap(size):
    ''' (int) -> 2Dlist
    Returns a size X size matrix containing the numbers 1 to size**2 in random
    order.
    '''
    one_d = list(range(size**2)) # create a list of 0 to size**2 - 1
    for x in range(len(one_d)):
        # pick random index and swap
        rnd_index = random.randint(0,len(one_d) - 1)
        (one_d[x], one_d[rnd_index]) = (one_d[rnd_index], one_d[x])
    #print(one_d)
    
    # create matrix from one_d list
    index = 0   
    matrix = []
    for x in range(size):
        row = []
        for y in range(size):
            row.append(one_d[index] + 1) # add one since one_d has numbers from 0
            index += 1
        matrix.append(row)
                    
    return matrix


size = int(input("Matrix size (e.g., 5): "))

n = int(input("How many times do you want to test the code (e.g., 10000): "))

# Test the slow version
print("Testing create_unique_matrix_gen")

start_time = timeit.default_timer()

for i in range(n):
    matrix = create_unique_matrix_gen(size)
    if not check_unique(matrix):
        print("Error!!")
        print(matrix)
        
print("Cumulative time: ", timeit.default_timer() - start_time)

# Test the slower version
print("\nTesting create_unique_matrix_index")

start_time = timeit.default_timer()

for i in range(n):
    matrix = create_unique_matrix_index(size)
    if not check_unique(matrix):
        print("Error!!")
        print(matrix)
        
print("Cumulative time: ", timeit.default_timer() - start_time)

# Test the faster version
print("\nTesting create_unique_matrix_swap")

start_time = timeit.default_timer()

for i in range(n):
    matrix = create_unique_matrix_swap(size)
    if not check_unique(matrix):
        print("Error!!")
        print(matrix)
        
print("Cumulative time: ", timeit.default_timer() - start_time)
