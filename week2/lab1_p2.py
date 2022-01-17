# APS106 Lab 1 - Drawing Shapes with Turtle
# Student Name: Kelvin Cao
# PRA Section: 0107


################################################
# Part 2 - Draw your initials
################################################

# provide access to the Turtle module
import turtle

# bring the turtle to life and call it alex
alex = turtle.Turtle()


# use alex to draw your first and last initials
# TODO: WRITE YOUR CODE HERE
# tell alex where to go
alex.setheading(90)     # make alex face north
alex.down()             # make alex put pen down
alex.forward(100)        # make alex go 100 forward
alex.right(180)          # make alex turn right 90 degree
alex.forward(50)   # make alex go forward for 20
alex.left(135)           # make alex turn to the left for 135 degree
alex.forward(50*2**(1/2))       # make alex go forward 50*sqrt(2) steps
alex.left(180)    #make alex turn 180 degrees
alex.forward(50*2**(1/2))   # make alex go forward 50*sqrt(2) steps
alex.left(90)   # make alex turn to the left for 90 degree
alex.forward(50*2**(1/2))   # make alex go forward 50*sqrt(2) steps
alex.right(180) # make alex turn to the right for 180 degree
alex.forward(50*2**(1/2))   # make alex go forward 50*sqrt(2) steps

alex.up()   # make alex lift pen 
alex.setheading(0)  # make alex face east
alex.forward(130)   # make alex go 130 forward
alex.left(90)       # make alex turn to the left for 90 degree
alex.forward(50)    # make alex go 50 forward
alex.left(90)       # make alex turn to the left for 90 degree
alex.down()         # make alex put pen down
alex.circle(50,180) # make alex draw a circle

turtle.done()
