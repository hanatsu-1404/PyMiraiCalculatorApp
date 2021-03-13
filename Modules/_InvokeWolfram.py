from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl,wlexpr
from wolframclient.language.exceptions import WolframLanguageException

def EvalWolf(self,Expr):
    Expr = 'N[' + Expr + ']'
    print(Expr)
    """with WolframLanguageSession("/usr/bin/wolfram") as session:
        CalResult = session.evaluate(wlexpr(Expr))
    return str(CalResult)"""
