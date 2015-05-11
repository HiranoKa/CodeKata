__author__ = 'le-user'
# -*- coding: utf-8 -*-

import datetime

class LeapYear():
    def __init__(self,  Year = ''):
        self.Year = self.ChekLInputeapYear(Year)
        self.Rslt = self.GetLeapYear(self.Year)

    def ChekLInputeapYear(self, Year):
        if Year.isdigit() == False:
            #数字以外が入っていたら現在の年を再設定する
            now = datetime.datetime.now()
            Rslt = int(now.strftime('%Y'))
        else:
            Rslt = int(Year)
        return Rslt

    def GetLeapYear(self, Year):
        Rslt = False
        if Year > 0:
            # 0以上が入力されたら判定実行
            if Year % 4 == 0:
                # 4で割り切れる年を閏年とする
                if Year % 400 == 0:
                    # 100で割り切れても400で割り切れる年は閏年とする
                    Rslt = True
                elif Year % 100 != 0:
                    # 但し100で割り切れない年のみ閏年とする
                    Rslt = True
        return Rslt

if __name__ == '__main__':
    # 西暦を入力
    InputStr = input('西暦で年を入力してください！')

    # 閏年の判定
    Func = LeapYear(InputStr)
    StrWk = str(Func.Year) + '年は、'
    if Func.Rslt == False:
        StrWk += '閏年ではありません！'
    else:
        StrWk += '閏年です！'
    print(StrWk)

    del Func
