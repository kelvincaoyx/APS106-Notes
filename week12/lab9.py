############################################################
# APS106 Winter 2022 - LAB 9 - Wind Turbine Placement OOP  #
############################################################

import csv
from itertools import count

class Point:
    """
    A point in a two-dimensional coordinate plane
    """
    
    def __init__(self, x, y):
        """
        Create a point with an x and y coordinate
        """
        self.x = x
        self.y = y
        
    def __str__(self):
        """
        Generate a string representation of a point
        """
        return "(" + str(self.x) + "," + str(self.y) + ")"


############################
# Part 1 - Circle Class
############################
class Circle:
    """
    A circle in a two-dimensional coordinate plane
    """
    
    def __init__(self, centre_x, centre_y, radius):
        """
        Create a rectangle defined by its bottom left and top right corner
        coordinates
        """
        self.centre = Point(centre_x, centre_y)
        self.radius = radius
        
    def __str__(self):
        """
        Generate a string representation of a rectangle
        """
        return ("Circle with centre coordinate " + 
                str(self.centre) + " and radius " + str(self.radius))
    
    def move(self, horizontal_translation, vertical_translation):
        """
        (Circle, int, int) -> None
        
        Alters the location of a circle by translating the coordinates
        of its centre coordinates.
        """
        # TODO complete the method
        self.centre.x = self.centre.x + horizontal_translation
        self.centre.y = self.centre.y + vertical_translation
        
    def overlap(self, circB):
        """
        (Circle, Circle) -> bool
        
        Checks whether two circles overlap, return true if they overlap, false otherwise
        """
        
        # compute the distance between the centres
        d = ((self.centre.x - circB.centre.x) ** 2 + (self.centre.y - circB.centre.y) ** 2) ** (1/2)
        return d < (self.radius + circB.radius)

##############################
# Part 2 - Wind Turbine Class
##############################
class WindTurbine:
    """
    A wind turbine placed in a two-dimensional area
    """
    
    def __init__(self, id_number, placement_centre_x, placement_centre_y, placement_radius):
        """
        Create a wind turbine
        """
        self.id_number = id_number
        self.placement = Circle(placement_centre_x,placement_centre_y, placement_radius)
        
        self.overlapping_turbines = []
    
    def __str__(self):
        """
        Generate a string representation of a WindTurbine object
        """
        return ("Wind Turbine ID: " + str(self.id_number) + 
                ", Placement: " + str(self.placement))

        
    def move(self, horizontal_translation, vertical_translation):
        """
        (WindTurbine, int, int) -> None
        
        Alters the location of a wind turbine by translating the coordinates
        of its bottom left and top right corner coordinates. After moving the 
        turbine, the overlapping turbine list should be reset to an empty
        list.
        
        The change in the x and y coordinates are specified by the
        horizontal_translation and vertical_translation parameters, respectively.
        """
        # TODO complete the method (approx. 2 lines of code)
        self.placement.centre.x = self.placement.centre.x + horizontal_translation
        self.placement.centre.y = self.placement.centre.y + vertical_translation
        
    def overlap(self, turbineB):
        """
        (WindTurbine, WindTurbine) -> bool
        
        Checks for overlap between a wind turbine and another turbine (turbineB).
        """
        # TODO complete the method (approx. 1 line of code)
    
        return self.placement.overlap(turbineB.placement)
            
    def validate_placement(self, turbines):
        """
        (WindTurbine, list of WindTurbines) -> None
        
        Check if the postion of a wind turbine is valid by checking for
        overlapping areas with all other wind turbines.
        """
        # TODO complete the method (approx. 3-4 lines of code)
        for tur in turbines:
            if tur.id_number != self.id_number:
                if self.placement.overlap(tur.placement):
                    self.overlapping_turbines.append(tur)

##########################################
# Part 3 - Load Wind Turbines from File
##########################################

def load_turbine_placements(turbine_filename):
    """
    (str) -> list of WindTurbines

    Opens a csv file containing wind turbine IDs, and placement 
    info (centre coordinates and radius) and returns a list
    of WindTurbine objects for each turbine defined in the file
    """

    # TODO Complete the function
    return_list = []
    csvfile = open(turbine_filename, "r")
    reader = csv.reader(csvfile)

    for i in reader:
        return_list.append(WindTurbine(i[0],i[1],i[2],i[3]))
    
    return_list.pop(0)
    return return_list

##########################################
# Part 4 - Testing Wind Turbine Placement
##########################################

def check_turbine_placements(turbines):
    """
    (list of WindTurbines) -> int
    
    Checks a list of wind turbines to identify turbines with invalid (overlapping)
    placements. The function should return the number of turbines with 
    invalid placements.
    
    All placements should be evaluated using the validate_placement method from
    the WindTurbine class.
    """
    
    ## TODO complete the function
    counter = 0
    
    for first_turbine in turbines:
        first_turbine.validate_placement(turbines)
        counter += len(first_turbine.overlapping_turbines)
    
    if counter > 1:
        factor = 2
        while factor < counter:
            counter = counter/factor
            factor += 1
    return factor