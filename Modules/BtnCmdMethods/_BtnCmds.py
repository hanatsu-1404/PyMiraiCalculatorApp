from tkinter import *
from tkinter import ttk
def MoveCmd(self,MoveDire):
    if MoveDire == "right":
        MoveNum = self.RetRightMoveNum()
    elif MoveDire == "left":
        MoveNum = self.RetLeftMoveNum()
    self.Index = self.CtrlIndex(self.Index,MoveNum)
    IndexColumn = self.RetIndexRowAndColumn(self.Index)[1]
    LineEndColumn = self.RetIndexRowAndColumn(self.LineEnd)[1]
    if IndexColumn > LineEndColumn:
        self.Index = self.LineEnd
    self.TextWid.mark_set(INSERT,self.Index)
    self.TextWid.focus_set()

def InvertShift(self):
    self.ShiftBool = not self.ShiftBool
    self.TextWid.focus_set()

def CLRCmd(self):
    self.TextWid.delete("1.0",self.LineEnd)
    self.TextWid.focus_set()

def EnterCmd(self):
    ExprText = self.TextWid.get("1.0",self.LineEnd)
    self.EvalWolf(ExprText)
    """AnsText =  "\n" + "Ans:" + self.EvalWolf(ExprText) + "\n"
    self.TextWid.insert("1.0",AnsText)
    self.Index = "1.0"
    self.LineEnd = "1.0"""

def InsCmd(self,StdText,ShiftText=None):
    InsText = StdText
    if self.ShiftBool and ShiftText != None:
        InsText = ShiftText
    self.TextWid.insert('insert',InsText)
    TextLen = len(InsText)
    self.Index = self.CtrlIndex(self.Index,TextLen)
    self.LineEnd = self.CtrlIndex(self.LineEnd,TextLen)
    self.TextWid.mark_set(INSERT,self.Index)
    self.TextWid.focus_set()

def DelCmd(self):
    MoveNum = self.RetLeftMoveNum()
    self.LineEnd = self.CtrlIndex(self.LineEnd,MoveNum)
    DelIndex = self.CtrlIndex(self.Index,MoveNum)
    InsIndex = self.Index
    self.MoveCmd("left")
    self.TextWid.delete(DelIndex,InsIndex)
