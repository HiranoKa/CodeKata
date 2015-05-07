__author__ = 'le-user'
# -*- coding: utf-8 -*-

class FizzBuzz():
    def __init__(self, count = 10):
        self.count = count
        self.runFizzBuzz()

    def runFizzBuzz(self):
        i = 1
        while i <= self.count :
            str = self.getStr(i)
            print(str)
            i += 1

    def getStr(self, num):
        str = num
        if (num % 3 == 0) & (num % 5 == 0):
            str = 'FizzBuzz'
        else:
            if num % 5 == 0:
                str = 'Buzz'
            if num % 3 == 0:
                str = 'Fizz'
        return str

if __name__ == '__main__':
     FizzBuzz(20)