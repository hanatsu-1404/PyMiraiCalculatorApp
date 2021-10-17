def SetBtnData(self):
    self.AllBtnData = {
        "CLR":self.BtnData("CLR",lambda:self.CLRCmd()),
        "←":self.BtnData("←",lambda:self.MoveCmd("left")),
        "→":self.BtnData("→",lambda:self.MoveCmd("right")),
        "DEL":self.BtnData("DEL",lambda:self.DelCmd()),
        "SHIFT":self.BtnData("SHIFT",lambda:self.InvertShift()),
        "sin":self.BtnData("sin",lambda:self.InsCmd("sin(","arcsin("),"arcsin"),
        "cos":self.BtnData("cos",lambda:self.InsCmd("cos(","arccos("),"arccos"),
        "tan":self.BtnData("tan",lambda:self.InsCmd("tan(","arctan("),"arctan"),
        "n!":self.BtnData("n!",lambda:self.InsCmd("factorial(","abs("),"abs"),
        "^2":self.BtnData("^2",lambda:self.InsCmd("^2","^(1/2)"),"^(1/2)"),
        "^y":self.BtnData("^y",lambda:self.InsCmd("^(","^(1/("),"^(1/y)"),
        "ln":self.BtnData("log",lambda:self.InsCmd("log(","ln("),"ln"),
        "π":self.BtnData("π",lambda:self.InsCmd("π","e"),"e"),
        "Ans":self.BtnData("Ans",lambda:self.InsCmd("Ans")),
        "Enter":self.BtnData("Enter",lambda:self.EnterCmd()),
    }
    self.SimpleBtnNameList = ["(",")","+","-","*","/","."]
    for a in self.SimpleBtnNameList:
        self.AllBtnData[a] = self.BtnData(a,lambda n=a:self.InsCmd(n))#n=aとしないと、lambda式が同じ値を返してしまうから
    for x in range(10):
        a = str(x)
        self.AllBtnData[a] = self.BtnData(a,lambda n=a:self.InsCmd(n))
