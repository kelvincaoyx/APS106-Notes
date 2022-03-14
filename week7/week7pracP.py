import random

def sortList(integer):
    newList = []
    while integer > 0:
        newList.append(random.randrange(0,999))
        integer -= 1
    newList.sort()
    print(newList)
    return newList

#sortList(10)

def median(list):
    if len(list) % 2 == 0:
        return (list[len(list)//2] + list[len(list)//2 - 1])/2
    else:
        return list[len(list)//2]

#print(median(sortList(6)))

def fancyList(list):
    arithemicAvg= sum(list)/len(list)
    sumMultiply=list[0]
    for i in range(1,len(list)):
        sumMultiply *= list[i]
    print(sumMultiply)
    geoAvg= sumMultiply**(1/len(list))
    
    return list[0],list[-1],median(list), arithemicAvg, geoAvg

#print(fancyList(sortList(3)))

def switchStrings(string, k):
    string = string[::-1]
    numOfSegmnet = len(string)//k
    print(numOfSegmnet)
    flippedString=""
    for i in range(0,len(string),k):
        flippedString += (string[(i):i+k]) + " "
    print(flippedString)
switchStrings("Hello!", 3)

database = {"Mohamed":["A","A+","C","FZ","B-"],"Cindy":["B","B","C","A","B"],"Mustafa":["A","A+","A+","C","C"],"Stefan":["FZ","B","B","C","C"]}

def testDatabase(database,grade):
    returnList = []
    for i in database.keys():
        for j in database[i]:
            if j == grade:
                returnList.append(i)
    return returnList

print(testDatabase(database,"A"))

list3=[["EDM", [18, 0, 0, 18]], ["OTT", [0,0,0,0]], "EDM"]
box_scores = [[["MTL", [1, 0, 0, 1]], ["TOR", [1,0,1,2]], "TOR"],
 [["VAN", [1, 2, 0, 3]], ["CGY", [1,1,0,4]], "CGY"],
 [["EDM", [18, 0, 0, 18]], ["OTT", [0,0,0,0]], "EDM"]]

def testList(i):

    print(sum(i[0][1][0:3]))
    if sum(i[0][1][0:3]) != i[0][1][3]:
        return False
    if sum(i[1][1][0:3]) != i[1][1][3]:
        return False
    if i[0][1][3] >= i[1][1][3]:
        if i[2] != i[0][1]:
            return False
    if i[0][1][3] <= i[1][1][3]:
        if i[2] == i[1][0]:
            return False
    return True
                
print(testList(list3))     