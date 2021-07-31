'''
All the executing result from the user interface.
'''

SUCCESS_PLACE = "Command: Placed.\n"
SUCCESS_MOVE = "Command: Moved.\n"
SUCCESS_LEFT = "Command: Turned left.\n"
SUCCESS_RIGHT = "Command: Turned right.\n"
REPORT_FORMAT = "Command: X: {0}, Y: {1}, FACING: {2}.\n"

FAIL_INVALID_ARGUMENTS = "Command: Invalid arguments.\n"
FAIL_UNKNOWN_COMMAND = "Command: Unknown command.\n"
FAIL_INVALID_POSITION = "Command: The initial position is invalid, should between (0,0) and (4,4).\n"
FAIL_INVALID_FACING = "Command: Unknown facing direction, possible values: NORTH, SOUTH, EAST, WEST(case insensitive).\n"

FAIL_FALL_OFF = "Command: Can\'t move, toy robot will fall off the table.\n"
FAIL_NOT_PLACED = "Command: Toy robot has not been placed on the table.\n"