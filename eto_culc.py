__author__ = 'le-user'
# -*- coding: utf-8 -*-

class EtoCulc():
    def __init__(self, Year = 0):
        self.Year = Year
        self.Dt1 = ['庚', '辛', '壬', '癸', '甲', '乙', '丙', '丁', '戊', '己']
        self.Dt2 = ['申', '酉', '戌', '亥', '子', '丑', '寅', '卯', '辰', '巳', '午', '未']
        self.Eto = self.GetEto(Year)

    def GetEto(self, Year):
        Rslt = ''
        Rslt10 = self.GetEto10(Year)
        Rslt12 = self.GetEto12(Year)
        if (Rslt10 != '') & (Rslt12 != ''):
            Rslt = Rslt10 + Rslt12
        return Rslt

    def GetEto10(self, Year):
        Rslt10 = ''
        LengDt = len(self.Dt1)
        Val = Year % 10
        if (Year >= 1) & (Val < LengDt):
            Rslt10 = self.Dt1[Val]
        return Rslt10

    def GetEto12(self, Year):
        Rslt12 = ''
        LengDt = len(self.Dt2)
        Val = Year % 12
        if (Year >= 1) & (Val < LengDt):
            Rslt12 = self.Dt2[Val]
        return Rslt12

if __name__ == '__main__':
    # 西暦を入力
    YearStr = input('干支を調べる西暦を入力してください！')
    YearInt = int(YearStr)
    Func = EtoCulc(YearInt)
    EtoStr = Func.Eto
    if EtoStr == '':
        RsltStr = '西暦を正しく入力してください！'
    else:
        RsltStr = "西暦" + str(Func.Year) + '年の干支は\"' + EtoStr + '\"です！'
    print(RsltStr)
    del Func