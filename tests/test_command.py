'''
Test Command.
'''

import unittest
import sys
sys.path.append("..")

from cmd import proc_cmd
from toy_robot import ToyRobot
from tests.stub import *
from tests.result import *


class CommandUnitTest(unittest.TestCase):

    def test_unsupported_command(self):
        robot = ToyRobot()

        command = "RANDOMCOMMAND\n"
        stub_stdin(self, command)

        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue()), FAIL_UNKNOWN_COMMAND)

    # MOVE/LEFT/RIGHT/REPORT commands, no argument required,
    def test_command_extra_arguments(self):
        robot = ToyRobot()

        command = "MOVE 1\n" \
                + "LEFT 90\n" \
                + "RIGHT 90\n" \
                + "REPORT OK\n"

        stub_stdin(self, command)
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue()), FAIL_INVALID_ARGUMENTS)

        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue()), FAIL_INVALID_ARGUMENTS)

        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue()), FAIL_INVALID_ARGUMENTS)

        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue()), FAIL_INVALID_ARGUMENTS)

    # PLACE commands, 3 arguments required.
    # Format: PLACE x, y, facing. Spaces between arguments can be handled flexibly
    # The values of x and y are in the range of [0,4]
    # the value of facing can be "NORTH", "SOUTH", "EAST", "WEST", Case insensitive
    def test_command_place_arguments(self):
        robot = ToyRobot()

        command = "PLACE 0, 4, NORTH\n" \
                + "PLACE 0, 4, south\n" \
                + "PLACE 0, 4\n" \
                + "PLACE 0, NORTH\n" \
                + "PLACE NORTH\n" \
                + "PLACE 0, 0, EAST, WEST\n" \
                + "PLACE \n" \
                + "PLACE 5, 1, NORTH\n" \
                + "PLACE 1, 5, NORTH\n" \
                + "PLACE 1, 4, MIDDLE\n" \
                + "PLACE 0, 0, EAST\n" \
                + "PLACE 4, 4, WEST\n" \
                + "PLACE 4 4 WEST\n" \
                + "PLACE 2,  3,WEST\n"

        stub_stdin(self, command)
        stub_stdout(self)
        proc_cmd(robot)

        # normal: "PLACE 0, 4, NORTH\n"
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_PLACE)
        stub_stdout(self)
        proc_cmd(robot)

        # lower case facing: "PLACE 0, 4, south\n"
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_PLACE)
        stub_stdout(self)
        proc_cmd(robot)

        # missing facing: "PLACE 0, 4\n"
        self.assertEqual(str(sys.stdout.getvalue()), FAIL_INVALID_ARGUMENTS)
        stub_stdout(self)
        proc_cmd(robot)

        # missing x or y: "PLACE 0, NORTH\n"
        self.assertEqual(str(sys.stdout.getvalue()), FAIL_INVALID_ARGUMENTS)
        stub_stdout(self)
        proc_cmd(robot)

        # missing x and y: "PLACE NORTH\n"
        self.assertEqual(str(sys.stdout.getvalue()), FAIL_INVALID_ARGUMENTS)
        stub_stdout(self)
        proc_cmd(robot)

        # extra arguments: "PLACE 0, 0, EAST, WEST\n"
        self.assertEqual(str(sys.stdout.getvalue()), FAIL_INVALID_ARGUMENTS)
        stub_stdout(self)
        proc_cmd(robot)

        # no argument: "PLACE\n"
        self.assertEqual(str(sys.stdout.getvalue()), FAIL_INVALID_ARGUMENTS)
        stub_stdout(self)
        proc_cmd(robot)

        # x out of range: "PLACE 5, 1, NORTH\n"
        self.assertEqual(str(sys.stdout.getvalue()), FAIL_INVALID_POSITION)
        stub_stdout(self)
        proc_cmd(robot)

        # y out of range: "PLACE 1, 5, NORTH\n"
        self.assertEqual(str(sys.stdout.getvalue()), FAIL_INVALID_POSITION)
        stub_stdout(self)
        proc_cmd(robot)

        # unsupported facing: "PLACE 1, 4, MIDDLE\n"
        self.assertEqual(str(sys.stdout.getvalue()), FAIL_INVALID_FACING)
        stub_stdout(self)
        proc_cmd(robot)

        # boundary x and y: "PLACE 0, 0, EAST\n"
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_PLACE)
        stub_stdout(self)
        proc_cmd(robot)

        # boundary x and y: "PLACE 4, 4, EAST\n"
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_PLACE)
        stub_stdout(self)
        proc_cmd(robot)

        # no comma between arguments: "PLACE 4 4 WEST\n"
        self.assertEqual(str(sys.stdout.getvalue()), FAIL_INVALID_ARGUMENTS)
        stub_stdout(self)
        proc_cmd(robot)

        # no space or extra space between arguments: "PLACE 2,  3,WEST\n"
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_PLACE)

    # all commands are case insensitive
    def test_command_lowercase_command(self):
        robot = ToyRobot()

        command = "place 2,2,north\n" \
                + "move\n" \
                + "left\n" \
                + "right\n" \
                + "report\n" \
                + "PLACE 2,2,north\n" \
                + "MOVE\n" \
                + "LEFT\n" \
                + "RIGHT\n" \
                + "REPORT\n"

        stub_stdin(self, command)
        stub_stdout(self)
        proc_cmd(robot)

        # lower case PLACE: "place 2,2,north\n"
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_PLACE)
        stub_stdout(self)
        proc_cmd(robot)

        # lower case move: "move\n"
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_MOVE)
        stub_stdout(self)
        proc_cmd(robot)

        # lower case left: "left\n"
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_LEFT)
        stub_stdout(self)
        proc_cmd(robot)

        # lower case right: "right\n"
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_RIGHT)
        stub_stdout(self)
        proc_cmd(robot)

        # lower case report: "report\n"
        self.assertEqual(str(sys.stdout.getvalue()), REPORT_FORMAT.format(2,3,"NORTH"))
        stub_stdout(self)
        proc_cmd(robot)

        # upper case place: "PLACE 2,2,north\n"
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_PLACE)
        stub_stdout(self)
        proc_cmd(robot)

        # upper case move: "MOVE\n"
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_MOVE)
        stub_stdout(self)
        proc_cmd(robot)

        # upper case left: "LEFT\n"
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_LEFT)
        stub_stdout(self)
        proc_cmd(robot)

        # upper case right: "RIGHT\n"
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_RIGHT)
        stub_stdout(self)
        proc_cmd(robot)

        # upper case report: "REPORT\n"
        self.assertEqual(str(sys.stdout.getvalue()), REPORT_FORMAT.format(2,3,"NORTH"))

    # discard all commands in the sequence until a valid PLACE command has been executed.
    def test_command_lowercase_command(self):
        robot = ToyRobot()

        command = "MOVE\n" \
                  + "LEFT\n" \
                  + "RIGHT\n" \
                  + "REPORT\n"

        stub_stdin(self, command)
        stub_stdout(self)
        proc_cmd(robot)

        # "MOVE\n"
        self.assertEqual(str(sys.stdout.getvalue()), FAIL_NOT_PLACED)
        stub_stdout(self)
        proc_cmd(robot)

        # "LEFT\n"
        self.assertEqual(str(sys.stdout.getvalue()), FAIL_NOT_PLACED)
        stub_stdout(self)
        proc_cmd(robot)

        # "RIGHT\n"
        self.assertEqual(str(sys.stdout.getvalue()), FAIL_NOT_PLACED)
        stub_stdout(self)
        proc_cmd(robot)

        # "REPORT\n"
        self.assertEqual(str(sys.stdout.getvalue()), FAIL_NOT_PLACED)


if __name__ == '__main__':
    unittest.main()
