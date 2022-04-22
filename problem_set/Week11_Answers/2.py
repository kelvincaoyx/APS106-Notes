class Cash_Register2:
    """A cash register."""

    def __init__(self, loonies, toonies, fives, tens, twenties):
        """ 
        (self, int, int, int, int, int) -> NoneType
        Creates a Cash_Register with loonies, toonies, fives, tens, and twenties.
        """

        self.cash = {"loonies" : loonies, "toonies" : toonies,
                     "fives" : fives, "tens" : tens, "twenties" : twenties}

    def __str__(self):
        """
        (self) -> str
        Return a string representing the cash register contents
        """
        return "The cash register holds: \n20s: " + str(self.cash["twenties"]) \
            + "\n10s: " + str(self.cash["tens"]) \
            + "\n5s: " + str(self.cash["fives"]) \
            + "\n2s: " + str(self.cash["toonies"]) \
            + "\n1s: " + str(self.cash["loonies"])
        
    def get_total(self):
        '''
        (self) -> num
        Return the total value of the cash in the register
        '''
        return 20 * self.cash["twenties"] + 10 * self.cash["tens"] \
               + 5 * self.cash["fives"] + 2 * self.cash["toonies"] \
               + self.cash["loonies"]

    def add(self, count, denomination):
        '''
        (self, num, str) -> NoneType
        Add count bills of size denomination to the register
        '''     
        self.cash[denomination] += count

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
        
        amt_to_remove = min(count, self.cash[denomination])
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
                amt_removed = self.remove_min(num_to_remove, denominations[i])
                amount -= bills[i] * amt_removed
                #print("\tamt remove:", bills[i], amt_removed)
            i += 1
            
        if amount > 0:
            print("Uh-oh. Something went wrong!")
        
            
        
register = Cash_Register2(4, 2, 4, 5, 5)
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