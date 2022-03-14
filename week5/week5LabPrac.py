def switchCases(string):
    return string.swapcase()

print(switchCases("Hello"))

def removeOtherCases(string):
    newString = ""
    for i in string:
        if i != "!" and i !="?":
            newString += i
    return newString

print(removeOtherCases("He????llo!????"))

def nameTest():
    userInput = input("PLz enter ur full name").lower()
    myName = "kelvin"
    if len(myName) <= len(userInput) and userInput == userInput[0:len(myName)]:
        print("how did you know my name?")
    else:
        print("It's rude to not know my name")
        
def flippNumbers(number):
    flippedNumber = 0
    
    while number > 0:
        onesPlace = number % 10
        flippedNumber = flippedNumber*10 + onesPlace
        number //= 10
    
    return flippedNumber

print(flippNumbers(9876543))

def flipstring(string):
    
    return int(string[::-1])

print(flipstring("12345"))