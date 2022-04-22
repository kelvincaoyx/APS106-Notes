import csv

class House:
    def __init__(self,number,street,type,size,floors,bedrooms,bathrooms,
                 lot,parking,facing,age,taxes,price):
        self.number = number
        self.street = street
        self.type = type
        self.size = size
        self.floors = floors
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.lot = lot
        self.parking = parking
        self.facing = facing
        self.age = age
        self.taxes = taxes
        self.price = price
        
    def __str__(self):
        return ("Address: " + self.number + " " + self.street + " Size: "  + self.size + " Price: $ "+ self.price )
        
def load(filename):
    """
    (str) -> list of WindTurbines

    Opens a csv file containing wind turbine IDs, and placement 
    info (centre coordinates and radius) and returns a list
    of WindTurbine objects for each turbine defined in the file
    """

    # TODO Complete the function
    return_list = []
    csvfile = open(filename, "r")
    reader = csv.reader(csvfile)
    csvfile.close()
    
    for i in reader:
        return_list.append(House(i[0],i[1],i[2],i[3],i[4],i[5],i[6],
                                    i[7],i[8],i[9],i[10],i[11],i[12]))
    return_list.pop(0)

    return return_list

# listOfHouses = load("exam/Week10_Questions/real_estate.csv")

# userInput = input("Enter a street name (type exit when done): ")

# return_list = []

# while userInput != "exit":
#     return_list.append(userInput)
#     userInput = input("Enter a street name (type exit when done): ")
#     #print(return_list)

# for streetName in return_list:
#     tempList = []
#     for i in listOfHouses:
#         if i.street == streetName:
#             tempList.append(i)
#     print("\nHouse on " + streetName + ":")
#     if len(tempList) == 0:
#         print("No houses on", streetName)
#     else:
#         for i in tempList:
#             print(i.__str__())

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def distance(self, secondPoint):
        return ((self.x-secondPoint.x)**2+(self.y-secondPoint.y)**2)**0.5
        
class Square:
    def __init__(self,lowerLeft,upperRight):
        self.lowerLeft = lowerLeft
        self.upperRight = upperRight
    
    def generate_random_point(self):
        

class Circle:
    def __init__(self,center,radius):
        self.center = center
        self.radius = radius
    
    def check_inside(self,point):
        distanceBetweenPOintAndCircle = self.center.distance(point)
        if distanceBetweenPOintAndCircle < self.radius:
            return True
        else:
            return False
        
circly= Circle(Point(0,0), 9)

print(circly.check_inside(Point(0,3)))