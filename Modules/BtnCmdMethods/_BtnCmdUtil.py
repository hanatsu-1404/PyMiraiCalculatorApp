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
    ScannedText = self.TextWid.get("insert",ScannedIndex)
    #getメソッドの引数は、インデックスが小さい方を先に渡さないといけない
    CountBracket = 0
    if ScannedText == None or ScannedText == "\n":
        return 0
    while(ScannedText[-1].isalpha()):
        ScannedIndexNum += 1
        ScannedIndex = ScannedIndex.replace(str(ScannedIndexNum-1),str(ScannedIndexNum))
        ScannedText = self.TextWid.get("insert",ScannedIndex)
        #getメソッドの引数は、インデックスが小さい方を先に渡さないといけない
    return ScannedIndexNum

"""RetLeftMoveNumとRetRightMoveNumとでメソッドを分けてるのは良いコードが思いつかなかったのと
分けたほうが見やすそうだったから"""

def RetLeftMoveNum(self):
    ScannedIndexNum = -1
    ScannedIndex = "insert -1c"
    ScannedText = self.TextWid.get(ScannedIndex,"insert")
    #getメソッドの引数は、インデックスが小さい方を先に渡さないといけない
    DoWhile = False
    CountBracket = 0
    if ScannedText == None or ScannedText == "\n":
        return 0
    while(ScannedText[0].isalpha() or (ScannedText[0] is '(')):
        if len(ScannedText) < (ScannedIndexNum*(-1)):
            break
        if ScannedText[0] is '(':
            CountBracket += 1
        if CountBracket >= 2:
            break
        DoWhile = True
        ScannedIndexNum -= 1
        ScannedIndex = ScannedIndex.replace(str(ScannedIndexNum+1),str(ScannedIndexNum))
        ScannedText = self.TextWid.get(ScannedIndex,"insert")
        #getメソッドの引数は、インデックスが小さい方を先に渡さないといけない
    if DoWhile is True:
        ScannedIndexNum += 1
    return ScannedIndexNum
