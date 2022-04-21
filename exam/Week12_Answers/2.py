import random

class DoublyLinkedOrderedList:
    ''' A class implementing an ordered doubly linked list'''
    
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
    
    def add(self, cargo):
        '''
        (self, Object) -> NoneType
        Create a new Node containing cargo and insert it into the right
        place in the ordered list
        '''
        node = Node(cargo)
        current = self.head
        while current is not None and current.cargo < cargo:
            current = current.next
            
        node.next = current
        
        is_at_front = current == self.head
        is_at_end = current is None
        
        if is_at_front: # insert at the front
            if self.head is not None:
                self.head.prev = node
            self.head = node
            
        if is_at_end: # insert at the end
            if self.tail is not None:
                self.tail.next = node 
            node.prev = self.tail
            self.tail = node
            
        if not is_at_front and not is_at_end: # insert in the middle
            node.prev = current.prev
            node.prev.next = node
            node.next.prev = node
        
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


my_list = DoublyLinkedOrderedList()
#for i in [5, 1, 8, 3, 7]:
    #print("Adding", i)
    #my_list.add(i)
    #print(my_list)

cargo_list = []

test_size = 20
for i in range(test_size):
    num = random.randint(0, 100)
    print("Adding", num)
    my_list.add(num)
    print(my_list)
    cargo_list.append(num)

for i in cargo_list:
    print("Removing: ", i, end = " ")
    my_list.remove_item(i)
    print(my_list)
    
