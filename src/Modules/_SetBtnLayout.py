from tkinter import *
from tkinter import ttk
def SetBtn(self):
    self.BtnFrame = Frame(self.Root)
    self.BtnFrame.pack(side=RIGHT,expand=1,fill=BOTH)
    self.BtnLayout = [  "CLR" , "←"   , "→"   , "SHIFT"   ,
                        "sin", "cos", "tan", "DEL"     ,
                        "n!"  , "^2"  , "^y"  , "ln"      ,
                        "π"   , "("   , ")"   , "+"       ,
                        "7"   , "8"   , "9"   , "-"       ,
                        "4"   , "5"   , "6"   , "*"       ,
                        "1"   , "2"   , "3"   , "/"       ,
                        "."   , "0"   , "Ans" , "Enter"    
                    ]
    BtnRowNum = 0
    BtnColumnNum = 0
    BtnPad = 10 
    for MakedBtnName in self.BtnLayout:
        if BtnColumnNum == 4:
            BtnColumnNum = 0
            BtnRowNum += 1
        MakedBtnData = self.AllBtnData[MakedBtnName]
        BtnText = MakedBtnData.BtnDispVal
        ShiftText = MakedBtnData.ShiftDispVal
        MakedBtn = Button(  self.BtnFrame,
                            text="{}\n{}".format(BtnText,ShiftText),
                            command=MakedBtnData.BtnCmd
                        )
        MakedBtn.grid(row=BtnRowNum,column=BtnColumnNum,sticky=N+E+S+W)
        self.BtnFrame.rowconfigure(BtnRowNum,weight=1)
        self.BtnFrame.columnconfigure(BtnColumnNum,weight=1)
        BtnColumnNum += 1
