from requests import head


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



on = head
prev = None
stack = []

while on is not none or len(strack) > 0:
    next_stack = []
    while on.next is not none:
        next_stack.append(on)
        on = on.left
    
    on = next_stack.pop
    
    if prev is not None and on.cargo <= prev.cargo:
        return False
    
    prev = on
    on = on.right
    
    
