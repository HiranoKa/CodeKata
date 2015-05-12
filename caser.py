__author__ = 'le-user'
# -*- coding: utf-8 -*-

class CaserFunc():
    def __init__(self, strChpher, strHint):
        # 暗号キー
        self.strKey = "abcdefghijklmnopqrstuvwxyz .,-"
        self.strRslt = ""

        self.ShiftStrCaseFunc(strChpher, strHint)

    def ShiftOneCaserFunc(self, strDt):
        # 変換文字を戻り地として初期設定
        strRslt = strDt
        # ';'は置換すべき文字列ではないので除外する
        if strDt != ';':
            # 暗号化解除
            KeyLen = len(self.strKey)
            for Step in range(KeyLen):
                if strDt == self.strKey[Step]:
                    # 変換文字を1文字シフトする
                    if (Step + 1) < KeyLen:
                        strRslt = self.strKey[Step + 1]
                        break
                    else:
                        # 暗号キーの最終位置である時は先頭位置
                        strRslt = self.strKey[0]
                        break
        return strRslt

    def ShiftStrCaseFunc(self, strChpher, strHint):
        LpCnt = 0
        LpMax = len(self.strKey)
        while True:
            self.strRslt = ""
            for Indx in range(len(strChpher)):
                self.strRslt += self.ShiftOneCaserFunc(strChpher[Indx])
            strChpher = self.strRslt
            if strHint in self.strRslt:
                # 暗号解除文内にヒントと一致する文章があれば完了
                break
            LpCnt += 1
            if LpCnt >= LpMax:
                # 暗号解除に失敗(解除実行最大回数を超えた)
                self.strRslt = ""
                break

if __name__ == '__main__':
    # 暗号文
    strChpher = "qdq-gi.q-a ziatmxxitmdqibtqi-ustbi ri.qmoqrcxi.qbubu zir -ibtqi-qp-qaai ripmymsqkir -ibtqi-qy dmxi ri.cnxuoi rruoumxakir -ibtqiqzmobyqzbkii-q.qmxi -imyqzpyqzbi rixmeaki -puzmzoqai -i-qscxmbu zaimzpir -i btq-iymbbq-a;iz -iatmxximzgi.q-a zinqiuzimzgiemgipuao-uyuzmbqpimsmuzabir -ia. za -uzsiacotiimi.qbubu zj"
    # ヒント
    strHint = "person"

    Func = CaserFunc(strChpher, strHint)
    print('暗号文:')
    print(strChpher)
    print('暗号解除文：')
    strWork = Func.strRslt
    if strWork != "":
        print(strWork)
    else:
        print("暗号解除失敗！！")

    del Func