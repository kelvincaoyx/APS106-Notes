# print((2 < 1 and "g" > "a") or not 'a' == 'b')
# print(list(range(4,8,2)))

# f = open('f.txt', 'w')
# f.write('Hello\n')
# f.write('\n')
# f.close()
# f = open('f.txt', 'w')
# f.write('Fun!')
# f.close()

# def fun1(num):
#     if num < 0:
#         return False
#     elif num > 0:
#         return True
#     print(num ** 0.5)
# print(fun1(4))

# class Date:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day 
# class Dog:
#     def __init__(self, first_name, adoption_date):
#         self.first_name = first_name
#         self.adoption_date = adoption_date
# adoption_date = Date(2019, 3, 28)
# my_dog = Dog("Barchimedes", adoption_date)
# adoption_date = Date(2017, 1, 1) 
# adoption_date.year = 2018
# print(my_dog.adoption_date.year)


# '''
# 1 1  1
# 1 2  2
# 2 2  4
# '''

# def my_func(x,y):
#     print(x,y,end = " ")
#     return x*y
# max_num = 3
# for i in range(1,max_num):
#     for j in range(i,max_num):
#         print(my_func(i,j))

'''
416-1212
True
None
'''

# phonebook = {'Akako':'416-1212',
#  'Ke':'647-2122',
#  'Alya':'416-9923'}

# print(phonebook['Akako'])
# print("Ke" in phonebook)
# print(phonebook["Freya"])

'''
1
3
5
'''

# class Node:
#     def __init__(self, cargo = 0, next = None):
#         self.cargo = cargo
#         self.next = next
# def print_special(n, p):
#     if n is None:
#         return
#     elif p:
#         print(n.cargo)
 
#     print_special(n.next, not p)
# n = Node(1, Node(2, Node(3, Node(4, Node(5)))))
# print_special(n, True)




def stopping_criteria(num):
    if num == 6:
        return True
    return False

temps = [1,2,3,4,5,6,7,8]
selected_temps = []

def extract_nums(temps, selected_temps):
    '''([num,num,…], []) -> NoneType'''
    index = 0
    while not stopping_criteria(temps[index]):
        selected_temps.append(temps[index])
        index += 1
    
# extract_nums(temps,selected_temps)
# print(selected_temps)

# temps = [1,2,3,4,5,6,7,8]
# selected_temps = []    

# def extract_nums2(temps, selected_temps):
#     for num in temps:
#         if not stopping_criteria(num):
#             selected_temps.append(num)
#         else:
#             return

# extract_nums2(temps,selected_temps)
# print(selected_temps)


class NodeBT:
    def __init__(self, c, l = None, r = None):
        '''Creates an object of type NodeBT whose cargo value is c. 
        '''
        self.cargo = c
        self.left = l
        self.right = r

    def sum_all_nodes(self):
        ''' (NodeBT) -> num
        Returns the sum of the cargo values of all the nodes in the binary 
        tree that is rooted at self.
        Precondition: All nodes have cargo values that are integers.
        '''    
        
        final = 0
        level = [self]
        
        while len(level) > 0:
            
            level_next = []
            
            for node in level:
                final += node.cargo
                if node.left is not None:
                    level_next.append(node.left)
                if node.right is not None:
                    level_next.append(node.right)
            
            level = level_next
        return final
    
    
    
    def print_tree(self):
        level = [self]
        while len(level) > 0:
            
            level_next = []
            
            for node in level:
                print(node.cargo, " ", end = "")
                
                if node.left is not None:
                    level_next.append(node.left) 
                if node.right is not None:
                    level_next.append(node.right)
            print('\n')
            level = level_next


t = NodeBT(1, NodeBT(2), NodeBT(3, NodeBT(4)))

print(t.sum_all_nodes())

t.print_tree()


class BinaryTree:
     
    def __init__(self, tree_root):
        ''' Constructs a binary tree with the NodeBT tree_root 
        as its root.'''
        
        self.root = tree_root
    
        self.tree_sum = self.root.sum_all_nodes()



def tree_merge(new_root, t1, t2):
    '''(NodeBT, BinaryTree, BinaryTree)-> BinaryTree 
    Returns a binary tree whose root is new_root and whose 
    left and right subtrees contain the nodes of t1 and t2, 
    respectively.'''
    new_root.left = t1.root
    new_root.right = t2.root
    new_tree = BinaryTree(new_root)
    
    t1.root = None
    t2.root = None
    
    return new_tree

r1 = NodeBT(2, NodeBT(1), NodeBT(3))
t1 = BinaryTree(r1)


