__author__ = 'le-user'
# -*- coding: utf-8 -*-
import random

class NumberGame():
    def __init__(self, MaxDt = 100):
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
                break
            elif Numb > InputDt:
                print(InputStr + 'では小さすぎます！')
            else:
                print(InputStr + 'では大きすぎます！')

class NumberGame2():
    def __init__(self, Digit = 5):
        self.Numb = []
        self.MaxDigit = Digit
        self.Numb = self.GetNumber2(self.MaxDigit)
        self.CheckNumber2(self.MaxDigit, self.Numb)

    def GetNumber2(self, MaxDigit):
        Rslt = []
        # 1文字目を生成
        Work = random.randint(1, 9)
        Rslt.append(Work)
        # 2文字目以降を生成
        while True:
            if len(Rslt) >= MaxDigit:
                # 生成文字数が最大数以上なら終了
                break
            Work = random.randint(0, 9)
            if Work not in Rslt:
                # 生成文字が以前生成されていない文字ならリストに追加
                Rslt.append(Work)
        return Rslt

    def InputNumber2(self, MaxDigit):
        while True:
            Rslt = input(str(MaxDigit) + "桁の数字を入力してください(\"e\"入力で操作中断) ：")
            if (Rslt == 'e') | (Rslt == 'E') :
                break
            if Rslt.isdigit() == False:
                print('数字以外が入力されています')
                continue
            if len(Rslt) != MaxDigit:
                print('入力桁数が違います！')
                continue
            break
        return Rslt

    def CheckNumber2(self, MaxDigit, Numb):
        print(Numb)
        while True:
            Hit = 0
            Blow = 0
            InputDt = self.InputNumber2(MaxDigit)
            if (InputDt == 'e') | (InputDt == 'E'):
                print('操作を中断します！')
                break
            for count in range(0, MaxDigit):
                Work1 = Numb[count]
                Work2 = int(InputDt[count])
                if Work1 == Work2:
                    Hit += 1
                elif Work2 in Numb:
                    Blow += 1
            if Hit == MaxDigit:
                print('全数一致、終了！')
                break
            else:
                print('Hit:%d / Blow:%d'%(Hit,Blow))

if __name__ == '__main__':
    InputDt = input('数当てゲーム(1:数当/2:Hit&Blow/e:終了)：')
    if InputDt == '1':
        strNum = input('数当てゲームを実行します、最大数を入力してください : ')
        if strNum.isdigit() == True:
            inNum = int(strNum)
            NumberGame(inNum)
        else:
            print('最大桁数に数字以外が入力されました、終了します。')
    elif InputDt == '2':
        strNum = input('数当てゲーム(Hit&Blow)を実行します、最大桁数を入力してください : ')
        if strNum.isdigit() == True:
            inNum = int(strNum)
            NumberGame2(inNum)
        else:
            print('最大桁数に数字以外が入力されました、終了します。')
