__author__ = 'le-user'
# -*- coding: utf-8 -*-

class Sqrt():
    def __init__(self, num = 0):
        self.num = num
        self.RunSqrt()
    def RunSqrt(self):
        Rslt = self.CulcSqrt(self.num)
        if Rslt < 0:
            str1 = "負数の平方根はありません"
        else:
            str1 = str(self.num) + "の平方根は" + str(Rslt) + "です。"
        print(str1)

    def CulcSqrt(self, Number):
        if Number == 0:
            return 0

        if Number < 0:
            return -1

        Data1 = Number
        Lmax = 50

        for Connt in range(0, Lmax):
            Data2=(Data1+(Number/Data1))/2
            Data3 = Data2 - Data1
            if Data3 < 0:
                Data3 *= -1
            if Data3 == 0:
                break
            Data1 = Data2

        return Data2

if __name__ == '__main__':
    Sqrt(255)