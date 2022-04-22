# generate random points in square and check if they are in the circle

import math
import random
import turtle

class Point:
    '''Represent and manipulate a 2D point'''
    
    def __init__(self, x = 0, y = 0):
        """ 
        (self, num, num) -> NoneType
        Create a new point at x, y 
        """
        self.x = x
        self.y = y
    
    def __str__(self):
        """(self) -> str"""
        return "(" + str(self.x) + "," + str(self.y)

    def distance(self, other):
        """ 
        (self, Point) -> num
        Compute my distance to other 
        """
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)** 2)

    def distance_from_origin(self):
        """
        (self) -> num
        Compute my distance from the origin 
        """
        return self.distance(Point(0,0))

    def halfway(self, target):
        """ 
        (self, Point) -> Point
        Return the halfway point between myself and the target 
        """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

    def draw(self, t, color = "black"):
        '''
        (self, Turtle, str) -> NoneType
        Draw the Point as a dot of color color.
        '''
        t.up()
        t.goto(self.x, self.y) 
        t.dot(color)

class Square:
    """ A square represented by two points, lower-left and upper-right """
    
    def __init__(self, lower_left, upper_right):
        """ 
        (self, Point, Point) -> NoneType
        Create a new square with corners lower_left and upper_right
        """
        self.lower_left = lower_left
        self.upper_right = upper_right
    
    def __str__(self):
        """(self) -> str"""
        return "LL: " + str(self.lower_left) + ") UR: " + str(self.upper_right) + ")"
        
    def area(self):
        """
        (self) -> num
        Returns the area of the square
        """
        return ((self.upper_right.x - self.lower_left.x) *
                (self.upper_right.y - self.lower_left.y))
    
    def centre(self):
        """
        (self) -> Point
        Returns the point that is the centre of the square
        """
        return self.upper_right.halfway(self.lower_left)
    
    def generate_random_point(self):
        ''' 
        (self) -> Point
        Returns a random point, inside the Square 
        '''
        x_rand = random.random()
        x_point = self.lower_left.x + \
            x_rand * (self.upper_right.x - self.lower_left.x)
        
        y_rand = random.random()
        y_point = self.lower_left.y + \
            y_rand * (self.upper_right.y - self.lower_left.y)
        
        return Point(x_point, y_point)

    def draw(self, t):
        '''
        (self, Turtle) -> NoneType
        Draw the square at the current position and size.
        '''
        t.up()
        t.goto(self.lower_left.x, self.lower_left.y) 
        t.setheading(0) # pointing to the right
        t.down()
        # draw the square
        distance = self.upper_right.x - self.lower_left.x
        for i in range(4):
            t.forward(distance)
            t.left(90)


    
class Circle:
    """ A circle represented by a point at its centre and a radius """
    
    def __init__(self, centre, r):
        """ 
        (self, Point, num) -> NoneType
        Create a new circle with centre at centre ad radius r
        """
        self.centre = centre
        self.radius = r
    
    def check_inside(self, p):
        ''' 
        (self, Point) -> bool
        Returns True if p is inside (or on the circumference) of the 
        Circle
        '''
        return (self.centre.distance(p) <= self.radius)

    def draw(self, t):
        '''
        (self, Turtle) -> NoneType
        Draw the circle at the current position and radius.
        '''
        t.up()
        t.goto(self.centre.x, self.centre.y - self.radius) 
        t.down()
        t.circle(radius)


def display_progress(t, num_in_circle, num_points, circle):
    '''
    (Turtle, int, int, Circle) -> NoneType
    Update the progress toward estimating PI
    '''
    # use the circle location to figure out where we should write the info
    # (i.e. below the circle) 
    font_size = 20
    
    x = circle.centre.x - circle.radius
    y = 2 * x # leave a space below the circle 
    
    t.up()
    t.goto(x,y)
    t.down()
    
    s = "Points: " + str(num_points) + "\nIn circle: " + str(num_in_circle) \
        + "\nPI approx: " + str(4 * num_in_circle / num_points)
    t.clear()
    t.write(s, font=("Arial", font_size, "normal"))

num_points = int(input("Enter number of points to generate: "))

origin = Point(0,0)
radius = 100

# create a Circle
c = Circle(origin, radius)

# create a Square exactly surrounding c
# if the centre of the Square is origin and half the length of side is radius
# calculate the lower left and upper right corners
lower_left = Point(origin.x - radius, origin.y - radius)
upper_right = Point(origin.x + radius, origin.y + radius)
s = Square(lower_left, upper_right)

animate = (input("Run animation (Y/N): ").lower() == 'y')
if animate:
    alex = turtle.Turtle()
    alex.pencolor("black")
    alex.speed(0) # maximum speed
    alex.ht()        # don't show the turtle

    c.draw(alex) # draw the circle
    s.draw(alex) # draw the square

    # use a different turtle to write out the display so that we can
    # erase the previous text each time
    progress_turtle = turtle.Turtle()   
    progress_turtle.ht()
    progress_turtle.speed(0)

num_in_circle = 0
for i in range(num_points):
    p = s.generate_random_point()
    #print("Random point: ", p.x, p.y)
    if c.check_inside(p):
        num_in_circle += 1
        if animate:
            p.draw(alex,"red")
    elif animate:
        p.draw(alex,"blue")

    if animate:        
        display_progress(progress_turtle, num_in_circle, i + 1, c)
    
pi_approx = 4 * num_in_circle / num_points

print("PI approximation: ", pi_approx, flush = True)

if animate:
    turtle.done()
