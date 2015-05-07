__author__ = 'le-user'
# -*- coding: utf-8 -*-

class HellowWordLoop():
    def __init__(self, num = 5):
        self.LoopMax = num
        self.runHellowWordLoop()

    def runHellowWordLoop(self):
        Step = 0
        while Step < self.LoopMax:
            print("Hellow word!")
            Step += 1

HellowWordLoop()