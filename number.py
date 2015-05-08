__author__ = 'le-user'
# -*- coding: utf-8 -*-
import random

class NumberGame():
    def __init__(self, MaxDt = 1000):
        self.MaxDt = MaxDt
        self.Numb = self.GetNumber(self.MaxDt)
        self.ChkNumber(self.Numb, self.MaxDt)

    def GetNumber(self, MaxDt):
        Numb = random.randint(1, MaxDt)
        return Numb

    def ChkNumber(self, Numb, Max):
        while True:
            InputStr = input("1から" + str(Max) + "の範囲で値を入力してください。")
            InputDt = int(InputStr)
            if Numb == InputDt:
                print(InputStr + 'で正解です！')
                break;
            elif Numb > InputDt:
                print(InputStr + 'では小さすぎます！')
            else:
                print(InputStr + 'ではおおきすぎます！')

class NumberGame2():
    def __init__(self, Digit = 5):
        self.MaxDigit = Digit
        self.GetNumber2(self.MaxDigit)

    def GetNumber2(self, MaxDigit):
        min = 10**MaxDigit
        max = min * 9 + 9
        for cnt in range(2, MaxDigit):
            max = max + 9 * (10**(cnt - 1))
        Numb = random.randint(min, max)
        return Numb



NumberGame2()