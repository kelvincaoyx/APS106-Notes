def editFile(fileName):
    file = open(fileName, "r")
    
    lst = []
    for i in file:
        lst.append(i.strip("\n"))
    print(lst)
    
    sawplst = []
    for i in range(0,len(lst),2):
        sawplst.append(lst[i+1])
        sawplst.append(lst[i])
    
    print(sawplst)

editFile("exam\Week13_Questions\lyrics.txt")