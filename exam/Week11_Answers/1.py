class Cash_Register:
    """A cash register."""

    def __init__(self, loonies, toonies, fives, tens, twenties):
        """ 
        (self, int, int, int, int, int) -> NoneType
        Creates a Cash_Register with loonies, toonies, fives, tens, and twenties.
        """

        self.loonies = loonies
        self.toonies = toonies
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

    def __str__(self):
        """
        (self) -> str
        Return a string representing the cash register contents
        """
        return "The cash register holds: \n20s: " + str(self.twenties) \
            + "\n10s: " + str(self.tens) + "\n5s: " + str(self.fives) \
            + "\n2s: " + str(self.toonies) + "\n1s: " + str(self.loonies)
        
    def get_total(self):
        '''
        (self) -> num
        Return the total value of the cash in the register
        '''
        return 20 * self.twenties + 10 * self.tens + 5 * self.fives + 2 * self.toonies + self.loonies

    def add(self, count, denomination):
        '''
        (self, num, str) -> NoneType
        Add count bills of size denomination to the register
        '''     
        if denomination == 'loonies':
            self.loonies += count
        elif denomination == 'toonies':
            self.toonies += count
        elif denomination == 'fives':
            self.fives += count
        elif denomination == 'tens':
            self.tens += count
        elif denomination == 'twenties':
            self.twenties += count    

    def remove(self, count, denomination):
        '''
        (self, num, str) -> NoneType
        Remove count bills of size denomination to the register
        '''
        self.add(-count,denomination)

    def remove_min(self, count, denomination):
        '''
        (self, int, str) -> int
        Removes the min of count and the number of units of denomination
        (so that we do not go below 0). Returns the number of bills removed.
        '''
        if denomination == 'loonies':
            amt_in_register = self.loonies
        elif denomination == 'toonies':
            amt_in_register = self.toonies
        elif denomination == 'fives':
            amt_in_register = self.fives
        elif denomination == 'tens':
            amt_in_register = self.tens
        elif denomination == 'twenties':
            amt_in_register = self.twenties
            
        amt_to_remove = min(count, amt_in_register)
        self.remove(amt_to_remove, denomination)
        
        return amt_to_remove
                    
                            
    def remove_amount(self, amount):
        '''
        (self, int) -> NoneType
        Calculate the to be removed to reduce the content of the register
        by amount dollars.
        '''
        
        if amount > self.get_total():
            print("I don't have that much in the register.")
            return None
        
        bills = (20,10,5,2,1)
        denominations = ("twenties", "tens", "fives", "toonies", "loonies")
        i = 0
        while amount > 0 and i < len(bills):
            num_to_remove = amount // bills[i]
            #print(bills[i], amount)
            if num_to_remove > 0:
                amt_removed = self.remove_min(num_to_remove,  denominations[i])
                amount -= bills[i] * amt_removed
                #print("\tamt remove:", bills[i], amt_removed)
            i += 1
            
        if amount > 0:
            print("Uh-oh. Something went wrong!")
        
            
        
register = Cash_Register(4, 2, 4, 5, 5)
print(register)
print(register.get_total())

register.add(3, 'fives')
register.add(4, 'loonies')
print(register.get_total())

register.remove(2, 'toonies')
register.remove(5, 'twenties')
print(register.get_total())

register.remove_amount(25)
print(register.get_total())

register.remove_amount(13)
print(register.get_total())