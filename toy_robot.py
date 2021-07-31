'''
The definition of the ToyRobot
The toy robot has three main properties:
(xPos, yPos) : the coordinatie used to describe the robot's position on the table top of dimensions 5 units x 5 units.
               (0, 0): the SOUTH WEST most corner
               (4, 4): the NORTH EAST most corner
facing: the robot's facing direction NORTH, SOUTH, EAST or WEST

The toy robot has 5 public methods, all the method return the execution result in the form of a string.

place(x ,y, facing): place the robot on the table in position (x,y) and facing direction.
move(): move the top robot one unit forward in the direction it is currently facing.
left(): rotate the robot 90 degrees left without changing the position of the robot.
right(): rotate the robot 90 degrees right without changing the position of the robot.
report(): announce the xPos, yPos and facing of the robot.
'''

TABLE_WIDTH = 5
TABLE_HEIGHT = 5

# in clockwise, the order of directions is : NORTH(0) - EAST(1) - SOUTH(2) - WEST(3) - NORTH(0)
# in anti-clockwise, the order of directions is : NORTH(0) - WEST(3) - SOUTH(2) - EAST(1) - NORTH(0)
DIRECTIONS = ["NORTH", "EAST", "SOUTH", "WEST"]
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
MOVE_XY_BY_DIRECTIONS = {
                NORTH: (0, 1),
                SOUTH: (0, -1),
                EAST: (1, 0),
                WEST: (-1,0)
              }    # for a specific facing direction, the position changes in x and y axles in one move.


class ToyRobot:

    def __init__(self):
        self.__xPos = None
        self.__yPos = None
        self.__facing = None
        self.__placed = False

    @staticmethod
    def __is_on_table(x, y):
        if x < 0 or x >= TABLE_WIDTH or y < 0 or y >= TABLE_HEIGHT:
            return False
        return True

    @staticmethod
    def __get_facing_code(facing):

        try:
            return DIRECTIONS.index(facing)
        except ValueError:
            return -1

    def place(self, x, y, facing):
        # check the input parameters are valid
        if not self.__is_on_table(x, y):
            return "The initial position is invalid, should between (0,0) and (4,4)."

        facing_code = self.__get_facing_code(facing.upper())
        if -1 == facing_code:
            return "Unknown facing direction, possible values: NORTH, SOUTH, EAST, WEST(case insensitive)."

        # set _placed to True, can execute following commands
        self.__placed = True

        # update toy robot's properties
        self.__xPos = x
        self.__yPos = y
        self.__facing = facing_code

        return "Placed."

    def move(self):
        # if the robot has not been placed, no other commands can be executed except PLACE
        if not self.__placed:
            return "Toy robot has not been placed on the table."

        # get the move for both x and y axles
        x_move = MOVE_XY_BY_DIRECTIONS[self.__facing][0]
        y_move = MOVE_XY_BY_DIRECTIONS[self.__facing][1]

        # check whether the robot will fall off with the move
        if not self.__is_on_table(self.__xPos + x_move, self.__yPos + y_move):
            return "Can\'t move, toy robot will fall off the table."

        # the command can be executed, update toy robot's properties
        self.__xPos += x_move
        self.__yPos += y_move
        return "Moved."

    def right(self):
        # if the robot has not been placed, no other commands can be executed except PLACE
        if not self.__placed:
            return "Toy robot has not been placed on the table."

        # the directions are ordered in clockwise, turning right means to increase the order by 1
        self.__facing = (self.__facing + 1) % 4
        return "Turned right."

    def left(self):
        # if the robot has not been placed, no other commands can be executed except PLACE
        if not self.__placed:
            return "Toy robot has not been placed on the table."

        # the directions are ordered in clockwise, turning left means to decrease the order by 1
        self.__facing = (self.__facing - 1 + 4) % 4
        return "Turned left."

    def report(self):
        if not self.__placed:
            return "Toy robot has not been placed on the table."

        '''
        format:
        X: __x_pos, Y: __y_pos, FACING: __facing
        '''
        report_info = "X: {0}, Y: {1}, FACING: {2}.".format(self.__xPos, self.__yPos, DIRECTIONS[self.__facing])
        return report_info

