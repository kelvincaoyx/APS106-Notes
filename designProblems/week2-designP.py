import math

l1 = 1
l2 = 98
theta1 = math.radians(120)
theta2 = math.radians(45)

l1x = l1*math.cos(theta1)
l1y = l2*math.sin(theta1)

l2x = l2*math.cos(theta1+theta2)
l2y = l2*math.sin(theta1+theta2)

totalx = l1x + l2x
totaly = l1y + l2y

print("Final coodinates: (" + str(round(totalx,2)) + "," + str(round(totaly,2)) + ")")