def SetBtnData(self):
    self.AllBtnData = {
        "CLR":self.BtnData("CLR",lambda:self.CLRCmd()),
        "←":self.BtnData("←",lambda:self.MoveCmd("left")),
        "→":self.BtnData("→",lambda:self.MoveCmd("right")),
        "DEL":self.BtnData("DEL",lambda:self.DelCmd()),
        "SHIFT":self.BtnData("SHIFT",lambda:self.InvertShift()),
        "sinx":self.BtnData("sinx",lambda:self.InsCmd("sin(","arcsin("),
                        "arcsinx"),
        "cosx":self.BtnData("cosx",lambda:self.InsCmd("cos(","arccos("),
                        "arccosx"),
        "tanx":self.BtnData("tanx",lambda:self.InsCmd("tan(","arctan("),
                        "arctanx"),
        "√x":self.BtnData("√x",lambda:self.InsCmd("^(1/2)")),
        "x^2":self.BtnData("x^2",lambda:self.InsCmd("^2","^(1/2)"),
                        "x^(1/2)"),
        "x^y":self.BtnData("x^y",lambda:self.InsCmd("^(","^(1/("),
                        "x^(1/y)"),
        "log_a(x)":self.BtnData("log_a(x)",lambda:self.InsCmd("log((e),(","10^("),
                        "10^x"),
        "π":self.BtnData("π",lambda:self.InsCmd("π","gamma("),
                        "n!"),
        "Ans":self.BtnData("Ans",lambda:self.InsCmd("Ans")),
        "Enter":self.BtnData("Enter",lambda:self.EnterCmd()),
    }
    self.SimpleBtnNameList = ["(",")","+","-","*","/","."]
    for a in self.SimpleBtnNameList:
        self.AllBtnData[a] = self.BtnData(a,lambda n=a:self.InsCmd(n))

    for x in range(10):
        a = str(x)
        self.AllBtnData[a] = self.BtnData(a,lambda n=a:self.InsCmd(n))
