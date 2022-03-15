'''
a = [(1,1),(2,4),(3,9)]

a += a

a = a*2

#a[1][1] =3

a[-1] = (2,4)

print(a)

list_a = ['cd'] 
set_a = set(list_a) 
print(set_a)
set_b = set('cd') 

print(set_b)
set_a = set_a.union(set_b)

print(set_a)

L = [1, 2, 3, 4] 
L += [5] 
print(L)
print(L.append(6))



import math 
 
def check_num(num): 
    if num % 2 == 0: 
        return False 
 
    root = int(math.sqrt(num)) 
 
    for f in range(3,root+1,2): 
        if num % f == 0: 
            return False 
 
    return True 
 
for n in range(27, 30): 
    print(n, check_num(n)) 


course = "APS106" 
cut_from_start = True 
while "P" in course: 
    print(course) 
    if cut_from_start: 
        course = course[1:] 
    else: 
        course = course[:-1] 
 
    cut_from_start = not cut_from_start
    
i = 0 
j = 6 
 
while 0 < j < 10: 
 
    print(i, end = " ") 
     
    if j % 3 == 0: 
        j = j // 2 
    elif j% 2 == 0: 
        j = j * 2 
    else: 
        j = j + 1 
 
    i += 1 
    print(j) 
    
'''

def calc_means(points): 
    ''' 
    ([(num, num), (num, num), ...]) -> (num,num) 
    Input: a list of tuples, each tuple representing a point 
	Output:  a tuple where each entry contains the mean of 
	corresponding entries in the input tuples (e.g., the first  
    entry in the returned tuple is the mean of 
    the first entries in the input tuples, etc.) 
    ''' 
    xValueCounter = 0
    yValueCounter = 0
    numberOfPoints = len(points)
	
    for coordinatePair in points:
        xValueCounter += coordinatePair[0]
        yValueCounter += coordinatePair[1]
    
    return xValueCounter/numberOfPoints, yValueCounter/numberOfPoints

#print(calc_means([(0,2),(3,4)]) )

def calc_line_of_best_fit(points): 
    ''' 
    ([(num, num),(num, num), ...]) -> (num, num) 
    Input: a list of tuples, each tuple representing a point 
    Output: a tuple containing the slope and y-intercept of the best 
    fit line for the points in the input list 
    ''' 
    numeratorCollector = 0
    demominatorCollector = 0
    mean = calc_means(points)
    for coordinate in points:
        numeratorCollector += (coordinate[0]-mean[0])*(coordinate[0]-mean[1])
        demominatorCollector += (coordinate[0]-mean[0])**2

    slope = numeratorCollector/demominatorCollector

    return slope, (mean[1] - slope*mean[0])

#print(calc_line_of_best_fit([(1,2),(3,4)]))

string='''Project 24,Mary,Word,Excel 
Project 24,Sarah,SolidWorks,PowerPoint 
Project 25,John,MATLAB,Word,PowerPoint 
Project 26,Tom,Wing101 
Project 26,Mary,Word,Wing101 
Project 26,Tom,SolidWorks'''

def load_data(filename): 
    '''(str) -> {str : {str, str, ...}} 
    Input: a string specifying the CSV filename 
    Output: a dictionary with employee names as keys and a software    
    expertise as values 
    '''     
    #print(string)
    list1 = string.split("\n")
    
    directory = dict()
    for person in range(len(list1)):
        list1[person] = list1[person].split(",")
        #print(person)
    
    
    for person in list1:
        personName = person[1]
        #print(personName)
        tools = person[2:]
        #print(tools)
        directory.update({personName:tools})
    return directory
    
    
#print(load_data(string))

def reverse_dictionary(employees_to_software): 
    '''({str : {str, str, ...}}) -> {str : {str, str, ...}} 
    Input: a dictionary with employee names as keys and a software 
    expertise as values 
    Output: a dictionary with software as keys and employee names as 
    values 
    ''' 
    keys = []
    
    for items in employees_to_software:
        values = employees_to_software.get(items)
        keys.extend(values)
        
    keys = set(keys)
    reversedDict = {}
    
    print(keys)
    for program in keys:
        tempList = set()
        for user in employees_to_software:
            if program in employees_to_software.get(user):
                tempList.add(user)
        reversedDict.update({program:tempList})
    
    print(reversedDict)

