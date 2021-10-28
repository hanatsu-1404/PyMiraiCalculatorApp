from tkinter import *
from tkinter import ttk

class MainUI:
    def __init__(self,UITitle="PyMirai Calcurator"):
        self.Root = Tk()
        self.Root.title(UITitle)
        self.Root.attributes("-fullscreen",True)
        self.Index = "1.0"
        self.LineEnd = "1.0"
        self.BeforeAns = "0"
        self.ShiftBool = False
        self.SetEntry()
        self.TextWid.tag_config("error",foreground="red")
        self.SetBtnData()
        self.SetQuitBtn()
        self.SetBtn()
        self.InitWolf()
        self.MainLoop()

    from Modules.BtnCmdMethods._BtnCmds import MoveCmd,InvertShift,CLRCmd,EnterCmd,InsCmd,DelCmd
    from Modules._SetBtnLayout import SetBtn
    from Modules._SetEntries import SetEntry
    from Modules._SettingBtnDatas import SetBtnData
    from Modules._SetQuitBtn import TkDestroy, QuitProcesses, SetQuitBtn
    from Modules.BtnCmdMethods._IndexRelation import RetIndexRowAndColumn,CtrlIndex,\
                                                            RetRightMoveNum,RetLeftMoveNum
    from Modules.BtnCmdMethods._CheckExpression import CheckExprSyntax,\
                                                        CheckParenthesesNum,CheckOpeOrder
    from Modules.BtnCmdMethods._InvokeWolfram import EvalWolf,InitWolf,TerminateWolf
    from Modules.BtnCmdMethods._ReplaceExpression import ReplaceExpr,ReplaceBracket
    from Modules.BtnDataClass import BtnData
    def MainLoop(self):
        self.Root.mainloop()
