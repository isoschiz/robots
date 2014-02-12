#!/usr/bin/python

class Robot:
    def __init__(self, name):
        self.name = name

    def run(self):
        print("I'm alive!")


if __name__ == "__main__":
    robot = Robot("Hal")
    robot.run()
