import random
from tabnanny import check

def matrixCreate(size, maxvalue):
    returnMatrix = []
    tempInnerMatrix = []
    for i in range(size):
        tempInnerMatrix = []
        for j in range(size):
            tempInnerMatrix.append(random.randint(0,maxvalue))
            #print("inner",tempInnerMatrix)
        returnMatrix.append(tempInnerMatrix)


    for lists in returnMatrix:
        for i in range(len(lists)):
            lists[i] = str(lists[i])
        print(" ".join(lists))
    
    for lists in returnMatrix:
        for i in range(len(lists)):
            lists[i] = int(lists[i])
         
    #print(returnMatrix)
    returnSum = sum(returnMatrix[0]) + sum(returnMatrix[-1])
    #print("returnsum",returnSum)
    #print(range(1,len(returnMatrix)-2))
    for i in range(1,len(returnMatrix)-1):
        #print(returnMatrix[i][0] + returnMatrix[i][-1])
        returnSum += returnMatrix[i][0] + returnMatrix[i][-1]
    print(returnSum)

#matrixCreate(3,10)
    
def uniqueMatrix(n):
    numSet = []
    for i in range(n**2):
        numSet.append(i+1)
    #print(numSet)

    returnMatrix = []
    for row in range(n):
        tempMatrix = []
        for column in range(n):
            randomNumInSet = numSet[random.randrange(0,len(numSet))]
            tempMatrix.append(randomNumInSet)
            numSet.remove(randomNumInSet)
        returnMatrix.append(tempMatrix)
    print(returnMatrix)
    
    for list in returnMatrix:
        for i in range(len(list)):
            list[i] = str(list[i])
        print(" ".join(list))
    
#uniqueMatrix(10)

sortedLIst = []

for i in range(100):
    sortedLIst.append(i)

#print(sortedLIst)  

def binary_search(array,value):
    lowerValue = 0
    higherValue = len(array)-1
    print(higherValue)
    
    checkerValue = (higherValue + lowerValue)//2
    #print(checkerValue)
    while array[checkerValue] != value:
        checkerValue = (higherValue + lowerValue)//2+1
        print("checker1", checkerValue)
        if array[checkerValue] < value:
            lowerValue = checkerValue
            
        if array[checkerValue] > value:
            higherValue = checkerValue
    print(checkerValue)

#binary_search(sortedLIst,99)


# Q1 from p. 219 of Gries book
# Write a function called find_dups that takes a list of integers as its input
# argument and returns a set of those integers that occur two or more times
#in the list.

def find_dupes(list):
    elementSet=set()
    dupSet=set()
    
    for entry in list:
        elementSetInitialLeng = len(elementSet)
        elementSet.add(entry)
        elementSetAfterLeng = len(elementSet)
        if elementSetInitialLeng == elementSetAfterLeng:
            dupSet.add(entry)
    
    return(dupSet)


# A variation on Q1 from p. 219 of Gries book
# Write a function called find_multiples at takes a list and an integer, k, 
# as its input and returns a set of the list element that occur k or more times
# in the list.

def find_multiples(list,k):
    returnSet = set()
    
    for entry in list:
        if list.count(entry) >= k:
            returnSet.add(entry)
            
    return(returnSet)


#print(find_multiples([1,2,3,3,4,19,0,1,3,0,0], 3))
#print(find_multiples(['Smith', 'O\'Brien', 'Smith', 'Mansour', 'Bryant', 'Smith'], 2))

# Q2 from p. 219 of Gries book
# Using the set.pop() method write a function called mating_pairs 
# that takes two equal-sized sets called males and females as input and 
# returns a set of pairs; each pair must be a tuple containing one male and 
# one female. (The elements of males and females may be strings containing 
# gerbil names or gerbil ID numbers — your function must work with both.)

def mating_pairs(male, female):
    returnSet = set()
    for index in range(len(male)):
        print(index)
        males = male.pop()
        females = female.pop()
        returnSet.add((males,females))
    
    return returnSet

#print(mating_pairs({'Anne', 'Beatrice', 'Cari'}, {'Ali', 'Bob', 'Chen'}))

'''
 A sparse vector is a vector whose entries are almost all zero, like [1, 0, 0, 0,
0, 0, 3, 0, 0, 0]. Storing all those zeros in a list wastes memory, so programmers often use 
dictionaries instead to keep track of just the nonzero
entries. For example, the vector shown earlier would be represented as
{0:1, 6:3}, because the vector it is meant to represent has the value 1 at
index 0 and the value 3 at index 6.
'''

def sparseVector(vector):
    sparse = dict()
    for i in range(len(vector)):
        if vector[i] != 0:
            sparse.update({i:vector[i]})
    return sparse
    
#sparseVector([1, 0, 0, 0, 0, 0, 3, 0, 0, 0])

'''
The sum of two vectors is just the element-wise sum of their elements.
For example, the sum of [1, 2, 3] and [4, 5, 6] is [5, 7, 9]. Write a function
called sparse_add that takes two sparse vectors stored as dictionaries
and returns a new dictionary representing their sum.
'''

def sparse_add(firstVector, secondVector):
    vector1 = sparseVector(firstVector)
    vector2 = sparseVector(secondVector)
    returnSet = dict()
    setOfKeys = vector1.keys()
    
    for key in setOfKeys:
        value = vector1.get(key) + vector2.get(key)
        returnSet.update({key:value})
    
    print(returnSet)
     
#sparse_add([1,2,3],[4,5,6])

'''
The dot product of two vectors is the sum of the products of corresponding elements.
For example, the dot product of [1, 2, 3] and [4, 5, 6]
is 4+10+18, or 32. Write another function called sparse_dot that calculates
the dot product of two sparse vectors
'''

def sparse_dotProdoct(firstVector, secondVector):
    vector1 = sparseVector(firstVector)
    vector2 = sparseVector(secondVector)
    returnSet = dict()
    setOfKeys = vector1.keys()
    
    for key in setOfKeys:
        value = vector1.get(key) * vector2.get(key)
        returnSet.update({key:value})
    
    dotProduct = 0
    for key in setOfKeys:
        dotProduct += returnSet.get(key)
    print(dotProduct)


#sparse_dotProdoct([1,2,3],[4,5,6])

'''
Your boss has asked you to write a function called sparse_len that will
return the length of a sparse vector (just as Python's len returns the
length of a list). What do you need to ask her before you can start
writing it?

'''

def sparse_len(firstVector):
    vector1 = sparseVector(firstVector)
    returnSet = dict()
    setOfKeys = vector1.keys()
    
    counter = 0
    for key in setOfKeys:
        counter += 1
    

    print(counter)

#sparse_len([1, 0, 0, 0, 0, 0, 3, 6, 0, 0])

# Write a program that asks a user to enter a string and output letter 
# that appears the most times and the number of times it appears. 
# You need to deal with both capital and lower-case letters.


