def swtichCases(string):
    newString=""
    for i in string:
        if i.isupper():
            newString += i.lower()
        else:
            newString += i.upper()
    print(newString)
    
swtichCases("HelloHowAreYou")


def switchStrings(string, k):
    numOfSegmnet = len(string)//k
    print(numOfSegmnet)
    flippedString=""
    for i in range(0,len(string),k):
        flippedString += (string[(i):i+k])[::-1] + " "
    print(flippedString)
switchStrings("University", 2)

def test(bedSlope,waveHeight,waterWaveLength):
    iribarrenNumber= tan(bedSlope)/(waveHeight/waterWaveLength)**2
    if iribarrenNumber < 3.3:
        print