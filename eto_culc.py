__author__ = 'le-user'
# -*- coding: utf-8 -*-

import datetime

class EtoCulc():
    def __init__(self, Year = ''):
        self.Dt1 = ['庚', '辛', '壬', '癸', '甲', '乙', '丙', '丁', '戊', '己']
        self.Dt2 = ['申', '酉', '戌', '亥', '子', '丑', '寅', '卯', '辰', '巳', '午', '未']
        self.Year = self.ChkLInpYearGetEto(Year)
        self.Eto = self.GetEto(self.Year)

    def ChkLInpYearGetEto(self, Year):
        if Year.isdigit() == False:
            #数字以外が入っていたら現在の年を再設定する
            now = datetime.datetime.now()
            Rslt = int(now.strftime('%Y'))
        else:
            Rslt = int(Year)
        return Rslt

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

    Func = EtoCulc(YearStr)
    EtoStr = Func.Eto
    if EtoStr == '':
        RsltStr = '西暦を正しく入力してください！'
    else:
        RsltStr = "西暦" + str(Func.Year) + '年の干支は\"' + EtoStr + '\"です！'
    print(RsltStr)
    del Func