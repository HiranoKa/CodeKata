__author__ = 'le-user'
# -*- coding: utf-8 -*-

import datetime
import calendar

class CalFunc():
    def __init__(self, Year = '', Mon = '', Type = 1):
        # 年情報設定
        self.Year = self.GetYearCalFunc(Year)
        # 月情報設定
        self.Mon = self.GetMonCalFunc(Mon)
        # カレンダー情報出力
        if Type == 2:
            self.DspCalFunc2(self.Year, self.Mon)
        elif Type == 3:
            self.HtmlCalFunc(self.Year, self.Mon)
        else:
            self.DspCalFunc(self.Year, self.Mon)

    def GetYearCalFunc(self, Year = ''):
        if Year.isdigit() == False:
            # 年情報が未入力なら現在の年を入力
            now = datetime.datetime.now()
            Rslt = int(now.strftime('%Y'))
        else:
            Rslt = int(Year)
        return Rslt

    def GetMonCalFunc(self, Mon = ''):
        if Mon.isdigit() == False:
            # 月情報が未入力なら現在の月を入力
            now = datetime.datetime.now()
            Rslt = int(now.strftime('%m'))
        else:
            Rslt = int(Mon)
            if (Rslt <= 0) | (12 < Rslt):
                # 入力された月情報が有効範囲外なら現在の月に置き換え
                now = datetime.datetime.now()
                Rslt = int(now.strftime('%m'))
        return Rslt

    def DspCalFunc(self, Year, Mon):
        calendar.setfirstweekday(calendar.SUNDAY)
        print(calendar.month(Year, Mon))

    def HtmlCalFunc(self, Year, Mon):
        OutpNm = 'Calendar.html'

        Cal = calendar.HTMLCalendar()
        file = open(OutpNm, 'w')
        file.write(Cal.formatmonth(Year, Mon))
        file.close()

    def DspCalFunc2(self, Year, Mon):
        w = ' Mo Tu We Th Fr Sa Su'
        D = calendar.monthrange(Year, Mon)[1]
        F = calendar.weekday(Year, Mon, 1)
        s = '   ' * (F+1) + '  '.join(map(str,range(1, 10))) + ' ' + ' '.join(map(str,range(10, D+1)))
        print(w, end='')
        for i, e in enumerate(s):
            print(e, end='\n' if i % len(w) == 0 or (i+1) == len(s) else '')

if __name__ == '__main__':
    Year =input("西暦年を入力してください：")
    Mon = input("月を入力してください：")
    Type = input('出力方式を指定してください(1:CUI/2:CUI-2/3:HTML):')
    CalFunc(Year, Mon, Type)