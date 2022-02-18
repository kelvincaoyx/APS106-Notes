from cgitb import small


smallestNumber = int(input("hey, enter an int and we will return the lowest number. enter negative one to exit"))
latestNumber = int(input("hey, enter an int and we will return the lowest number. enter negative one to exit"))
while latestNumber >= 0:
    if smallestNumber > latestNumber:
        smallestNumber = latestNumber
    print(smallestNumber)
    latestNumber = int(input("hey, enter an int and we will return the lowest number. enter negative one to exit"))
    
    