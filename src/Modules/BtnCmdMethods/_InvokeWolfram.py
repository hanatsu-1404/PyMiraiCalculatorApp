from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl,wlexpr
import atexit

def InitWolf(self):
    self.session = WolframLanguageSession("usr/bin/wolfram")
    atexit(self.TerminateWolf())

def TerminateWolf(self):
    self.session.terminate()

def EvalWolf(self,Expr):
    Expr = 'N[' + Expr + ']'
    print(Expr)
    """with WolframLanguageSession("/usr/bin/wolfram") as session:
        CalResult = session.evaluate(wlexpr(Expr))
    return str(CalResult)"""
