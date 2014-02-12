#!/usr/bin/python

class Robot:
    def __init__(self, name):
        self.name = name

    def run(self):
        print("I'm alive!")

    def talk(self, say=None):
        print("I can talk!")
        if say is not None:
            print(say)


if __name__ == "__main__":
    robot = Robot("Hal")
    robot.run()
