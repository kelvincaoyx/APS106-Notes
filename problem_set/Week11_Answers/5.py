import random

class DoublyLinkedList:
    ''' A class implementing an doubly linked list'''

    def __init__(self):
        '''
        (self) -> NoneType
        Create an empty list
        '''
        self.length = 0
        self.head = None # points to first element
        self.tail = None # points to last element

    def __str__(self):
        '''
        (self) -> NoneType
        Iteratively traverse the list printing each element
        '''
        s = "["
        curr = self.head
        while curr is not None:
            s += str(curr) + " "
            curr = curr.next
        if len(s) > 1:
            s = s[:-1] # remove the last space
        s += "]"
        return s

    def print_backward_nicely(self):
        '''
        (self) -> NoneType
        Recursively traverse the list printing it out in reverse order
        '''
        print("[", end="")
        if self.tail is not None:
            self.tail.print_backward()
        print("]", end="")
    
    def add_first(self, cargo):
        '''
        (self, Object) -> NoneType
        Create a new Node containing cargo and insert it at the head of 
        the list
        '''
        node = Node(cargo)
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        else: 
            # this is the first element
            self.tail = node
            
        self.head = node
        self.length += 1
        
    def add_last(self, cargo):
        '''
        (self, Object) -> NoneType
        Create a new Node containing cargo and insert it at the end of 
        the list
        '''
        node = Node(cargo)
        node.prev = self.tail
        if self.tail is not None:
            self.tail.next = node
        else: 
            # this is the first element
            self.head = node
        
        self.tail = node
        self.length += 1

    def remove_item(self, item):
        '''
        (self, Object) -> NoneType
        Find the Node containing item and remove it from the list 
        '''
        current = self.head
        while current is not None and current.cargo != item:
            current = current.next
        
        if current is not None: # if item was found
            is_first_item = current is self.head
            is_last_item = current is self.tail
            
            if is_first_item: 
                self.head = current.next
                if self.head is not None:
                    self.head.prev = None
                
            if is_last_item: 
                self.tail = current.prev
                if self.tail is not None:
                    self.tail.next = None
                
            if not is_first_item and not is_last_item:
                current.prev.next = current.next
                current.next.prev = current.prev

            current.next = None
            current.prev = None
            
            self.length -= 1
        
        
class Node:
    ''' A class representing an element in a doubly linked list '''
    
    def __init__(self, cargo=None, prev = None, next=None):
        '''
        (self, Object, Node, Node) -> NoneType
        Create Node with cargo and next and prev references
        '''
        self.cargo = cargo
        self.prev = prev
        self.next = next

    def __str__(self):
        '''
        (self) -> str
        Return the string of the cargo
        '''
        return str(self.cargo)

    def print_backward(self):
        '''
        (self) -> NoneType
        Recursively print the list backward
        '''
        print(self.cargo, end=" ")
        if self.prev is not None:
            self.prev.print_backward()

my_list = DoublyLinkedList()

my_list.add_first(3)
print(my_list)

my_list.remove_item(3)
print(my_list)

cargo_list = []

test_size = 10
for i in range(test_size):
    num = random.randint(0, 100)
    if num % 2 == 0:
        my_list.add_first(num)
    else:
        my_list.add_last(num)
        
    cargo_list.append(num)

print(my_list)

for i in cargo_list:
    print("Removing: ", i, end = " ")
    my_list.remove_item(i)
    print(my_list)
    

