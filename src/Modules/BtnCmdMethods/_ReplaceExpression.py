def ReplaceExpr(self,Expr):
    WolfExprCorres = {
        "arcsin(":"ArcSin[",
        "arccos(":"ArcCos[",
        "arctan(":"ArcTan[",
        "sin(":"Sin[",
        "cos(":"Cos[",
        "tan(":"Tan[",
        "ln(":"Log[",
        "log(":"Log10[",    
        "factorial(":"Factorial[",
        "abs(":"RealAbs[",
        "e":"E"
    }
    WolfExpr = Expr
    for ReplacedText in WolfExprCorres:
        WolfExpr = WolfExpr.replace(ReplacedText,WolfExprCorres[ReplacedText])
    WolfExpr = self.ReplaceBracket(WolfExpr)
    return WolfExpr

def ReplaceBracket(self,WolfExpr):
    CountBracket = 0
    for i in range(len(WolfExpr)):
        ScannedChar = WolfExpr[i]
        if ScannedChar == '[':      WolfExpr = WolfExpr[:i+1] + self.ReplaceBracket(WolfExpr[i+1:])
        if ScannedChar == '(':      CountBracket += 1
        if ScannedChar == ')':      CountBracket -= 1
        if CountBracket < 0:
            if i == len(WolfExpr):
                WolfExpr = WolfExpr[:i] + ']'
            else:
                WolfExpr = WolfExpr[:i] + ']' + WolfExpr[i+1:]
            break
    return WolfExpr
