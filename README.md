### Description and requirements

- The application is a simulation of a toy robot moving on a square table top, of demensions 5 units * 5 units；
- There are no other obstructions on the table surface；
- The robot is free to roam around the surface of the table, but must be prevented from falling to destruction；
- Any movement that would result in the robot falling from the table must be prevented. However further valid movement commands must still be allowed;

### Commands
- These commands can be used to control the robot's movement；
- PLACE
  - Put the toy robot on the table in position X,Y and facing F direction.
  - Usage: PLACE X, Y, F
    X is the x -coordinate
	Y is the y-coordinate
	F is the direction the robot is facing( NORTH, SOUTH, EAST or WEST)
  - All the spaces between arguments will be ingored.
  - The origin(0, 0) can be considered to be the SOUTH WEST most corner.
  - It is required that the first commands to the robot is a PLACE command, after that, any sequence of commands may be issued, in any order, including another PLACE command.
  - All the commands before a valid PLACE command can't be executed successfully.
- MOVE
  - Move the toy robot one unit forward in the direction it is currently facing.
  - Usage: MOVE
- LEFT
  - Rotate the robot 90 degress to the left without changing the position of the robot.
  - Usage: LEFT
- RIGHT
  - Rotate the robot 90 degress to the right without changing the position of the robot.
  - Usage: RIGHT
- REPORT
  - Announce the X(x-coordinate on the table), Y(y-coordinate on the table) and F(facing direction) of the robot.
  - Usage: REPORT
  - Output: X: x_coordinate, Y: y_coordinate, FACING:  facing direction.
    e.g. X: 2, Y: 2, FACING: NORTH

### To run the application
  $ python3 run_gume.py

### To test the application
- To run all the unittests: 
$ python3 -m unittest discover tests
- To run the command test suit:
$ python3 -m unittest tests/test_command.py
- To run the movement test suit:
$ python3 -m unittest tests/test_move.py
