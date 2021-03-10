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
    if ScannedText == None or ScannedText == "\n":
        return 0
    while(True):
    #while(ScannedTest.isalpha())にしないのは、RetLeftMoveNumメソッドと見た目を揃えるため
        ScannedIndexNum += 1
        ScannedIndex = ScannedIndex.replace(str(ScannedIndexNum-1),str(ScannedIndexNum))
        ScannedText = self.TextWid.get("insert",ScannedIndex)
        #getメソッドの引数は、インデックスが小さい方を先に渡さないといけない
        if not (ScannedText.isalpha()):
            break
    return ScannedIndexNum
"""
RetLeftMoveNumとRetRightMoveNumとでメソッドを分けてるのは良いコードが思いつかなかったのと
分けたほうが見やすそうだったから
"""
def RetLeftMoveNum(self):
    ScannedIndexNum = -1
    ScannedIndex = "insert -1c"
    ScannedText = self.TextWid.get(ScannedIndex,"insert")
    #getメソッドの引数は、インデックスが小さい方を先に渡さないといけない
    if ScannedText == None or ScannedText == "\n":
        return 0
    while(True):
    #while(ScannedTest.isalpha())にしないのは、最後にScannedIndexNum+=1を実行したいから
        ScannedIndexNum -= 1
        ScannedIndex = ScannedIndex.replace(str(ScannedIndexNum+1),str(ScannedIndexNum))
        ScannedText = self.TextWid.get(ScannedIndex,"insert")
        #getメソッドの引数は、インデックスが小さい方を先に渡さないといけない
        if not (ScannedText.isalpha()):
            ScannedIndexNum += 1
            break
        if len(ScannedText) < (ScannedIndexNum*(-1)):#
            ScannedIndexNum += 1
            break
    return ScannedIndexNum
