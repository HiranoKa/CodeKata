__author__ = 'le-user'
# -*- coding: utf-8 -*-

class ArrFunc():
    def __init__(self, Dt =[0]):
        self.ArrDt = Dt
        print(self.ArrDt)
        self.ChgArrFunc(self.ArrDt)
        print(self.ArrDt)

    def ChgArrFunc(self, Dt):
        print('先頭以外の要素を0に置き換える')
        for index in range(len(Dt)):
            # 先頭以外の要素を0に置き換える
            if index != 0:
                Dt[index] = 0

if __name__ == '__main__':
    ArrDt = [3, 5, 2, 4, 2]
    ArrFunc(ArrDt)