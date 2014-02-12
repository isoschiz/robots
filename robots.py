#!/usr/bin/python

import sys

class Robot:
    def __init__(self, name):
        self.name = name

    def run(self):
        print("I'm alive! I am {}".format(self.name))


if __name__ == "__main__":
    name = "Hal" if len(sys.argv) == 1 else sys.argv[1]
    robot = Robot(name)
    robot.run()
