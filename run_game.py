'''
The application is a simulation of a toy robot moving on a square table top, of dimensions 5 units x 5 units.
There are no other obstructions on the table surface.
The robot is free to roam around the surface of the table, but must be prevented from falling to destruction.
Any movement that would result in the robot falling from the table must be prevented,
however further valid movement commands must still be allowed.

Commands:
PLACE X,Y,F
MOVE
LEFT
RIGHT
REPORT
'''
from cmd import proc_cmd
from toy_robot import ToyRobot

def run_game():
    print("Game start... ")
    robot = ToyRobot()
    while True:
        proc_cmd(robot)


if __name__ == "__main__":
    run_game()