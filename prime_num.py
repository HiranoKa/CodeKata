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
            for count in range(2, self.num):
                self.result = self.CalcPrimeNum(count)
                if self.result == True:
                    print(count)
                count += 1

    def GetPrimeNum(self, number):
        if number <= 0:
            print('1以上の数値を入力してください！！')
        else:
            self.result = self.CalcPrimeNum(number)
            str1 = str(number)
            if self.result == True:
                str2 = "は素数です"
            else:
                str2 = 'は素数ではありません'
            print(str1+str2)

    def CalcPrimeNum(self, number):
        if number == 0:
            return False
        if number == 1:
            return False
        for count in range(2, number):
            if number % count == 0:
                return False
        return True

if __name__ == '__main__':
    PrimeNum(239)