#reverse_dictionary(load_data(string))
'''
car_info = (("Prius", 1998), (39.9, "MPG"), [133032, "km"])
car_info += ("Red",)
car_info[0] = ("Cobalt", 2009)
car_info *= 2
car_info[2][0] += 2000 
'''
def func1(mult=10, reps=2): 
    result_list=[] 
    for i in range(1, reps+1): 
        result_list.append(i*mult) 
    return mult, result_list 
'''
print(func1(5, 3))  
print(func1(reps=1))  

l1 = [1,2,3,4]

l2 = l1

print(l1)
print(l2)

l1 +=[5]

print(l1)
print(l2)

tuplea = "c", "d"
tupleb = ("d", "c")

print(tuplea == tupleb)


my_var = ('Python') * 4 
print(my_var)
print(type(my_var)) 

b = {'Lowry':1,'VanVleet':2,'Siakam':3} 
print(b['Lowry','VanVleet'])

'''
def least_likely(particle_to_probability):  
    """ (dictionary of {str: float}) -> str 
    3. 
    4. Return the particle from particle_to_probability with the 
    5. lowest  probability. 
    6. """ 

    smallest = 1  
    name = '' 
   
    for particle in particle_to_probability:  
        probability = particle_to_probability[particle]  
        if probability <= smallest: 
            smallest = probability  
            name == particle 
    return name

#print(least_likely({'Hasanium': 0.55, 'Beckium': 0.21, 'Varium': 0.03, 'Rosium': 0.07}))


def vector_add(vectors): 
    ''' 
    ([(num, num, num), (num, num, num), ...]) -> tuple (num, num, num) 
    Input: a list of tuples, each tuple representing a 3-d vector 
	Output:  a tuple which contains the vector resulting from addition 
	(i.e., the first tuple entry is the x value of the resultant 
	vector, the second is the y value and the third is the z value) 
    ''' 
    xCollector = 0
    yCollector = 0
    zCollector = 0

    for singleVector in vectors:
        xCollector += singleVector[0]
        yCollector += singleVector[1]
        zCollector += singleVector[2]

    return xCollector, yCollector, zCollector

#resultant = vector_add([(0,2,1),(1,-2,2),(1,2,-4)])  
#print(resultant) 

import math

def calc_mag_dir(list):
    '''
    (list) -> (tuple)
    
    Takes in a list of vectors and then outputs a tuple
    that contains its magnitude and its direction vecotr
    '''
    totalVectors = vector_add(list)
    
    magnitude = (totalVectors[0]**2 + totalVectors[1]**2 + totalVectors[2]**2)**(0.5)
    
    
    x = totalVectors[0]/magnitude
    y = totalVectors[1]/magnitude
    z = totalVectors[2]/magnitude
    
    return magnitude, tuple([x,y,z])

#(mag, dirV) = calc_mag_dir([(0,2,1),(1,-2,2),(1,2,-4)])  
#print(mag)
#print(dirV)

identities = ['John', 'Sarah', 'Candice', 'Alex'] 
toppings = [['pepperoni', 'mushrooms', 'blackolives'],  
['mushrooms', 'onions', 'greenpeppers', 'extracheese'], 
['pineapple', 'spinach'], ['sausage', 'mushrooms', 'pineapple', 
'onions']] 

def topping_dict(identities, toppings): 
    ''' 
    (list, list of lists) -> dictionary of {str: tuple} 
    Converts a list of names and list of nested lists of toppings 
        into a dictionary of tuples of toppings indexed by corresponding 
name 
    ''' 
    
    directory = dict()
    for i in range(len(identities)):
        name = identities[i]
        toppingThingy = tuple(toppings[i])
        directory.update({name:toppingThingy})
    return directory

dict_of_toppings = topping_dict(identities, toppings) 
#print(dict_of_toppings)  

def topping_set(toppings): 
    ''' 
    (list of lists of str) -> set of str 
    Converts a list of lists of toppings to a set containing all 
    toppings in the original lists 
    ''' 
    toppingSet = set()
    
    for outerList in toppings:
        for innerListItem in outerList:
            toppingSet.add(innerListItem)
            
    return toppingSet

set_of_toppings = topping_set(toppings) 
#print(set_of_toppings)     

