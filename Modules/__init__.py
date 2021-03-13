from tkinter import *
from tkinter import ttk

class MainUI:
    def __init__(self,UITitle="PyMirai Calcurator"):
        self.Root = Tk()
        self.Root.title(UITitle)
        self.Index = "1.0"
        self.LineEnd = "1.0"
        self.ShiftBool = False
        self.SetEntry()
        self.SetBtnData()
        self.SetBtn()
        self.MainLoop()

    from Modules.BtnCmdMethods._BtnCmds import MoveCmd,InvertShift,CLRCmd,EnterCmd,InsCmd,DelCmd
    from Modules._SetBtnLayout import SetBtn
    from Modules._SetEntries import SetEntry
    from Modules._SettingBtnDatas import SetBtnData
    from Modules.BtnCmdMethods._BtnCmdUtil import RetIndexRowAndColumn,CtrlIndex
    from Modules.BtnCmdMethods._BtnCmdUtil import RetRightMoveNum,RetLeftMoveNum
    from Modules.BtnDataClass import BtnData
    from Modules._InvokeWolfram import EvalWolf
        
    def MainLoop(self):
        self.Root.mainloop()

