from tkinter.messagebox import RETRY


class CashRegister:
    def __init__(self,loonies=0,toonies=0,fives=0,tens=0,twenties=0):
        self.loonies = loonies
        self.toonies = toonies
        self.fives = fives
        self.tens = tens
        self.twenties = twenties
    
    def __str__(self):
        returny = ("loonies: " + self.loonies +"\n"
                   "toonies: " + self.toonies +"\n"
                   "fives: " + self.fives +"\n"
                   "tens: " + self.tens +"\n"
                   "twenties: " + self.twenties)
        return returny
    
    def calculate(self):
        final = (self.loonies + self.toonies*2+self.fives*5 +
                 self.tens*10 + self.twenties*20)
        return final
    
    def add(self,loonies=0,toonies=0,fives=0,tens=0,twenties=0):
        self.loonies += loonies
        self.toonies += toonies
        self.fives += fives
        self.tens += tens
        self.twenties += twenties
    
    def remove(self,dollars):
        dollarsLeft = dollars
        returnDict = {"loonies":0, "toonies": 0, "fives":0,"tens":0,"twenties":0}
        while dollarsLeft >= 20:
            dollarsLeft -= 20
            self.twenties -=1
            returnDict.update({"twenties":returnDict["twenties"]+1})
        
        while dollarsLeft >= 10:
            dollarsLeft -= 10
            self.tens -=1
            returnDict.update({"tens":returnDict["tens"]+1})
            
        while dollarsLeft >= 5:
            dollarsLeft -= 5
            self.fives -=1
            returnDict.update({"fives":returnDict["fives"]+1})
            
        while dollarsLeft >= 2:
            dollarsLeft -= 2
            self.toonies -=1
            returnDict.update({"toonies":returnDict["toonies"]+1})
            
        while dollarsLeft >= 1:
            dollarsLeft -= 1
            self.loonies -=1
            returnDict.update({"loonies":returnDict["loonies"]+1})
        
        return returnDict
        


    def make_purchase(self,cost,loonies,toonies,fives,tens,twenties):
        self.add(loonies,toonies,fives,tens,twenties)
        print(self.remove(cost))
       
# cash= CashRegister(5,3,4,2,5)

# print(cash.calculate())

# cash.remove(50)

# print(cash.calculate())

class Node:
    def __init__(self, cargo=None, prev=None, next=None):
        self.cargo = cargo
        self.prev = prev
        self.next = next
        
    def __str__(self):
        return str(self.cargo)
    
    def print_backward(self):
        '''
        (self) -> NoneType
        Recursively print the list backward
        '''
        print(self.cargo, end=" ")
        if self.prev is not None:
            self.prev.print_backward()

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
        pass

    def print_backward_nicely(self):
        '''
        (self) -> NoneType
        Recursively traverse the list printing it out in reverse order
        '''
        pass
    
    def add_first(self, cargo):
        '''
        (self, Object) -> NoneType
        Create a new Node containing cargo and insert it at the head of 
        the list
        '''
        pass
        
    def add_last(self, cargo):
        '''
        (self, Object) -> NoneType
        Create a new Node containing cargo and insert it at the end of 
        the list
        '''
        pass

    def remove_item(self, item):
        '''
        (self, Object) -> NoneType
        Find the Node containing item and remove it from the list 
        '''
        pass




        
        