from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl,wlexpr
import atexit

def InitWolf(self):
    self.session = WolframLanguageSession("/usr/bin/wolfram")
    self.session.evaluate(wlexpr("1+1")) #If it is not done. First calculate becom so slowly.
    atexit.register(self.TerminateWolf)

def TerminateWolf(self):
    print("wolfram terminated")
    self.session.terminate()

def EvalWolf(self,Expr):
    if ("Ans" in Expr):
        Expr = Expr.replace("Ans", self.BeforeAns)
    Expr = "N[" + Expr + "]"
    print(Expr)
    CalResult = str(self.session.evaluate(wlexpr(Expr)))
    self.BeforeAns = CalResult
    return CalResult
