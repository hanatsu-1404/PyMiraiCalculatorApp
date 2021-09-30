def CheckParenthesesNum(self,Expr):
    LeftParentheses = Expr.count('(')
    RightParentheses = Expr.count(')')
    if LeftParentheses != RightParentheses:
        self.TextWid.insert("1.0","\nParentheses Error\n","error")
        self.TextWid.insert("1.0",Expr)
        self.TextWid.mark_set("insert","1.0")
        return False
    return True

def CheckOpeOrder(self,Expr):
    AllOpe = ['*','/','^','(']
    TextBuff = ""
    for ScannedChar in Expr:
        if ScannedChar in AllOpe:   TextBuff += ScannedChar
        else:TextBuff = ""
        if TextBuff == "((" or TextBuff == "^(":\
            TextBuff = ""
        if len(TextBuff) >= 2:
            self.TextWid.insert("1.0","\nOperator Error\n","error")
            self.TextWid.insert("1.0",Expr)
            self.TextWid.mark_set("insert","1.0")
            return False
    return True

def CheckExprSyntax(self,Expr):
    ParenthesesBool = self.CheckParenthesesNum(Expr)
    OpeBool = self.CheckOpeOrder(Expr)
    if ParenthesesBool is True and OpeBool is True:     return True
    else:   return False
