import random

# Again a couple of solutions. I prefer sum_with_sum

def sum_with_sum(matrix):
    ''' (2D-list) -> int
    Returns the sum of the elements in the border of the size X size matrix. 
    First and last rows and columns.
    '''
    size = len(matrix)
    s = sum(matrix[0]) # first row
    
    for x in range(1,size - 1):
        # first and last elements of middle rows
        s += matrix[x][0] + matrix[x][size - 1] 
        
    s += sum(matrix[size - 1]) # last row

    return s

def sum_with_loops(matrix):
    ''' (2D-list) -> int
    Returns the sum of the elements in the border of the size X size matrix. 
    First and last rows and columns.
    '''
    size = len(matrix)
    s = 0
    for row in range(size):
        if row == 0 or row == size - 1:
            # sum whole row for first and last rows
            for value in matrix[row]:
                s += value
        else:
            # sum first and last entries for middle rows
            s += matrix[row][0]
            s += matrix[row][size - 1]
            
    return s

size = int(input("Please input the matrix size (e.g., 5): "))
max_value = int(input("Please input the maximum value: "))

# create the matrix
matrix = []
for x in range(size):
    row = []
    for y in range(size):
        row.append(random.randint(0, max_value))
    matrix.append(row)

print(matrix) # Bonus question: print out each row of matrix on a different line

# sum the borders
print(sum_with_sum(matrix))
print(sum_with_loops(matrix))

