from tkinter import *
from tkinter import ttk
import sys

def TkDestroy(self):
    print("Do tkinter destroy session")
    self.Root.destroy()

def QuitProcesses(self):
    self.TerminateWolf()
    self.TkDestroy()
    sys.exit()

def SetQuitBtn(self):
    self.QuitBtn = Button( self.EntFrame,
                           text = "QUIT",
                           command = self.QuitProcesses
                         )
    self.QuitBtn.pack(side=BOTTOM,anchor=SW)
