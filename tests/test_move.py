'''
Test Moving result
'''

import unittest
import sys
sys.path.append("..")

from cmd import proc_cmd
from toy_robot import ToyRobot
from tests.stub import *
from tests.result import *


class MoveUnitTest(unittest.TestCase):

    def test_left_boundary(self):
        robot = ToyRobot()

        command = "PLACE 2,2,WEST\n" \
                 + "MOVE\n" \
                 + "MOVE\n"  \
                 + "MOVE\n"

        stub_stdin(self, command)

        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_PLACE)
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_MOVE)
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_MOVE)
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue()), FAIL_FALL_OFF)

    def test_right_boundary(self):
        robot = ToyRobot()

        command = "PLACE 2,2,EAST\n" \
                 + "MOVE\n" \
                 + "MOVE\n"  \
                 + "MOVE\n"

        stub_stdin(self, command)

        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_PLACE)
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_MOVE)
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_MOVE)
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue()), FAIL_FALL_OFF)

    def test_top_boundary(self):
        robot = ToyRobot()

        command = "PLACE 2,2,NORTH\n" \
                 + "MOVE\n" \
                 + "MOVE\n"  \
                 + "MOVE\n"

        stub_stdin(self, command)

        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_PLACE)
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_MOVE)
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_MOVE)
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue()), FAIL_FALL_OFF)

    def test_bottom_boundary(self):
        robot = ToyRobot()

        command = "PLACE 2,2,SOUTH\n" \
                 + "MOVE\n" \
                 + "MOVE\n"  \
                 + "MOVE\n"

        stub_stdin(self, command)

        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_PLACE)
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_MOVE)
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_MOVE)
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue()), FAIL_FALL_OFF)

    def test_leftbottom_to_righttop(self):
        robot = ToyRobot()

        command = "PLACE 0,0,NORTH\n" \
                 + ("MOVE\n" \
                 + "RIGHT\n" \
                 + "MOVE\n" \
                 + "LEFT\n" \
                 + "REPORT\n") * 4

        stub_stdin(self, command)

        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_PLACE)

        for i in range(4):
            stub_stdout(self)
            proc_cmd(robot)
            self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_MOVE)
            stub_stdout(self)
            proc_cmd(robot)
            self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_RIGHT)
            stub_stdout(self)
            proc_cmd(robot)
            self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_MOVE)
            stub_stdout(self)
            proc_cmd(robot)
            self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_LEFT)
            stub_stdout(self)
            proc_cmd(robot)
            self.assertEqual(str(sys.stdout.getvalue()), REPORT_FORMAT.format(i+1, i+1, "NORTH"))

    def test_rightbottom_to_lefttop(self):
        robot = ToyRobot()

        command = "PLACE 4,0,NORTH\n" \
                 + ("MOVE\n" \
                 + "LEFT\n" \
                 + "MOVE\n" \
                 + "RIGHT\n" \
                 + "REPORT\n") * 4

        stub_stdin(self, command)

        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_PLACE)

        for i in range(4):
            stub_stdout(self)
            proc_cmd(robot)
            self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_MOVE)
            stub_stdout(self)
            proc_cmd(robot)
            self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_LEFT)
            stub_stdout(self)
            proc_cmd(robot)
            self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_MOVE)
            stub_stdout(self)
            proc_cmd(robot)
            self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_RIGHT)
            stub_stdout(self)
            proc_cmd(robot)
            self.assertEqual(str(sys.stdout.getvalue()), REPORT_FORMAT.format(3 - i, i + 1, "NORTH"))

    def test_circle(self):
        robot = ToyRobot()

        command = "PLACE 0,4,EAST\n" \
                 + (("MOVE\n" * 4) \
                 + "RIGHT\n") * 4 \
                 + "REPORT\n"

        stub_stdin(self, command)

        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_PLACE)

        for i in range(4):
            for j in range(4):
                stub_stdout(self)
                proc_cmd(robot)
                self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_MOVE)
            stub_stdout(self)
            proc_cmd(robot)
            self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_RIGHT)

        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue()), REPORT_FORMAT.format(0, 4, "EAST"))

    def test_circle_around(self):
        robot = ToyRobot()

        command = "PLACE 2,2,SOUTH\n" \
                 + ("RIGHT\n" * 4) \
                 + "REPORT\n" \
                  + ("LEFT\n" * 4) \
                  + "REPORT\n"

        stub_stdin(self, command)

        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_PLACE)

        for i in range(4):
            stub_stdout(self)
            proc_cmd(robot)
            self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_RIGHT)

        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue()), REPORT_FORMAT.format(2, 2, "SOUTH"))

        for i in range(4):
            stub_stdout(self)
            proc_cmd(robot)
            self.assertEqual(str(sys.stdout.getvalue()), SUCCESS_LEFT)

        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue()), REPORT_FORMAT.format(2, 2, "SOUTH"))


if __name__ == '__main__':
    unittest.main()