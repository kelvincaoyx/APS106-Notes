'''
NoneType
'''

# str="hello"
# print(str[:2])

# print("3\")

# print(4/(3*(2-1)) == 4/3*(2-1))

# print(4/(3*(2-1)))
# print(4/3*(2-1))

x = "abcdef"
i = "i"
while i in x:
    print(i, end=" ")

# x = ['ab', 'cd']
# for i in x:
#     i.upper()
# print (x)

# names = ['Anagha', 'Tanishq', 'FruitPunch', 'Gloria']
# print (names [-1] [-1])

'''
[1,2]
NoneType
5
'''

# d = {1:[1,2], 0:[3,4]}
# print(d[1])
# print(d[0] .append(5))
# print (d[0] [-1])

'''
tinasuebrad
'''
# names = ['Tina', 'Sue', 'Brad']
# myfile = open("names.txt", "w")
# for item in names:
#     myfile .write(item.lower(0))
# myfile . close ()

'''
6




'''

def substitute(s):
    " (string) -> string"
    sub_s = s
    i = len(sub_s) // 2
    while i <= len(sub_s):
        sub_s[i] = "!"
        i = i + 2
    return sub_s.upper()

# print (substitute ('hello spring'))
'''
[1,2,3]
[1,2,3]
[val,val,val]
'''

def all_val(x, val):
    """(list, int)->(list)"""
    index_len = len(x)
    for i in range (index_len):
        x[i] = val
    return x

z = [1,2,3]
x = z[:]
y = all_val(x,2)

# print (z)
# print (x)
# print (y)

def fun2(lst) :
    '''(list)-> (list) '''
    if lst == []: 
        return []
    else: 
        l = lst[-1] 
        ll = lst[:-1] 
        return [l] + fun2(ll) 
lst = [1, 2, 3, 4]
# print (fun2 (lst))


def vectorize (M):
    '''(list of lists) —> list 
    Transforms a two dimensional matrix M into a vector. 
    oil '''
    returnLst= []
    for i in M:
        for j in i:
            returnLst.append(j)
    return returnLst

M = [[2, 1, 4, 5], [5, 2, 8, 1], [3, 6, 2, 0]] 
# print(vectorize(M) )

def reshape(V, m, n):
    '''(list, int, int) -> list of lists 
    Transforms a vector V into a two dimensional matrix with m 
    rows and n columns. If the vector cannot be reshaped to the 
    dimensions specified by m and n, then print the error message 
    'Error: vector cannot be reshaped to specified dimensions' and 
    return an empty list. 
    '''
    if len(V) != m*n:
        print("Error: vector cannot be reshaped to specified dimensions")
        return []
    returnlst = []
    tempList = []
    for i in V:
        tempList.append(i)
        if len(tempList) == n:
            returnlst.append(tempList)
            tempList = []
    return returnlst
        
# V = [2, 1, 4, 5, 5, 2, 8, 1, 3, 6, 2, 0] 
# print(reshape(V, 3, 6))


class Vehicle: 
    def __init__ (self, speed, maxSpeed, colour):
        self.speed = speed #in km/h 
        self.maxSpeed = maxSpeed #in km/h 
        self.colour = colour 
    def accelerate(self, x): 
        '''Increases the Vehicle object's speed by x. Note that 
        the Vehicle cannot have a speed higher than its maxSpeed 
        attribute.'''
        newSpeed = self.speed + x
        
        if newSpeed > self.maxSpeed:
            self.speed = self.maxSpeed
        else:
            self.speed = newSpeed

    def brake (self, x): 
        self.speed = self.speed - x 
        if(self.speed < 0):
            self.speed = 0 
            
    def race(self, other):
        '''Returns the Vehicle object self or other, whichever 
        has a higher speed. In the case of a tie, returns the 
        self object'''
        if self.speed > other.speed:
            return self
        elif self.speed < other.speed:
            return other
        else:
            return self
    
    def __str__ (self):
        '''Returns the Vehicle in the form: <colour> vehicle 
        travelling at <speed> km/h 
        >>> print(Vehicle(0,100,"red") 
        red vehicle travelling at 0 km/h 
        '''
        return self.colour + " vehicle travelling at " + str(self.speed) + " km/h"
    
    
    '''
    red car is now 70
    blue is 75
    
    this winnder of the race is blue vehicle travelling at 75 km/h
    '''
    
# redcar = Vehicle(60, 200, "red") 
# bluecar = Vehicle(80, 160, "blue") 
# redcar.accelerate (10) 
# bluecar. brake (5) 
# print("The winner of the race is",redcar.race(bluecar)) 

class Node: 
    def __init__(self, c = None, p = None): 
        '''Creates an object of type Node.''' 
        self.cargo = c 
        self.priority = p 
        self.next = None 
class LinkedList: 
    def __init__(self):
        '''Create a linked list, i.e., an object of type 
        LinkedList. This list is empty. 
        '''
        self.length = 0 # the number of elements in the list 
        self.head = None 
    def insert_in_front(self, cargo, priority):
        '''(LinkedList) -> NoneType 
        Insert an element at the front of the list. 
        '''
        if self.length == 0: 
            self.head = Node(cargo, priority) 
        else: 
            aux = self.head 
            self.head = Node(cargo, priority) 
            self.head.next = aux 
        self.length += 1 
        
    def insert_after_node (self, n, cargo, priority):
        '''(LinkedList) -> NoneType 
        Insert an element in the list, right after node n. 
        , , , '''
        aux = n.next 
        n.next = Node(cargo, priority) 
        n.next.next = aux 
        self.length += 1
        
    def is_empty(self):
        '''LinkedList) —> bool 
        Return True if the list is empty and False otherwise. 
        ''V '''
        if self.head == None:
            return True
        return False
    
    def extract_first (self):
        '''(LinkedList) —> string or NoneType 
        If the list has at least one element, remove the first 
        element from the list, return its cargo and assign the 
        next node in the sequence to be the new head of the list. 
        If the list has only one element, remove the element and 
        return its cargo. Return None if the list is empty. (No 
        element removal is performed in this case.) 
        '''
        
        if self.head == None:
            return None
        
        current = self.head
        self.head = self.head.next
        current.next = None
    
        return current.cargo
    
    def insert(self, cargo, priority): 
        '''I (LinkedList, string, int) -> NoneType 
        Insert a new element in the list at the position 
        corresponding to its given priority. 
        Update the length of the list. 
        III '''
        
        if priority > self.head.priority:
            self.insert_in_front(cargo,priority)
            self.length += 1
            return
        else:   
            current = self.head
            
            while current.next is not None and current.next.priority > priority:
                current = current.next
            
            self.insert_after_node(current,cargo,priority)
        
        self.length += 1
            
    def __str__(self):
        current = self.head
        
        while current != None:
            print(current.cargo, current.priority)
            current = current.next


one = Node("robin",7)
two = Node("erin",6)
three = Node("ashley",1)

one.next = two
two.next = three
lst = LinkedList()
lst.head = one
lst.length = 3

lst.__str__()

print("#############")
lst.extract_first()

lst.__str__()
print("#############")
lst.insert("alexis",3)

lst.__str__()







    