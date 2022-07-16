'''
neutron++1
is the best part
'''
# particles = ["neutron", "proton", "electron"]
# charges = ["0", "+1", "-1"]
# print(particles[0] + "+" + charges[1])
# print("is the best particle"[:-4])

'''
we are\we are\we are
THE ENGINEERS!!!
'''

# final = '!'
# final *= 3
# lyric = "we are\\"
# print(lyric)
# chorus = "the engineers".upper()
# chorus.lower()

# for i in range(2):
#     print(i)
#     lyric += lyric

# print(lyric, chorus, sep = '\n', end = final)

'''


'''
# import csv
# with open('test.csv') as csvfile:
#     file_reader = csv.reader(csvfile)
#     for row in file_reader:
#         print(row[0] + 'exam on' + '-'.join(row[1:-1]) + 'at'  
#             + row[-1])

'''
1000
100
10
1
10
100
1000

'''
from calendar import c
from itertools import count
from platform import node
import re
from this import d


def fun1(n):
    if n < 10:
        print(n)    
    else:
        print(n)
        fun1(n//10)
        print(n)
        
# fun1(1000)

'''
{0:H, 2:l, 4:o}

0->H
N/A
2->1
N/a
4->o
N/A

'''
# message = "Hello!"
# positions = [0,1,2,3,4,5]
# my_dictionary = {}
# count = 0 
# for i in range(0, len(positions), 2):
#     my_dictionary[positions[i]] = message[count]
#     count += 2
 
# for element in positions:
#     print(element, end="-> ")
#     if element in my_dictionary:
#         print(my_dictionary[element])
#     else:
#         print("N/A")


def sum_ascii(s):
    ''' (str) -> int 
    Output: Returns the sum of the ASCII values of all the characters 
    in string s.
    '''
    counter = 0
    for i in s:
        counter += ord(i)
    
    return counter
        
# print(sum_ascii(""))

def pi_over_4(epsilon):
    """(float) -> (float, int)
    Input: A number determining the accuracy of the estimate of pi/4.
    Output: Returns a tuple containing an estimate of pi/4 and the 
    number of terms summed to generate the estimate.
    """
    returnCounter = 0
    for i in range(epsilon):
        returnCounter += ((-1)**i)/(2*i +1)
    return returnCounter, epsilon

# print(pi_over_4(2))

class ComplexNumber:
    def __init__(self, real = 0, imaginary = 0):
        ''' Creates a complex number with two data attributes: 
        a real part (real) and an imaginary part (imaginary).
        '''
        self.real = real
        self.imaginary = imaginary
        
    def __str__(self):
        '''(ComplexNumber) -> str
        Output: Returns a string representing the complex number.
        The format of the string is '(r + si)' where r is the
        real part and s is the imaginary part. 
        >>> c = ComplexNumber(3.1,4.2)
        >>> print(c)
        (3.1 + 4.2i)
        The parenthesis and i are part of the string.
        '''
        return "(" + str(self.real) + " + " + str(self.imaginary) + "i)"

    def add(self, other):
        '''(ComplexNumber, ComplexNumber) -> ComplexNumber
        Output: Returns a new ComplexNumber object resulting from
        adding the ComplexNumbers self and other. 
        '''
        new = ComplexNumber(self.real + other.real, self.imaginary + other.imaginary )
        return new
    
# print(ComplexNumber(5,4).add(ComplexNumber(8,3)))

class Node:
    def __init__(self):
        '''Initialize a Node'''
        self.cargo = None
        self.next = None
        
class Stack:
    def __init__(self,length=0,head=None):
        '''Initialize a Stack'''
        self.length = length # the number of elements in the Stack
        self.head = head
    
    def is_empty(self):
        '''(Stack) -> bool
        Output: Return True if the Stack is empty and False otherwise.
        '''
        if self.head == None:
            return True
        
        return False
    
    def peek(self):
        '''(Stack) -> the type of the cargo or NoneType
        Output: Return the cargo of the element at the front of the
        Stack or None if the Stack is empty.
        '''
        if self.is_empty():
            return None
        
        return self.head.cargo
    


    def pop(self):
        '''(Stack) -> the type of the cargo or NoneType
        Output: Remove the first element of the Stack and return the
        cargo. Return None if the Stack is empty. Update self.length
        
        one = Node()
        two = Node()
        three = Node()
        
        
        one = Node() -> None
        
        
        two = Node()
        three = Node()
        '''
        
        if self.is_empty():
            return None
        
        current = self.head
        self.head = current.next
        
        current.next = None
        
        self.length -= 1
        
        return current.cargo
    
    def __str__(self):
        current = self.head
        
        while current is not None:
            print(current.cargo)
            current = current.next
    
    def push(self, cargo):
        '''(Stack, type of cargo) -> NoneType
        Output: Insert a new item at the front of the Stack. Return
        None. Update self.length
        '''
        new = Node()
        new.cargo = cargo
        new.next = self.head
        
        self.head = new
        self.length += 1

    
one = Node()
two = Node()
three = Node()

one.cargo = 1
two.cargo = 2
three.cargo = 3

one.next = two
two.next = three

s = Stack()

s.length = 3
s.head = one

print(s.peek())

# s.__str__()

# print(s.pop())

# print("###########")
# s.push(69)

# s.__str__()
# print(s.length)

import csv
def load_inventory(filename):
    '''(str) -> dictionary {str : [[int, str], [int, str], ...]]}
    Input: a string specifying the CSV filename
    Output: a dictionary representing the inventory, amounts, and
    locations. 
    ''' 
    with open(filename) as csvFile:
        
        dictt = dict()
        
        listVersion = []
        for row in csv.reader(csvFile):
            listVersion.append(row)
        
        for row in listVersion:
            key = row[0]
            if key not in dictt:
                dictt.update({key:[]})
            dictt[key].append([row[1],row[2]])
        
        return dictt

# print(load_inventory("inv.csv"))

def is_correct(prediction, label):
    '''(list, list) -> bool
    Input: two lists, prediction and label, of floating point numbers
    representing probability values corresponding to digits 0 – 9
    Output: True only if most probable digit in prediction matches
    label. False, otherwise.
    '''
    highIndex = 0
    highNum = prediction[highIndex]
    for i in range(len(prediction)):
        if prediction[i] > highNum:
            highIndex = i
            highNum = prediction[i]
    
    highIn = 0
    for i in range(len(label)):
        if label[i] == 1:
            highIn = i
    
    if highIn == highIndex:
        return True
    
    return False

predictions = [[0.06, 0.01, 0.02, 0.01, 0.5, 0.05, 0.01, 0.01, 0.08, 0.3],
 [0.01, 0.02, 0.06, 0.7, 0.1, 0.07, 0.06, 0.01, 0.01, 0.01],
 [0.35, 0.07, 0.01, 0.01, 0.05, 0.01, 0.45, 0.02, 0.06, 0.02]]
labels = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def percent_correct(predictions, labels):
    '''(list of lists, list of lists) -> float
    Input: two nested lists of floating point numbers
    Output: a float representing a percentage score of accurately 
    classified digit samples over the total number of samples.
    Pre-conditions: all sub-lists have the same size and contain
    only floating point numbers.
    '''
    trueCounter = 0
    total = 0
    for i in range(len(predictions)):
        if is_correct(predictions[i],labels[i]):
            trueCounter += 1
        total += 1
        
    return trueCounter/total *100

#print(percent_correct(predictions, labels))
