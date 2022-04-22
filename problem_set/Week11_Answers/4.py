import random

class World_Model:
    '''
    A class that picks a location for a robot on a map, keeps track of the
    robot when it moves, and provides accorate sensor readings.
    '''
    
    def __init__(self, wold_map):
        '''
        (self, list) -> None
        Saves the map and randomly chooses a position on the map for the
        robot
        '''
        self.world_map = world_map
        self.robot_position = random.randrange(len(world_map))
        print("Secret robot position is: ", self.robot_position)
        
    def robot_move(self):
        '''
        (self) -> None
        Record the new position of the robot after a move to the left
        '''
        self.robot_position += 1
        if self.robot_position >= len(self.world_map): # wrap around
            self.robot_position = 0
        print("(Secret robot position is now:", self.robot_position)
        
    def read_sensor(self):
        '''
        (self) -> str
        Returns the color of the current cell of the robot
        '''
        return self.world_map[self.robot_position]
        
class Robot:
    """ An object that can localize itself"""
    
    def __init__(self, map, world_model):
        """
        (self, list, World_Model) -> None
        Initialize map and store world_model
        """
        self.map = map
        self.possible_locations = set(range(len(map))) 
        self.world_model = world_model
               
    def move(self):
        '''
        (self) -> None
        Move the robot one step to the right and re-calculate possible 
        locations
        '''
        print("*** MOVE ***")
        
        # inform the world model of the move
        self.world_model.robot_move()

        new_locations = set()
        # Increment each possible location by 1 as long as we don't run
        # off the map
        for loc in self.possible_locations:
            loc += 1
            if loc >= len(self.map): # assume the map wraps around
                loc = 0
            new_locations.add(loc)                
                
        self.possible_locations = new_locations    
        

    def sense(self):
        """
        (self) -> str
        Prompt the world_model for measurement at current state and return it
        """
        return self.world_model.read_sensor()
    
    def localize(self, sensor_value):
        """Examine all the possible locations and remove those that are
        not consistent with sensor_value
        """
        # self.possible_locations contains the set of possible locations
        # given the new sensor_value remove any of the elements of the list
        # that can no longer be the current position
        new_locations = set()
        for loc in self.possible_locations:
            if self.map[loc] == sensor_value:
                new_locations.add(loc)
        
        self.possible_locations = new_locations

    def has_possible_locations(self):
        """
        (self) -> bool
        Return True if the robot has at least one location where it could be
        """
        return self.possible_locations

    def is_localized(self):
        """
        (self) -> bool
        Return True if the robot has only one location where it could be
        """
        return len(self.possible_locations) == 1

    def __str__(self):
        """
        (self)->str
        Return information about the state of the Robot in a string
        """
        s = "-------------\n"
        if self.is_localized():
            s += "\nLocalized at position: " + str(self.possible_locations) + "\n"
        else:
            s += "Not localized. Possible locations: " + str(self.possible_locations) + \
            "\n-------------\n"      
        return s

# initialize map of the world
world_map = ['white','black','black','white','white','black','white','black','black',
       'black','black','white','white','black','white','white','black','white',
       'black','white','white','black','black','white','black','white','black']

print("The map looks like this: ", world_map)
#print("\nPick a location for the robot (but keep it secret).")

# create localization instance
sensor = World_Model(world_map)
robot = Robot(world_map, sensor)

print("Before doing anything")
print(robot)

sensor_value = robot.sense()
robot.localize(sensor_value)
print(robot)

while(robot.has_possible_locations() and not robot.is_localized()):
    robot.move()
    sensor_value = robot.sense()
    robot.localize(sensor_value)
    print(robot)

if (not robot.has_possible_locations()):
    print("Failure. Robot does not know where it is.")
else:
    if sensor.robot_position in robot.possible_locations:
        print("Success! The robot is successfully localized at position: ", 
              sensor.robot_position)
    else:
        print("Failure! Robot location is", sensor.robot_position,
              "but it thinks it is at", robot.possible_locations)
    
