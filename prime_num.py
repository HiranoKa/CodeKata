__author__ = 'le-user'
# -*- coding: utf-8 -*-

class PrimeNum():
    def __init__(self, num = 0):
        self.num = num
        self.GetPrimeNum2()

    def GetPrimeNum2(self):
        if self.num <= 0:
            print('1以上の数値を入力してください！！')
        else:
            count = 2
            while count < self.num:
                self.result = self.CalcPrimeNum(count)
                if self.result == True:
                    print(count)
                count += 1

    def GetPrimeNum(self, number):
        if number <= 0:
            print('1以上の数値を入力してください！！')
        else:
            self.result = self.CalcPrimeNum(number)
            str1 = self.num
            if self.result == True:
                str2 = "は素数です"
            else:
                str2 = 'は素数ではありません'
            print(str2)

    def CalcPrimeNum(self, number):
        if number == 0:
            return False
        if number == 1:
            return False
        count = 2
        while count < number:
            if number % count == 0:
                return False
            count += 1
        return True

if __name__ == '__main__':
    PrimeNum(239)