def popular_toppings(dict_of_toppings, set_of_toppings, num_times): 
    ''' 
    (dictionary of {str: tuple}, set of str, int) -> list of str 
    Uses a dictionary containing classmate names and topping choices 
    along with the set of all possible topping choices to return the 
    list of toppings that were chosen at least num_times by 
    classmates. 
    ''' 
    returnListOfToppings = []
    for topping in set_of_toppings:
        tempCounter = 0
        for nameOfPerson in dict_of_toppings:
            for toppingChosen in dict_of_toppings.get(nameOfPerson):
                if toppingChosen == topping:
                    tempCounter += 1
                
        
        if tempCounter >= num_times:
            returnListOfToppings.append(topping)
    return returnListOfToppings

fav_toppings = popular_toppings(dict_of_toppings,set_of_toppings,2) 
#print(fav_toppings) 
#['onions', 'mushrooms', 'pineapple'] 



'''            
phonebook = {'Sam':'416−1212', 
             'Katie':'647−2122', 
             'Joan':'416−9923'} 
phonebook['Mike'] = '416-1000' 
 
print('416-1000' in phonebook) 
print(phonebook['Sam']) 

number = 10 
divisor = 1 
list_divisors = [] 
while divisor < number: 
    if number % divisor == 0:           
        list_divisors += [divisor] 
    divisor += 1 
 
print(list_divisors)
'''


def euclidean_distance(p, q): 
    '''(list, list) -> float 
    Input: two lists, p and q, of floating point numbers 
 
    Output: the Euclidean distance between p and q as a floating 
    point number 
 
    Pre-conditions: p and q have the same size and contain only 
    floating point numbers. 
    ''' 
    collector = 0
    for i in range(len(p)):
        collector += (p[i] - q[i])**2
    
    return collector**0.5

print(euclidean_distance([1, 1], [4, 5])) 
print(euclidean_distance([1.5, -1.1, 4], [4.2, 1, -2.3]))

def find_minmax_distances(points): 
    '''(list of lists) -> (num, num) 
    Input: a nested list of floating point numbers representing at   
    least three points in an n-dimensional space 
 
    Output: a tuple (min, max) containing the minimum and the maximum 
    Euclidean distance between all pairs of two different points 
 
    Pre-conditions: all sub-lists have the same size and contain 
    only floating point numbers. 
    ''' 
    shortestDistance = euclidean_distance(points[0], points[1])
    longestDistance = euclidean_distance(points[0], points[1]) 
    for i in range(len(points)):
        for j in range(len(points)):
            if i != j:
                distance = euclidean_distance(points[i],points[j])
                if distance < shortestDistance:
                    shortestDistance = distance
                if distance > longestDistance:
                    longestDistance = distance
    
    return shortestDistance, longestDistance

points = [[1,2,3], [1,1,4], [1,-2,3], [1,0,1], [10,0,-1]] 
#print(find_minmax_distances(points))

inventory_dict = {'gloves': [[120, 'Toronto'], [240, 'Vancouver']],'bucket': [[200, 'Toronto']]}

#print("12".isnumeric())


def check_inventory(inventory, product, amount): 
    '''(dictionary, str, int) -> bool 
    Return True if the total amount of product in inventory 
    is greater than or equal to amount. Otherwise return False 
 
    Preconditions: the input arguments are all in the correct format 
    ''' 
    stockCollector = 0
    for stock in inventory[product]:
        stockCollector += stock[0]
    
    return stockCollector >= amount
'''  
print(check_inventory(inventory_dict, 'gloves', 300))

print("askdj3".isnumeric())

string_b="Going to do awesome on my midterm"
string_b = string_b.upper()
string_b.lower()
print(string_b)
string_b = string_b[5:0:-2]
print(string_b)

string="Tisha the cat"


for i in string:
    print(i)
    
print(1%2)
'''



def replaceStuff(string,numbers):
    newString = ""
    for letter in range(len(string)):
        if string[letter] in numbers:
            newString += "!"
        else:
            newString += string[letter]
        
    print(newString)
    
#replaceStuff("APS-106 Hello! Today is March 11th. ", {"1","2","3","4"})

def box(n):
    firstLast = "*"*n
    between = "*" + " "*(n-2) + "*"
    
    final = firstLast + "\n"
    for i in range(n-2):
        final += between + "\n"
    final += firstLast
    
    print(final)

#box(5)


def angle(list):
    returnDict = dict()
    for i in list:
        returnDict.update({i:[math.cos(math.radians(i)),math.sin(math.radians(i))]})
    print(returnDict)

angle({30,40,50,60,70})
        


    