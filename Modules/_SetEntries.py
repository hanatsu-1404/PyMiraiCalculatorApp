from tkinter import *
from tkinter import ttk
def SetEntry(self):
    self.EntFrame = Frame(self.Root)
    self.TextWid = Text(self.EntFrame)
    self.EntFrame.pack(side=LEFT,expand=1,fill=BOTH)
    self.TextWid.pack(expand=1,fill=BOTH)