r2 = NodeBT(6, NodeBT(5), NodeBT(8))
t2 = BinaryTree(r2)


print("ssssss")
t1.root.print_tree()
print("ssssss")
t2.root.print_tree()
print("ssssss")

r = NodeBT(4)
t = tree_merge(r, t1, t2)

t.root.print_tree()

print("root cargo = ", t.root.cargo)
print("tree total = ", t.tree_sum)


    
class Date:
    '''
    Stores and manipulates dates from January 1, 1900
    '''
    def __init__(self,year=1900,month=1,day=1):
        self.year = year
        self.day = day
        self.month = month
    
    def __str__(self):
        months = ['', 'January', 'February', 'March', 
                  'April', 'May', 'June', 'July', 
                  'August', 'September', 'October', 'November', 'December']
        return months[self.month] + " "+ str(self.day) +", " + str(self.year)

    def valid_date(self):
        '''
        Returns True if the object contains a valid date in 1900 or later.
        Otherwise, returns False.
        Does not deal with leap years: assumes that February has 28 days 
        '''
        if self.year < 1900:
            return False
        
        if self.month < 1 or self.month > 12:
            return False
        
        if self.day <= 0:
            return False
        
        if (self.month in [1,3,5,7,8,10,12]) and self.day > 31:
            return False
        
        if (self.month in [4,6,9,11]) and self.day > 30:
            return False
        
        if (self.month == 2) and self.day > 28:
            return False
        
        return True
        
        
        
        
#print(Date(2019,2,30).valid_date())


def scramble_items(sample_list):
    '''
    [item, item,… ,item] -> [str, str,… ,str]
    Input: list of items that could be int, float, or string.
    Output: list of scrambled strings.
    '''
    returnList = []
    for item in sample_list:
        item = str(item)
        scrabledList = []
        
        for even in range(1,len(item),2):
            scrabledList.append(item[even])
        for odd in range(0,len(item),2):
            scrabledList.append(item[odd])
        
        combinedWords =""
        
        for i in scrabledList:
            combinedWords += (i)
            
        returnList.append(combinedWords)
    return returnList

sample_list = ['Elon Tusk', 420, 'Mars Rd.', 343521]
new_list = scramble_items(sample_list)
#print(new_list)

import csv
def write_scrambled_items(filename, original_data):
    '''
    (str, [[item, item,… ,item], …]) -> NoneType
    Input: a string and a nested list with list items being any 
    combination of int, float and string types.
    Output: nothing is returned. A scrambled version of the nested list 
    data is saved to filename using comma separated value format.
    '''
    scrambledList = []
    
    for i in original_data:
        scrambledList.append(scramble_items(i))
    
    with open(filename, "w") as file:
        writer = csv.writer(file)
        for i in scrambledList:
            writer.writerow(i)

# data = [['Elon Tusk', 420, 'Mars Rd.', 343521],
#  ['Haramble', 123, 'Zoo Ave.', 123456],
#  ['Snoop Dug', 42, 'Boring St.', 4578091]]
# write_scrambled_items('data.csv', data)

def calc_averages(lab_grades):
    '''
    [[str,…,str],[num,…,num], …] -> [[str, str],[num, num], …]

    Input: a nested list of strings and integers representing field names, student 
    ids and lab grades which may have ‘e’ included.
    Output: nested list containing the student ID and average grade on the labs 
    calcula
    '''
    returnLst = [['Student ID', 'Average Grade'],]
    for person in range(1,len(lab_grades)):
        studentId = lab_grades[person][0]

        totalGradeCounter = []
        for grades in lab_grades[person]:
            if grades != studentId and grades != "e":
           
                totalGradeCounter.append(grades)
        lowest = totalGradeCounter[0]
        for i in totalGradeCounter:
            if i < lowest:
                lowest = i
        totalGradeCounter.remove(lowest)
        print(totalGradeCounter)

        
        returnLst.append([studentId,sum(totalGradeCounter)/len(totalGradeCounter)])
                
    return returnLst
lab_grades = [['ID','Lab 1','Lab 2','Lab 3','Lab 4','Lab 5','Lab 6', 'Lab 7','Lab 8','Lab 9'], [1001, 5, 8, 3, 2, 
3, 6, 1, 0, 9],[1002, 9, 'e', 10, 9, 9, 9, 'e', 9, 10], [1003, 9, 
7, 9, 'e', 5, 9, 8, 6, 8]]
avg_grades = calc_averages(lab_grades)
print(avg_grades)