__author__ = 'le-user'
# -*- coding: utf-8 -*-

class LeapYear():
    def __init__(self,  Year = 0):
        self.Year = Year
        self.Rslt = self.GetLeapYear(self.Year)

    def GetLeapYear(self, Year):
        Rslt = False
        if Year > 0:
            # 0以上が入力されたら判定実行
            if Year % 4 == 0:
                # 4で割り切れる年を閏年とする
                if Year % 100 == 0:
                    # 但し100で割り切れる場合は平年とする
                    if Year % 400 == 0:
                        # 但し400で割り切れる場合は閏年になる
                        Rslt = True
                else:
                    Rslt = True
        return Rslt

if __name__ == '__main__':
    # 西暦を入力
    InputStr = input('西暦で年を入力してください！')

    # 閏年の判定
    InputData = int(InputStr)
    Func = LeapYear(InputData)
    StrWk = str(Func.Year) + '年は、'
    if Func.Rslt == False:
        StrWk += '閏年ではありません！'
    else:
        StrWk += '閏年です！'
    print(StrWk)

    del Func
