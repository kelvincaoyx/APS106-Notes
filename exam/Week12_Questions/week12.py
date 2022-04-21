class Node:
    def __init__(self,cargo,next):
        self.cargo = cargo
        self.next = next
    
    def __str__(self):
        return self.cargo

class sorted_linked:
    def __init__(self):
        self.length = 0
        self.head = None
    
    def add(self, newNode):
        
        if self.head == None or self.head.cargo > newNode.cargo:
            newNode.next = self.head
            self.head = newNode
        
        else:
            before = self.head
            after = self.head.next
            
            while after != None or after >= newNode.cargo:
                before = after
                after = after.next
        
            before.next = newNode
            newNode.next = after
        
        self.length += 1

    def remove(self, number):
        current = 
    def len(self):
        on = self.head
        leng = 0
        while on.next != None:
            leng += 1
            on = on.next

        return leng
    
    def find(self,findingNode):
        
        current = self.head
        
        while current.cargo != findingNode or current != None:
            current = current.next 
        
        return current
        