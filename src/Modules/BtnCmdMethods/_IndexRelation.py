def RetIndexRowAndColumn(self,Index):
    SplittedIndex = Index.split('.')
    RetRow = int(SplittedIndex[0])
    RetColumn = int(SplittedIndex[1])
    return RetRow,RetColumn

def CtrlIndex(self,Index,MoveNum):
    TempRow,TempColumn = self.RetIndexRowAndColumn(Index)
    TempColumn += MoveNum
    if TempColumn < 0:
        TempColumn = 0
    RetIndex = str(TempRow) + '.' + str(TempColumn)
    return RetIndex

def RetRightMoveNum(self):
    ScannedIndexNum = 1
    ScannedIndex = "insert +1c"
    ScannedText = self.TextWid.get("insert",ScannedIndex)#getメソッドの引数は、Indexが小さい方を先に渡さないといけない
    CountBracket = 0
    if ScannedText == None or ScannedText == "\n":
        return 0
    while(ScannedText[-1].isalpha()):
        if ScannedText == 'e' or ScannedText == 'π':break
        ScannedIndexNum += 1
        ScannedIndex = ScannedIndex.replace(str(ScannedIndexNum-1),str(ScannedIndexNum))
        ScannedText = self.TextWid.get("insert",ScannedIndex)#getメソッドの引数は、Indexが小さい方を先に渡さないといけない
    return ScannedIndexNum

"""RetLeftMoveNumとRetRightMoveNumとでメソッドを分けてるのは良いコードが思いつかなかったのと
分けたほうが見やすそうだったから"""

def RetLeftMoveNum(self):
    ScannedIndexNum = -1
    ScannedIndex = "insert -1c"
    ScannedText = self.TextWid.get(ScannedIndex,"insert")#getメソッドの引数は、Indexが小さい方を先に渡さないといけない
    if ScannedText == None or ScannedText == "\n":
        return 0
    DoWhile = False     #while文が実行されていたら特別な処理を実行したいので、実行されたか確認するための変数
    CountParentheses = 0    #１個目の(は認識させたいが、2個目以降は認識させたくないので個数をカウントするための変数
    while(ScannedText[0].isalpha() or (ScannedText[0] == '(')):
        if ScannedText == 'e' or ScannedText == 'π':break
        if len(ScannedText) < (ScannedIndexNum*(-1)):break      #Indexが先頭などにあり、それ以上左を参照できないと無限ループするのでその対策
        if ScannedText[0] == '(':CountParentheses += 1
        if CountParentheses >= 2:break
        DoWhile = True
        ScannedIndexNum -= 1
        ScannedIndex = ScannedIndex.replace(str(ScannedIndexNum+1),str(ScannedIndexNum))
        ScannedText = self.TextWid.get(ScannedIndex,"insert")#getメソッドの引数は、Indexが小さい方を先に渡さないといけない
    if DoWhile is True:     
        ScannedIndexNum += 1
    return ScannedIndexNum
