class Node:
    '''A class that can be used to form an element of a linked list'''
    
    def __init__(self,cargo=None,next=None):
        '''
        (self) -> None
        Create a node with cargeo and next
        '''
        self.cargo = cargo
        self.next = next
    
    def __str__(self):
        '''
        (self) -> str
        Return string representation of a Node
        '''
        return str(self.cargo)
    
class SortedLinkedList:
    '''A linked list implementation that maintains the elements in non-descending order'''
    
    def __init__(self):
        '''
        (self) -> None
        Create an empty list
        '''
        self.head = None  # no elements
        self.length = 0
        
    def __str__(self):
        '''
        (self) -> str
        Return the string representation of the tree
        '''
        if self.head == None:
            return "[]"
        
        ret_str = "["
        node = self.head
        while node.next != None: # get the string for all but the last node
            ret_str += str(node) + ","
            node = node.next
        ret_str += str(node) + "]"
        
        return ret_str
                    
    def len(self):
        '''
        (SortedLinkedList) -> int
        Return the length of the list
        '''
        return self.length
    
    def add(self, new_node):
        '''
        (SortedLinkedList, Node) -> NoneType
        Add new_node to the list maintaining the sorted order
        '''
        # if the list is empty or if the first element is greater than new_node,
        # make new_node the first element
        if self.head == None or self.head.cargo >= new_node.cargo: 
            new_node.next = self.head # make new_node point to the old first element
            self.head = new_node      # make new_node the first element
        else:
            # start with before pointing to the first element and 
            # after pointing to the second
            before = self.head
            after = self.head.next
            # while we have not found an element greater than new_node,
            # go to the next element
            while after != None and after.cargo < new_node.cargo:
                before = after
                after = after.next
            
            # make before point to new node and new_node point to after
            before.next = new_node
            new_node.next = after
            
        self.length += 1
 
    def remove(self, num):
        '''
        (SortedLinkedList, num) -> Node
        Remove a node containing num from the list and return a reference to it
        or None if it doesn't exist
        '''
        if self.head == None:
            return None
        
        # remove first element
        if self.head.cargo == num:
            ret_node = self.head
            self.head = ret_node.next
            ret_node.next = None
            self.length -= 1
            return ret_node
        
        # find the element in the list
        before = self.head
        after = self.head.next
        # while we have not found an element greater than new_node,
        # go to the next element
        while after != None and after.cargo < num:
            before = after
            after = after.next
        
        if after != None and after.cargo == num: # after points to num!!!
            # remove after
            # make before point to the element following after and 
            # make the removed node point to none
            before.next = after.next
            after.next = None
            self.length -= 1
            return after
        
        # if after is None, we have reached the end of the list
        # if not but after.cargo > num, num isn't on the list: return None in both cases
        return None
        
    def find(self, num):
        '''
        (SortedLinkedList, num) -> Node
        Return reference to a Node containing num or None if there is none
        '''
        node = self.head
        while node != None and node.cargo != num:
            node = node.next
        
        return node
            
my_list = SortedLinkedList()
print(my_list)

print("Add 20")
my_list.add(Node(20)) 
print(my_list)

print("Add 12")
my_list.add(Node(12)) 
print(my_list)

print("Add 99")
my_list.add(Node(99)) 
print(my_list)

print("Add 37")
my_list.add(Node(37))
print(my_list)

print("Find 37")
n = my_list.find(37)
print(n)
print(n.next)

print("Find 88 - not on the list")
n = my_list.find(88)
print(n)

print("** Removing **")
print("Remove 20")
n = my_list.remove(20)
print(my_list, n)

print("Remove 99")
n = my_list.remove(99)
print(my_list, n)

print("Remove 20 again - not in list")
n = my_list.remove(20)
print(my_list, n)

print("Remove 12")
n = my_list.remove(12)
print(my_list, n)

