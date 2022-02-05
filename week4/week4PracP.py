def numCounter(num):
    '''
    (int) -> int
    
    takes in an integer and counts the number
    of digits in it
    '''
    num = abs(num)
    count = 1
    while num // 10 != 0:
        num //= 10
        count += 1
    return count


def flipper(num):
    '''
    (int) -> int 
    takes in a number and then flips it
    '''
    
    count = numCounter(num)
    
    flippedNum = 0
    placeholder = 1
    while count != 0:
        flippedNum += ((num // 10**(count-1)) * (placeholder))
        num %=10**(count-1)
        placeholder *= 10
        print(flippedNum)
        count -= 1
    

def intergerAsker():
    num = int(input("plz enter integer"))
    
    neg_int = 0
    pos_int = 0
    while num != 0:
        if num > 0:
            pos_int += 1
        else:
            neg_int += 1
        num = int(input("plz enter integer"))
    print ("you entered", pos_int,"pos & neg", neg_int)
    
    
