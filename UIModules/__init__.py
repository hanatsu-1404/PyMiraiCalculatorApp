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

    from UIModules.BtnCmdMethods._BtnCmds import MoveCmd,InvertShift,CLRCmd,EnterCmd,InsCmd,DelCmd
    from UIModules._SetBtnLayout import SetBtn
    from UIModules._SetEntries import SetEntry
    from UIModules._SettingBtnDatas import SetBtnData
    from UIModules.BtnCmdMethods._BtnCmdUtil import RetIndexRowAndColumn,CtrlIndex
    from UIModules.BtnCmdMethods._BtnCmdUtil import RetRightMoveNum,RetLeftMoveNum
    from UIModules.BtnDataClass.BtnDataClass import BtnData
        
    def MainLoop(self):
        self.Root.mainloop()

