import sys
from tkinter import *
#from archlex import*

#import semantics
from archlex import *
from archlexfinal import *
#from syntaxfinal import *



try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import Archer_support


tokctr = 0
toktype = []
tokvalue = []
syntaxerror=[]

INT=[]
FLOAT=[]
CHAR=[]
STR=[]
BOOLEAN=[]
VOID=[]
semanticerrors=[]
dictionary = {}
previousToken=' '
previousValue=' '

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    Archer_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    Archer_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

    

class Toplevel1:
            
    def program(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        self.globaldec()
        if(toktype[tokctr] == "MainFunctionBegin"):
            tokctr+=1
            if(toktype[tokctr] == "LCURLY"):
                tokctr+=1
                self.statement()
                if (toktype[tokctr] == "RCURLY"):
                    tokctr+=1
                    if (toktype[tokctr] == "MainFunctionEnd"):
                        tokctr+=1
                        return
                    else:
                        syntaxerror.append("Syntax Error! Unexpected token {}, Expected token \'^SHOOT\'".format(tokvalue[tokctr]))
                        return
                else:
                    syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] +", Expected token \'}\'")
                    return
            else:
                syntaxerror.append("Syntax Error! Unexpected token "+ tokvalue[tokctr] +", Expected token \'{\'")
                return
        else:
            syntaxerror.append("Syntax Error! Unexpected token "+ tokvalue[tokctr] + ", Expected token \'^AIM, CONS, DOJO, VOID, INT, FLOAT, CHAR, STR, BOOLEAN\'")
    
    def globaldec(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        globaldecfirstset=['CONS', 'DOJO', 'VOID', 'INT', 'FLOAT', 'CHAR', 'STR', 'BOOLEAN']
        if(tokvalue[tokctr] not in globaldecfirstset):
            return
        else:
            self.globalchoice()
            self.globaldec()
    
    def globalchoice(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        datatypeset = ['INT', 'FLOAT', 'STR', 'CHAR', 'BOOLEAN']
        if(tokvalue[tokctr] == "CONS"):
            tokctr+=1
            self.datatype()
            if(toktype[tokctr] == "ID"):
                tokctr+=1
                self.consarray()
                if(tokvalue[tokctr] == "="):
                    tokctr+=1
                    self.constantvalue()
                    self.constantnext()
                    if(tokvalue[tokctr] == "|"):
                        tokctr+=1
                        return
                    else:
                        syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'|\'")
                        return
                else:
                    syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[
                        tokctr] + ", Expected token \'=\'")
                    return
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[
                        tokctr] + ", Expected token \'ID\'")
                return
        elif(tokvalue[tokctr] == "DOJO"):
            tokctr+=1
            if(toktype[tokctr] == "ID"):
                tokctr+=1
                if (tokvalue[tokctr] == "{"):
                    tokctr+=1
                    self.structbody()
                    if (tokvalue[tokctr] == "}"):
                        tokctr+=1
                        self.structid()
                        if (tokvalue[tokctr] == "|"):
                            tokctr+=1
                            return
                        else:
                            syntaxerror.append(
                                "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'|\'")
                            return
                    else:
                        syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'}\'")
                        return
                else:
                    syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'{\'")
                    return
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID\'")
                return
        elif(tokvalue[tokctr] == "VOID"):
            tokctr+=1
            if (toktype[tokctr] == "ID"):
                tokctr+=1
                if (tokvalue[tokctr] == "("):
                    tokctr+=1
                    self.param()
                    if (tokvalue[tokctr] == ")"):
                        tokctr+=1
                        if (tokvalue[tokctr] == "{"):
                            tokctr+=1
                            self.statement()
                            if (tokvalue[tokctr] == "}"):
                                tokctr+=1
                                return
                            else:
                                syntaxerror.append(
                                    "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'}\'")
                                return
                        else:
                            syntaxerror.append(
                                "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'{\'")
                            return
                    else:
                        syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \')\'")
                        return
                else:
                    syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'(\'")
                    return
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID\'")
                return
        elif(tokvalue[tokctr] in datatypeset):
            tokctr+=1
            if (toktype[tokctr] == "ID"):
                tokctr+=1
                self.functvar()
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID\'")
                return
        else:
            return
    
    def functvar(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        firstsetfunctvar = ['|', '=', ',', '[', '(']
        if(tokvalue[tokctr] not in firstsetfunctvar):
            syntaxerror.append("Syntax Error! Unexpected token "+ tokvalue[tokctr] + ", Expected token \'|, =, ,, [, (\'")
        else:
            if(tokvalue[tokctr] == "=" or tokvalue[tokctr] == "," or tokvalue[tokctr] == "[" or tokvalue[tokctr] == "|"):
                self.datachoices()
                if(tokvalue[tokctr] == "|"):
                    tokctr+=1
                    return
                else:
                    syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'|\'")
            else:
                self.functiondec()
    
    def constantvalue(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        firstsetconstantvalue = ["LCURLY", "ID", "INTLit", "FLOATLit", "CHARLit", "STRLit", "BoolTrue", "BoolFalse"]
        if(toktype[tokctr] not in firstsetconstantvalue):
            syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'{,ID,INTLit,FLOATLit,CHARLit,STRLit,TRUE,FALSE\'")
        else:
            if(tokvalue[tokctr] == "{"):
                tokctr+=1
                self.value()
                self.valuenext2()
                if(tokvalue[tokctr] == "}"):
                    tokctr+=1
                else:
                    syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'}\'")
            else:
                self.value()
    
    def valuenext2(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == ","):
            tokctr+=1
            self.value()
            self.valuenext2()
        else:
            return
    
    def constantnext(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == ","):
            tokctr+=1
            self.inputvar()
            if (tokvalue[tokctr] == "="):
                tokctr+=1
                self.constantvalue()
                self.constantnext()
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'=\'")
                return
        else:
            return
    
    def datachoices(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if (tokvalue[tokctr] == "=" or tokvalue[tokctr] == ","):
            self.vardec()
        elif(tokvalue[tokctr] == "["):
            self.array()
        else:
            return
    
    def vardec(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "="):
            tokctr+=1
            self.value()
            self.digitid()
            self.vardecnext()
        elif(tokvalue[tokctr] == ","):
            self.vardecnext()
        else:
            return
    
    def vardecnext(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == ","):
            tokctr+=1
            if(toktype[tokctr] == "ID"):
                tokctr+=1
                self.datachoices()
            else:
                syntaxerror.append("Syntax Error! Unexpected token "+ tokvalue[tokctr] + ", Expected token \'ID\'")
                return
        else:
            return
    
    def literals(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        firstsetliterals = ["INTLit", "FLOATLit", "CHARLit", "STRLit", "BoolTrue", "BoolFalse"]
        if(toktype[tokctr] not in firstsetliterals):
            syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'TRUE, FALSE, INTLit, FLOATLit, CHARLit, STRLit \'")
        else:
            tokctr+=1

    def consarray(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "["):
            tokctr+=1
            self.arraysize()
            if(tokvalue[tokctr] == "]"):
                tokctr+=1
                self.consarraynext()
            else:
                syntaxerror.append("Syntax Error! Unexpected token "+ tokvalue[tokctr] + ", Expected token \']\'")
                return
        else:
            return

    def consarraynext(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "["):
            tokctr+=1
            self.arraysize()
            if(tokvalue[tokctr] == "]"):
                tokctr+=1
            else:
                syntaxerror.append("Syntax Error! Unexpected token "+ tokvalue[tokctr] + ", Expected token \']\'")
                return
        else:
            return
    
    def array(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "["):
            tokctr+=1
            self.arraysize()
            if(tokvalue[tokctr] == "]"):
                tokctr+=1
                self.arraynext()
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \']\'")
                return
        else:
            syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'[\'")
    
    def arraysize(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(toktype[tokctr] == "INTLit"):
            tokctr+=1
        elif(toktype[tokctr] == "ID"):
            self.inputvar()
        else:
            syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID, INTLit\'")
    
    def arraynext(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "="):
            tokctr+=1
            if(tokvalue[tokctr] == "{"):
                tokctr+=1
                self.value()
                self.digitid()
                self.literalnext()
                if(tokvalue[tokctr] == "}"):
                    tokctr+=1
                    self.vardecnext()
                else:
                    syntaxerror.append("Syntax Error! Unexpected token "+ tokvalue[tokctr] + ", Expected token \'}\'")
                    return
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'{\'")
                return
        elif(tokvalue[tokctr] == "["):
            tokctr+=1
            self.arraysize()
            if(tokvalue[tokctr] == "]"):
                tokctr+=1
                self.arraynext2()
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \']\'")
                return
        else:
            self.vardecnext()
    
    def literalnext(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == ","):
            tokctr+=1
            self.value()
            self.digitid()
            self.literalnext()
        else:
            return
    
    def arraynext2(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "="):
            tokctr+=1
            if(tokvalue[tokctr] == "{"):
                tokctr+=1
                self.arrayval()
                self.arrayvalnext()
                if(tokvalue[tokctr] == "}"):
                    tokctr+=1
                    self.vardecnext()
                else:
                    syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'}\'")
                    return
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'{\'")
                return
        else:
            self.vardecnext()
    
    def arrayval(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "{"):
            tokctr+=1
            self.value()
            self.digitid()
            self.literalnext()
            if(tokvalue[tokctr] == "}"):
                tokctr+=1
                return
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'}\'")
                return
        else:
            syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'{\'")
            return
    
    def arrayvalnext(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == ","):
            tokctr+=1
            self.arrayval()
            self.arrayvalnext()
        else:
            return
    
    def structid(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(toktype[tokctr] == "ID"):
            tokctr+=1
            self.arraystruct()
        else:
            return
    
    def arraystruct(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "["):
            tokctr+=1
            self.arraystructsize()
            if(tokvalue[tokctr] == "]"):
                tokctr+=1
                self.arraystructsizenext()
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \']\'")
        elif(tokvalue[tokctr] == ","):
            tokctr+=1
            if(toktype[tokctr] == "ID"):
                tokctr+=1
                self.arraystruct()
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID\'")
                return
        else:
            return
    
    def arraystructsize(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if (toktype[tokctr] == "INTLit"):
            tokctr += 1
        elif (toktype[tokctr] == "ID"):
            self.inputvar()
        else:
            syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID, INTLit\'")
    
    def arraystructsizenext(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if (tokvalue[tokctr] == "["):
            tokctr += 1
            self.arraystructsize()
            if (tokvalue[tokctr] == "]"):
                tokctr += 1
                self.arraystruct2dnext()
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \']\'")
        elif (tokvalue[tokctr] == ","):
            tokctr += 1
            if (toktype[tokctr] == "ID"):
                tokctr += 1
                self.arraystruct()
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID\'")
                return
        else:
            return
    
    def arraystruct2dnext(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if (tokvalue[tokctr] == ","):
            tokctr += 1
            if (toktype[tokctr] == "ID"):
                tokctr += 1
                self.arraystruct()
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID\'")
                return
        else:
            return
    
    def structbody(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        firstsetstructbody = ["INT", "CHAR", "FLOAT", "STR", "BOOLEAN"]
        if(tokvalue[tokctr] in firstsetstructbody):
            self.datatype()
            if(toktype[tokctr] == "ID"):
                tokctr+=1
                self.arraystruct()
                if(tokvalue[tokctr] == "|"):
                    tokctr+=1
                    self.structbody()
                    return
                else:
                    syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token '|'")
                    return
        else:
            return
    
    def structaccess(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if (tokvalue[tokctr] == "."):
            tokctr += 1
            if (toktype[tokctr] == "ID"):
                tokctr += 1
                self.structaccessarray()
                return
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID\'")
                return
        else:
            return
    
    def structaccessarray(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if (tokvalue[tokctr] == "["):
            tokctr += 1
            self.arraystructsize()
            if (tokvalue[tokctr] == "]"):
                tokctr += 1
                self.structaccessarraynext()
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \']\'")
        else:
            return
    
    def structaccessarraynext(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if (tokvalue[tokctr] == "["):
            tokctr += 1
            self.arraystructsize()
            if (tokvalue[tokctr] == "]"):
                tokctr += 1
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \']\'")
        else:
            return
    
    def structfuncarray(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "["):
            tokctr+=1
            self.value()
            if(tokvalue[tokctr] == "]"):
                tokctr+=1
                self.structfuncarraynext()
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \']\'")
                return
        elif(tokvalue[tokctr] == ","):
            tokctr+=1
            if(toktype[tokctr] == "ID"):
                tokctr+=1
                self.structfuncarray()
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID\'")
                return
        else:
            return
    
    def structfuncarraynext(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if (tokvalue[tokctr] == "["):
            tokctr += 1
            self.value()
            if (tokvalue[tokctr] == "]"):
                tokctr += 1
                self.structfuncarraynext2()
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \']\'")
                return
        elif (tokvalue[tokctr] == ","):
            tokctr += 1
            if (toktype[tokctr] == "ID"):
                tokctr += 1
                self.structfuncarray()
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID\'")
                return
        else:
            return
    
    def structfuncarraynext2(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if (tokvalue[tokctr] == ","):
            tokctr += 1
            if (toktype[tokctr] == "ID"):
                tokctr += 1
                self.structfuncarray()
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID\'")
                return
        else:
            return
    
    def functiondec(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "("):
            tokctr+=1
            self.param()
            if(tokvalue[tokctr] == ")"):
                tokctr+=1
                if (tokvalue[tokctr] == "{"):
                    tokctr+=1
                    self.statement()
                    if (tokvalue[tokctr] == "}"):
                        tokctr+=1
                        return
                    else:
                        syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'}\'")
                        return
                else:
                    syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'{\'")
                    return
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \')\'")
                return
        else:
            syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'(\'")
    
    def param(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        datatypeset = ['INT', 'FLOAT', 'STR', 'CHAR', 'BOOLEAN']
        if(tokvalue[tokctr] in datatypeset):
            self.datatype()
            if(toktype[tokctr] == "ID"):
                tokctr+=1
                self.paramnext()
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID\'")
                return
        else:
            return
    
    def paramnext(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if (tokvalue[tokctr] == ","):
            tokctr+=1
            self.datatype()
            if (toktype[tokctr] == "ID"):
                tokctr += 1
                self.paramnext()
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID\'")
                return
        elif(tokvalue[tokctr] == "["):
            tokctr+=1
            if(tokvalue[tokctr] == "]"):
                tokctr+=1
                self.paramnext2()
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \']\'")
                return
        else:
            return
    
    def paramnext2(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if (tokvalue[tokctr] == ","):
            tokctr+=1
            self.param()
        elif (tokvalue[tokctr] == "["):
            tokctr += 1
            if (tokvalue[tokctr] == "]"):
                tokctr += 1
                self.paramnext3()
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \']\'")
                return
        else:
            return
    
    def paramnext3(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if (tokvalue[tokctr] == ","):
            tokctr += 1
            self.param()
        else:
            return
    
    def returns(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "RETURN"):
            tokctr+=1
            self.returnbody()
            if(tokvalue[tokctr] == "|"):
                tokctr+=1
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'|, + , - , *, / , % \'")
        else:
            syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'RETURN\'")
    
    def returnstate(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        firstsetreturnstate = ["ID", "INTLit", "FLOATLit", "CHARLit", "STRLit", "BoolTrue", "BoolFalse"]
        if(toktype[tokctr] in firstsetreturnstate):
            self.value()
            self.digitnext()
        else:
            return
    
    def returnbody(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "("):
            tokctr+=1
            self.returnstate()
            if(tokvalue[tokctr] == ")"):
                tokctr+=1
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \')\'")
                return
        else:
            self.returnstate()
    
    def functparam(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        firstsetfunctparam = ["ID", "INTLit", "FLOATLit", "CHARLit", "STRLit", "BoolTrue", "BoolFalse"]
        if(toktype[tokctr] in firstsetfunctparam):
            self.value()
            self.digitnext()
            self.functparamnext()
        else:
            return
    
    def functparamnext(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == ","):
            tokctr+=1
            self.functparam()
        else:
            return
    
    def value(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        firstsetvalue = ["ID", "INTLit", "FLOATLit", "CHARLit", "STRLit", "BoolTrue", "BoolFalse"]
        if(toktype[tokctr] in firstsetvalue):
            if(toktype[tokctr] == "ID"):
                tokctr+=1
                self.valuenext()
            else:
                self.literals()
        else:
            syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID, INTLit, FLOATLit, CHARLit, STRLit, TRUE, FALSE\'")
            return
    
    def valuenext(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "("):
            tokctr+=1
            self.functparam()
            if(tokvalue[tokctr] == ")"):
                tokctr+=1
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \')\'")
                return
        else:
            self.inputvar1()
    
    def statement(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        firstsetstatement = ["ID", "Struct", "Integer", "Float", "Character", "String", "Boolean", "INCREMENT", "DECREMENT", "Ifstatement", "LoopFor", "LoopWhile", "Switchstatement", "Output", "Input", "Return"]
        if(toktype[tokctr] in firstsetstatement):
            self.progstatement()
            self.statement()
        else:
            return
    
    def progstatement(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        firstsetprogstatement = ["ID", "Struct", "Integer", "Float", "Character", "String", "Boolean", "INCREMENT", "DECREMENT",
                             "Ifstatement", "LoopFor", "LoopWhile", "Switchstatement", "Output", "Input", "Return"]
        datatypeset = ['INT', 'FLOAT', 'STR', 'CHAR', 'BOOLEAN']
        if(toktype[tokctr] == "ID"):
            tokctr+=1
            if(tokvalue[tokctr] == "("):
                self.paramcall()
                if(tokvalue[tokctr] == "|"):
                    tokctr+=1
                else:
                    syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'|\'")
                    return
            else:
                tokctr-=1
                self.inputvar()
                self.idprod()
                if (tokvalue[tokctr] == "|"):
                    tokctr += 1
                else:
                    syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'|\'")
                    return
    
        elif(tokvalue[tokctr] in datatypeset):
            self.datatype()
            if(toktype[tokctr] == "ID"):
                tokctr+=1
                self.bodychoices()
                if(tokvalue[tokctr] == "|"):
                    tokctr+=1
                else:
                    syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'|\'")
                    return
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID\'")
                return
    
        elif(tokvalue[tokctr] == "++" or tokvalue[tokctr] == "--"):
            tokctr+=1
            self.inputvar()
            if (tokvalue[tokctr] == "|"):
                tokctr += 1
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'|\'")
                return
    
        elif(tokvalue[tokctr] == "PRINT" or tokvalue[tokctr] == "INPUT"):
            self.iostatement()
    
        elif(tokvalue[tokctr] == "IF"):
            self.ifstatement()
    
        elif(tokvalue[tokctr] == "QUIVER"):
            self.switch()
    
        elif(tokvalue[tokctr] == "FOR" or tokvalue[tokctr] == "WHILE"):
            self.looping()
    
        elif(tokvalue[tokctr] == "RETURN"):
            self.returns()
    
        elif(tokvalue[tokctr] == "DOJO"):
            tokctr+=1
            if(toktype[tokctr] == "ID"):
                tokctr+=1
                if(toktype[tokctr] == "ID"):
                    tokctr+=1
                    self.structfuncarray()
                    if(tokvalue[tokctr] == "|"):
                        tokctr+=1
                    else:
                        syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'|\'")
                        return
                else:
                    syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID\'")
                    return
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID\'")
                return
    
    def bodychoices(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "=" or tokvalue[tokctr] == ","):
            self.vardec()
        elif(tokvalue[tokctr] == "["):
            self.array()
        else:
            return
    
    def iostatement(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "PRINT"):
            tokctr+=1
            if(tokvalue[tokctr] == "("):
                tokctr+=1
                self.output()
                if(tokvalue[tokctr] == ")"):
                    tokctr+=1
                    if(tokvalue[tokctr] == "|"):
                        tokctr+=1
                    else:
                        syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token '|'")
                        return
                else:
                    syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token ')'")
                    return
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token '('")
                return
        elif(tokvalue[tokctr] == "INPUT"):
            tokctr+=1
            if (tokvalue[tokctr] == "("):
                tokctr+=1
                self.inputvar()
                
                if (tokvalue[tokctr] == ")"):
                    tokctr += 1
                    if (tokvalue[tokctr] == "|"):
                        tokctr += 1
                    else:
                        syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token '|'")
                        return
                else:
                    syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token ')'")
                    return
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token '('")
                return
    
    def output(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        firstsetoutput = ["ID", "INTLit", "FLOATLit", "CHARLit", "STRLit", "BoolTrue", "BoolFalse"]
        if(toktype[tokctr] not in firstsetoutput):
            syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID, STRLit, INTLit, FLOATLit, CHARLit, True, False\'")
            return
        else:
            if(toktype[tokctr] == "STRLit" or toktype[tokctr] == "CHARLit" or toktype[tokctr] == "BoolTrue" or toktype[tokctr] == "BoolFalse"):
                tokctr+=1
                self.outputnext()
            else:
                self.digitmathop()
                self.outputnext()
    
    def outputnext(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == ","):
            tokctr+=1
            self.output()
        else:
            return
    
    def inputvar(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(toktype[tokctr] == "ID"):
            tokctr+=1
            self.inputvar1()
        else:
            syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID\'")
            return
    
    def inputvar1(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "["):
            tokctr+=1
            self.funcarrayvalue()
            if(tokvalue[tokctr] == "]"):
                tokctr+=1
                self.funcarraynext()
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \']\'")
                return
        else:
            self.structaccess()
    
    def funcarrayvalue(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(toktype[tokctr] == "ID"):
            self.inputvar()
            self.digitid()
        elif(toktype[tokctr] == "INTLit"):
            tokctr+=1
            self.digitid()
        else:
            syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID, INTLit\'")
    
    def funcarraynext(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if (tokvalue[tokctr] == "["):
            tokctr += 1
            self.funcarrayvalue()
            if (tokvalue[tokctr] == "]"):
                tokctr += 1
                self.structaccess()
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \']\'")
                return
        else:
            self.structaccess()
    
    def idprod(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "++" or tokvalue[tokctr] == "--"):
            tokctr+=1
        elif(tokvalue[tokctr] == "+=" or tokvalue[tokctr] == "-=" or tokvalue[tokctr] == "*=" or tokvalue[tokctr] == "/=" or tokvalue[tokctr] == "%=" or tokvalue[tokctr] == "="):
            self.assignop()
        else:
            syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'=, +=, -=, *=, /=, %=, ++, --\'")
            return
    
    def paramcall(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "("):
            tokctr+=1
            self.functparam()
            if(tokvalue[tokctr] == ")"):
                tokctr+=1
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[
                    tokctr] + ", Expected token \')\'")
                return
    
    def assignopvalues(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(toktype[tokctr] == "STRLit" or toktype[tokctr] == "CHARLit" or toktype[tokctr] == "BoolTrue" or toktype[tokctr] == "BoolFalse"):
            tokctr+=1
        elif(toktype[tokctr] == "ID" or tokvalue[tokctr] == "(" or toktype[tokctr] == "INTLit" or toktype[tokctr] == "FLOATLit"):
            self.digitmathop()
        else:
            syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[
                tokctr] + ", Expected token \'ID, (, Literals\'")
            return
    
    def ifstatement(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "IF"):
            tokctr+=1
            if(tokvalue[tokctr] == "("):
                tokctr+=1
                self.condition()
                if(tokvalue[tokctr] == ")"):
                    tokctr+=1
                    if(tokvalue[tokctr] == "{"):
                        tokctr+=1
                        self.states()
                        if(tokvalue[tokctr] == "}"):
                            tokctr+=1
                            self.elseifstatement()
                            self.elsestatement()
                        else:
                            syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[
                                tokctr] + ", Expected token \'}\'")
                            return
                    else:
                        syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[
                            tokctr] + ", Expected token \'{\'")
                        return
                else:
                    syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[
                        tokctr] + ", Expected token \')\'")
                    return
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[
                    tokctr] + ", Expected token \'(\'")
                return
    
    def condition(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        firstsetcondition = ["NOT", "LPAREN", "ID", "NULL", "INTLit", "FLOATLit", "STRLit", "CHARLit", "BoolTrue", "BoolFalse"]
        if(toktype[tokctr] in firstsetcondition):
            if(tokvalue[tokctr] == "!"):
                self.nut()
                self.condition()
            elif(tokvalue[tokctr] == "("):
                tokctr+=1
                self.conditional()
                if(tokvalue[tokctr] == ")"):
                    tokctr+=1
                    self.conditionalnext()
                    self.logicalopend()
                else:
                    syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[
                        tokctr] + ", Expected token \')\'")
                    return
            else:
                self.conditional()
                self.condition2()
        else:
            syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[
                tokctr] + ", Expected token \'!, (, ID, NULL, INTLit, FLOATLit, CHARLit, STRLit, TRUE, FALSE\'")
            return

    def condition2(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "("):
            tokctr+=1
            self.logicalopend()
            if(tokvalue[tokctr] == ")"):
                tokctr+=1
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[
                    tokctr] + ", 2Expected token \')\'")
                return
        else:
            self.logicalopend()
    
    def conditional(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        comparesfirstset=["INTLit", "FLOATLit", "ID"]
        newfirstset=["CHARLit", "STRLit"]
        if(tokvalue[tokctr] == "!"):
            self.nut()
            self.conditional()
        elif(tokvalue[tokctr] == "("):
            tokctr+=1
            self.compares()
            if(tokvalue[tokctr] == ")"):
                tokctr+=1
                self.conditionalnext()
            else:
                syntaxerror.append("Syntax Error! Unexpected token " + tokvalue[
                    tokctr] + ", 3Expected token \')\'")
                return
        else:
            if(toktype[tokctr] in comparesfirstset):
                self.compares()
                self.conditionalnext()
            else:
                self.comparesnew()
                print("conditionalnext2")
                self.conditionalnext2()
    
    def conditionalnext(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        firstsetconditionalnext = ["==", "!=", "<", ">", "<=", ">="]
        if(tokvalue[tokctr] in firstsetconditionalnext):
            self.relationalop()
            self.comp()
        else:
            return

    def conditionalnext2(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        firstsetconditionalnext = ["==", "!=", "<", ">", "<=", ">="]

        if (tokvalue[tokctr] in firstsetconditionalnext):
            self.relationalop()
            self.comp3()
        else:
            if(tokvalue[tokctr-2] in firstsetconditionalnext):
                return
            else:
                syntaxerror.append(
                    "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'==, !=, <, >, <=, >=\'")
                return

    def comp(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "!"):
            self.nut()
            self.comp2()
        elif(tokvalue[tokctr] == "("):
            tokctr+=1
            if (tokvalue[tokctr] == "!"):
                self.nut()
                self.conditional()
                if(tokvalue[tokctr] == ")"):
                    tokctr+=1
                else:
                    syntaxerror.append(
                        "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \')\'")
                    return
            else:
                self.conditional()
                if(tokvalue[tokctr] == ")"):
                    tokctr+=1
                else:
                    syntaxerror.append(
                        "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \')\'")
                    return
        else:
            self.comp2()
    
    def comp2(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "("):
            tokctr+=1
            if(tokvalue[tokctr] == "!"):
                self.nut()
                self.conditional()
                if (tokvalue[tokctr] == ")"):
                    tokctr += 1
                else:
                    syntaxerror.append(
                        "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \')\'")
                    return
            else:
                self.conditional()
                if (tokvalue[tokctr] == ")"):
                    tokctr += 1
                else:
                    syntaxerror.append(
                        "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \')\'")
                    return
        else:
            self.conditional()

    def comp3(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if (tokvalue[tokctr] == "!"):
            self.nut()
            self.comp4()
        elif (tokvalue[tokctr] == "("):
            tokctr += 1
            if (tokvalue[tokctr] == "!"):
                self.nut()
                self.conditional()
                if (tokvalue[tokctr] == ")"):
                    tokctr += 1
                else:
                    syntaxerror.append(
                        "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \')\'")
                    return
            else:
                self.compares()
                if (tokvalue[tokctr] == ")"):
                    tokctr += 1
                else:
                    syntaxerror.append(
                        "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \')\'")
                    return
        else:
            self.comp4()

    def comp4(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if (tokvalue[tokctr] == "("):
            tokctr += 1
            if (tokvalue[tokctr] == "!"):
                self.nut()
                self.conditional()
                if (tokvalue[tokctr] == ")"):
                    tokctr += 1
                else:
                    syntaxerror.append(
                        "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \')\'")
                    return
            else:
                self.conditional()
                if (tokvalue[tokctr] == ")"):
                    tokctr += 1
                else:
                    syntaxerror.append(
                        "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \')\'")
                    return
        else:
            self.conditional()
    
    def compares(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        firstsetcompares = ["LPAREN", "ID", "INTLit", "FLOATLit", "Null"]
        if(toktype[tokctr] not in firstsetcompares):
            syntaxerror.append(
                "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID, (, INTLit, FLOATLit\'")
            return
        else:
            if(toktype[tokctr] == "LPAREN"):
                tokctr+=1
                self.compares2()
            elif(toktype[tokctr] == "ID"):
                tokctr+=1
                self.idcompares()
                self.comparesnext()
            elif(toktype[tokctr] == "Null"):
                tokctr+=1
            elif(toktype[tokctr] == "INTLit" or toktype[tokctr] == "FLOATLit"):
                tokctr+=1
                self.comparesnext()

    def comparesnew(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        firstsetcomparesnew = ["BoolTrue", "BoolFalse", "CHARLit", "STRLit"]
        if(toktype[tokctr] in firstsetcomparesnew):
            tokctr+=1
        else:
            syntaxerror.append(
                "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'CHARLit, STRLit, TRUE, FALSE\'")
            return
    
    def compares2(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        firstsetcompares2 = ["ID", "INTLit", "FLOATLit"]
        if (toktype[tokctr] not in firstsetcompares2):
            syntaxerror.append(
                "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID, (, INTLit, FLOATLit\'")
            return
        else:
            if (toktype[tokctr] == "ID"):
                tokctr += 1
                self.idcompares()
                if(tokvalue[tokctr] == ")"):
                    tokctr+=1
                    self.comparesnext()
                else:
                    syntaxerror.append(
                        "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \')\'")
                    return
            else:
                if(toktype[tokctr] == "INTLit" or toktype[tokctr] == "FLOATLit"):
                    tokctr+=1
                    if (tokvalue[tokctr] == ")"):
                        tokctr += 1
                        self.comparesnext()
                    else:
                        syntaxerror.append(
                            "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \')\'")
                        return
    
    def comparesnext(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        self.digitid()
    
    def idcompares(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "["):
            tokctr+=1
            self.funcarrayvalue()
            if(tokvalue[tokctr] == "]"):
                tokctr+=1
                self.funcarraynext()
            else:
                syntaxerror.append(
                    "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \']\'")
                return
        elif(tokvalue[tokctr] == "("):
            tokctr+=1
            self.functparam()
            if(tokvalue[tokctr] == ")"):
                tokctr+=1
            else:
                syntaxerror.append(
                    "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \')\'")
                return
        else:
            self.structaccess()
    
    def relationalop(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        relationalopset = ["==", "!=", ">", "<", "<=" ,">="]
        if(tokvalue[tokctr] in relationalopset):
            tokctr+=1
        else:
            syntaxerror.append(
                "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'==, !=, >, <, <= ,>=\'")
            return
    
    def logicalopend(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        logicalopendset = ["AND", "OR"]
        if(tokvalue[tokctr] in logicalopendset):
            self.logop()
            self.logopmore()
            self.logicalopend()
        else:
            return
    
    def nut(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if (tokvalue[tokctr] == "!"):
            tokctr+=1
            self.nut()
        else:
            return
    
    def logop(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        logopset = ["AND", "OR"]
        if (tokvalue[tokctr] in logopset):
            tokctr+=1
        else:
            syntaxerror.append(
                "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'AND, OR\'")
            return
    
    def logopmore(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "!"):
            tokctr+=1
            if(tokvalue[tokctr] == "("):
                tokctr+=1
                self.condition()
                if(tokvalue[tokctr] == ")"):
                    tokctr+=1
                else:
                    syntaxerror.append(
                        "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \')\'")
                    return
            else:
                self.condition()

        elif(tokvalue[tokctr] == "("):
            tokctr+=1
            self.condition()
            if(tokvalue[tokctr] == ")"):
                tokctr+=1
            else:
                syntaxerror.append(
                    "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \')\'")
                return
        else:
            self.condition()
    
    def states(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        firstsetstates = ["ID", "Struct", "Integer", "Float", "Character", "String", "Boolean", "INCREMENT", "DECREMENT",
                                 "Ifstatement", "LoopFor", "LoopWhile", "Switchstatement", "Output", "Input", "Return"]
        if(tokvalue[tokctr] == "BREAK" or tokvalue[tokctr] == "CONTINUE"):
            tokctr+=1
            if(tokvalue[tokctr] == "|"):
                tokctr+=1
                self.states()
            else:
                syntaxerror.append(
                    "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'|\'")
                return
        elif(toktype[tokctr] in firstsetstates):
            self.progstatement()
            if (tokvalue[tokctr] == "BREAK" or tokvalue[tokctr] == "CONTINUE"):
                tokctr += 1
                if (tokvalue[tokctr] == "|"):
                    tokctr += 1
                    self.states()
                else:
                    syntaxerror.append(
                        "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'|\'")
                    return
            else:
                self.states()
                return
        else:
            return
    
    def elseifstatement(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "ELSEIF"):
            tokctr+=1
            if(tokvalue[tokctr] == "("):
                tokctr+=1
                self.condition()
                if(tokvalue[tokctr] == ")"):
                    tokctr+=1
                    if(tokvalue[tokctr] == "{"):
                        tokctr+=1
                        self.states()
                        if(tokvalue[tokctr] == "}"):
                            tokctr+=1
                            self.elseifstatement()
                        else:
                            syntaxerror.append(
                                "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'}\'")
                            return
                    else:
                        syntaxerror.append(
                            "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'{\'")
                        return
                else:
                    syntaxerror.append(
                        "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \')\'")
                    return
            else:
                syntaxerror.append(
                    "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'(\'")
                return
        else:
            return
    
    def elsestatement(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "ELSE"):
            tokctr+=1
            if (tokvalue[tokctr] == "{"):
                tokctr += 1
                self.states()
                if (tokvalue[tokctr] == "}"):
                    tokctr += 1
                else:
                    syntaxerror.append(
                        "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'}\'")
                    return
            else:
                syntaxerror.append(
                    "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'{\'")
                return
        else:
            return
    
    def switch(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "QUIVER"):
            tokctr+=1
            if(tokvalue[tokctr] == "("):
                tokctr+=1
                if(toktype[tokctr] == "ID"):
                    tokctr+=1
                    if(tokvalue[tokctr] == ")"):
                        tokctr+=1
                        if(tokvalue[tokctr] == "{"):
                            tokctr+=1
                            self.case()
                            self.default()
                            if(tokvalue[tokctr] == "}"):
                                tokctr+=1
                            else:
                                syntaxerror.append(
                                    "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'}\'")
                                return
                        else:
                            syntaxerror.append(
                                "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'{\'")
                            return
                    else:
                        syntaxerror.append(
                            "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \')\'")
                        return
                else:
                    syntaxerror.append(
                        "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID\'")
                    return
            else:
                syntaxerror.append(
                    "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'(\'")
                return
    
    def case(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "ARROW"):
            tokctr+=1
            if(toktype[tokctr] == "INTLit" or toktype[tokctr] == "CHARLit"):
                tokctr+=1
                if(tokvalue[tokctr] == ":"):
                    tokctr+=1
                    self.statement()
                    self.swtchcontrol()
                    self.case()
                else:
                    syntaxerror.append(
                        "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \':\'")
                    return
            else:
                syntaxerror.append(
                    "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'INTLit, CHARLit\'")
                return
        else:
            return
    
    def swtchcontrol(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(tokvalue[tokctr] == "BREAK"):
            tokctr+=1
            if(tokvalue[tokctr] == "|"):
                tokctr+=1
            else:
                syntaxerror.append(
                    "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'|\'")
                return
        else:
            return
    
    def default(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if (tokvalue[tokctr] == "DEFAULT"):
            tokctr+=1
            if(tokvalue[tokctr] == ":"):
                tokctr+=1
                self.statement()
                self.swtchcontrol()
            else:
                syntaxerror.append(
                    "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \':\'")
                return
        else:
            return
    
    def looping(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if (tokvalue[tokctr] == "FOR"):
            tokctr+=1
            if (tokvalue[tokctr] == "("):
                tokctr+=1
                self.initialize()
                if (tokvalue[tokctr] == "|"):
                    tokctr+=1
                    self.forcondition()
                    if (tokvalue[tokctr] == "|"):
                        tokctr+=1
                        self.forcontrol()
                        if (tokvalue[tokctr] == ")"):
                            tokctr+=1
                            if (tokvalue[tokctr] == "{"):
                                tokctr+=1
                                self.states()
                                if (tokvalue[tokctr] == "}"):
                                    tokctr+=1
                                else:
                                    syntaxerror.append(
                                        "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'}\'")
                                    return
                            else:
                                syntaxerror.append(
                                    "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'{\'")
                                return
                        else:
                            syntaxerror.append(
                                "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \')\'")
                            return
                    else:
                        syntaxerror.append(
                            "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'|\'")
                        return
                else:
                    syntaxerror.append(
                        "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'|\'")
                    return
            else:
                syntaxerror.append(
                    "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'(\'")
                return
        elif(tokvalue[tokctr] == "WHILE"):
            tokctr+=1
            if (tokvalue[tokctr] == "("):
                tokctr+=1
                self.condition()
                if (tokvalue[tokctr] == ")"):
                    tokctr+=1
                    if (tokvalue[tokctr] == "{"):
                        tokctr+=1
                        self.states()
                        if (tokvalue[tokctr] == "}"):
                            tokctr+=1
                        else:
                            syntaxerror.append(
                                "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'}\'")
                            return
                    else:
                        syntaxerror.append(
                            "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'{\'")
                        return
                else:
                    syntaxerror.append(
                        "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \')\'")
                    return
            else:
                syntaxerror.append(
                    "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'(\'")
                return
    
    def initialize(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if (tokvalue[tokctr] == "INT"):
            tokctr+=1
            if(toktype[tokctr] == "ID"):
                tokctr+=1
                if(tokvalue[tokctr] == "="):
                    tokctr+=1
                    self.forinit()
                else:
                    syntaxerror.append(
                        "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'=\'")
                    return
            else:
                syntaxerror.append(
                    "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID\'")
                return
        elif(tokvalue[tokctr] == "FLOAT"):
            tokctr+=1
            if (toktype[tokctr] == "ID"):
                tokctr += 1
                if (tokvalue[tokctr] == "="):
                    tokctr += 1
                    self.forinit()
                else:
                    syntaxerror.append(
                        "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'=\'")
                    return
            else:
                syntaxerror.append(
                    "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID\'")
                return
        elif(toktype[tokctr] == "ID"):
            tokctr+=1
            if(tokvalue[tokctr] == "="):
                tokctr+=1
                self.forinit()
            else:
                syntaxerror.append(
                    "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'=\'")
                return
        else:
            return
    
    def forinit(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(toktype[tokctr] == "INTLit" or toktype[tokctr] == "FLOATLit"):
            tokctr+=1
            self.operation()
        elif(toktype[tokctr] == "ID"):
            self.inputvar()
            self.operation()
        else:
            syntaxerror.append(
                "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID, INTLit, FLOATLit\'")
            return
    def forcontrol(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if (toktype[tokctr] == "INCREMENT" or toktype[tokctr] == "DECREMENT"):
            tokctr+=1
            self.inputvar()
        elif(toktype[tokctr] == "ID"):
            self.inputvar()
            self.idprod()
        else:
            return
    
    def forcondition(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        firstsetforcondition = ["NOT", "LPAREN", "ID", "INTLit", "FLOATLit", "CHARLit", "STRLit", "BoolTrue", "BoolFalse"]
        if(toktype[tokctr] in firstsetforcondition):
            self.condition()
        else:
            return
    
    def digit(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if(toktype[tokctr] == "INTLit" or toktype[tokctr] == "FLOATLit"):
            tokctr+=1
        elif(toktype[tokctr] == "ID"):
            tokctr+=1
            self.idcompares()
        else:
            syntaxerror.append(
                "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID, INTLit, FLOATLit\'")
            return
    
    def digitcomp(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if (toktype[tokctr] == "INTLit" or toktype[tokctr] == "FLOATLit"):
            tokctr += 1
        else:
            syntaxerror.append(
                "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'INTLit, FLOATLit\'")
            return
    
    def digitnext(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        mathopdata = ["+", "-", "/", "*", "%"]
        if (tokvalue[tokctr] in mathopdata):
            self.mathoperation()
            self.digitmathop()
        else:
            return
    
    def digitoperation(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        digitoperationdata = ["INTLit", "FLOATLit", "ID"]
        if (toktype[tokctr] in digitoperationdata):
            self.digit()
            self.mathoperation()
            self.digit()
            self.digitnext()
    
        elif(tokvalue[tokctr] == "("):
            tokctr+=1
            self.digitoperation()
            if (tokvalue[tokctr] == ")"):
                tokctr+=1
                self.digitnext()
            else:
                syntaxerror.append(
                    "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \')\'")
                return
        else:
            syntaxerror.append(
                "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID, INTLit, FLOATLit\'")
            return
    
    def digitmathop(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        digitmathopdata = ["INTLit", "FLOATLit", "ID"]
        if (toktype[tokctr] in digitmathopdata):
            self.digit()
            self.digitnext()
        elif (tokvalue[tokctr] == "("):
            tokctr += 1
            self.digitit()
            self.digitnext()
            if (tokvalue[tokctr] == ")"):
                tokctr += 1
                self.digitnext()
            else:
                syntaxerror.append(
                    "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \')\'")
                return
        else:
            syntaxerror.append(
                "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID, INTLit, FLOATLit\'")
            return
    
    def digitit(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        digitmathopdata = ["INTLit", "FLOATLit", "ID"]
        if (toktype[tokctr] in digitmathopdata):
            self.digit()
            self.digitnext()
        elif (tokvalue[tokctr] == "("):
            tokctr += 1
            self.digit()
            self.digitnext()
            if (tokvalue[tokctr] == ")"):
                tokctr += 1
            else:
                syntaxerror.append(
                    "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \')\'")
                return
        else:
            syntaxerror.append(
                "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'ID, INTLit, FLOATLit\'")
            return
    
    def digitid(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        mathopdata = ["+", "-", "/", "*", "%"]
        if(tokvalue[tokctr] in mathopdata):
            self.mathoperation()
            self.digitmathop()
        else:
            return
    
    def operation(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        mathopdata = ["+", "-", "/", "*", "%"]
        if (tokvalue[tokctr] in mathopdata):
            self.mathoperation()
            self.arraysize()
            self.operation()
        else:
            return
    
    def mathoperation(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        mathopdata = ["+", "-", "/", "*", "%"]
        if (tokvalue[tokctr] in mathopdata):
            tokctr+=1
        else:
            syntaxerror.append(
                "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'+, -, *, /, %\'")
            return
    
    def assignop(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        if (tokvalue[tokctr] == "="):
            tokctr += 1
            self.assignopvalues()
        elif (tokvalue[tokctr] == "+=" or tokvalue[tokctr] == "-=" or tokvalue[tokctr] == "*=" or tokvalue[
            tokctr] == "/=" or tokvalue[tokctr] == "%="):
            tokctr+=1
            self.digitmathop()
        else:
            syntaxerror.append(
                "Syntax Error! Unexpected token " + tokvalue[tokctr] + ", Expected token \'=, +=, -=, *=, /=, %=\'")
            return
    
    def datatype(self):
        global toktype
        global tokvalue
        global tokctr
        global syntaxerror
        datatypeset = ['INT', 'FLOAT', 'STR', 'CHAR', 'BOOLEAN']
        if(tokvalue[tokctr] in datatypeset):
            tokctr+=1
        else:
            syntaxerror.append("Syntax Error! Unexpected token "+ tokvalue[tokctr] + ", Expected token \'INT, FLOAT, STR, CHAR, BOOLEAN\'")
    
    
    def semantic(self):
        global toktype
        global tokvalue
        global VOID
        global INT
        global FLOAT
        global CHAR
        global STR
        global BOOLEAN
        global dictionary
        global semanticerrors
        
        
        VOID=[]
        INT=[]
        FLOAT=[]
        CHAR=[]
        STR=[]
        BOOLEAN=[]
        dictionary={}
        semanticerrors=[]
        
        ctr = 0
        innerctr = 0
        i=0
        datatype=['INT','FLOAT','CHAR','STR','BOOLEAN']
        mathop=['+','-','/','*','%','(',')','[',']']
        mathop2 = ['+','-','/','*','%']
        arrmathop=['+','-','/','*','%','(',')','{','}',',','[',']']
        charmathop=['{','}',',','[',']','(',')']
        assignop=['=','+=','-=','*=','/=','%=']
        charassignop=['+=','-=','*=','/=','%=']
        param=[]
        functionvar=''
        lits = ['INTLit', 'FLOATLit','CHARLit','STRLit']

        while(i < len(toktype)):
            ctr = 0
            innerctr = 0
            if(tokvalue[i] == 'VOID'):
                ctr = i+1
                if(tokvalue[ctr+1] == '('):
                    if(tokvalue[ctr] in INT or tokvalue[ctr] in FLOAT or tokvalue[ctr] in CHAR or tokvalue[ctr] in STR or tokvalue[ctr] in BOOLEAN or tokvalue[ctr] in VOID):
                        semanticerrors.append("Semantic Error: "+tokvalue[ctr]+" has already been declared")
                        ctr+=1
                        while(tokvalue[ctr] != ')'):
                            ctr+=1
                    else:
                        functionvar = tokvalue[ctr]
                        VOID.append(tokvalue[ctr])
                        ctr+=1
                        while(tokvalue[ctr] != ')'):
                            if(tokvalue[ctr] in datatype):
                                param.append(tokvalue[ctr])
                                if(tokvalue[ctr+1] in INT or tokvalue[ctr+1] in FLOAT or tokvalue[ctr+1] in CHAR or tokvalue[ctr+1] in STR or tokvalue[ctr+1] in BOOLEAN or tokvalue[ctr+1] in VOID):
                                    semanticerrors.append("Semantic Error: "+tokvalue[ctr]+" has already been declared")
                                else:
                                    if(tokvalue[ctr] == 'INT'):
                                        INT.append(tokvalue[ctr+1])
                                        
                                    if(tokvalue[ctr] == 'FLOAT'):
                                        FLOAT.append(tokvalue[ctr+1])
                                    
                                    if(tokvalue[ctr] == 'CHAR'):
                                        CHAR.append(tokvalue[ctr+1])
                                    
                                    if(tokvalue[ctr] == 'STR'):
                                        STR.append(tokvalue[ctr+1])
                                    
                                    if(tokvalue[ctr] == 'BOOLEAN'):
                                        BOOLEAN.append(tokvalue[ctr+1])
                            ctr+=1
                        if(param):
                            dictionary[functionvar] = param
                        else:
                            dictionary[functionvar] = ['none']
                        param=[]
                        functionvar=''
                i=ctr
            elif(tokvalue[i] in datatype):
                if (tokvalue[i] == 'INT'):
                    ctr = i+1
                    if(tokvalue[ctr+1] == '('):
                        if(tokvalue[ctr] in INT or tokvalue[ctr] in FLOAT or tokvalue[ctr] in CHAR or tokvalue[ctr] in STR or tokvalue[ctr] in BOOLEAN or tokvalue[ctr] in VOID ):
                            semanticerrors.append("Semantic Error: "+tokvalue[ctr]+" has already been declared")
                            ctr+=1
                            while(tokvalue[ctr] != ')'):
                                ctr+=1
                        else:
                            functionvar = tokvalue[ctr]
                            INT.append(tokvalue[ctr])
                            ctr+=1
                            while(tokvalue[ctr] != ')'):
                                if(tokvalue[ctr] in datatype):
                                    param.append(tokvalue[ctr])
                                    if(tokvalue[ctr+1] in INT or tokvalue[ctr+1] in FLOAT or tokvalue[ctr+1] in CHAR or tokvalue[ctr+1] in STR or tokvalue[ctr+1] in BOOLEAN or tokvalue[ctr+1] in VOID):
                                        semanticerrors.append("Semantic Error: "+tokvalue[ctr]+" has already been declared")
                                    else:
                                        if(tokvalue[ctr] == 'INT'):
                                            INT.append(tokvalue[ctr+1])
                                            
                                        if(tokvalue[ctr] == 'FLOAT'):
                                            FLOAT.append(tokvalue[ctr+1])
                                        
                                        if(tokvalue[ctr] == 'CHAR'):
                                            CHAR.append(tokvalue[ctr+1])
                                        
                                        if(tokvalue[ctr] == 'STR'):
                                            STR.append(tokvalue[ctr+1])
                                        
                                        if(tokvalue[ctr] == 'BOOLEAN'):
                                            BOOLEAN.append(tokvalue[ctr+1])
                                ctr+=1
                            if(param):
                                dictionary[functionvar] = param
                            else:
                                dictionary[functionvar] = ['none']
                            param=[]
                            functionvar=''
                    else:
                        
                        while (tokvalue[ctr] != '|'):
                            #a[
                            if (tokvalue[ctr + 1] == '['):
                                if(tokvalue[ctr] in INT or tokvalue[ctr] in FLOAT or tokvalue[ctr] in CHAR or tokvalue[ctr] in STR or tokvalue[ctr] in BOOLEAN  or tokvalue[ctr] in VOID):
                                    semanticerrors.append("Semantic Error: Variable "+tokvalue[ctr]+" has already been declared")
                                    ctr+=1
                                else:
                                    INT.append(tokvalue[ctr])
                                    ctr+=1
                                while (tokvalue[ctr] != ']'):
                                    ctr += 1
                                #] = {
                                if (tokvalue[ctr + 1] == '='):
                                    ctr += 2
                                    innerctr = ctr
                                    while (tokvalue[innerctr] != '|' and not (
                                            tokvalue[innerctr] == '}' and tokvalue[innerctr + 1] == ',' and toktype[innerctr + 2] == 'ID')):
                                        if (toktype[innerctr] == 'FLOATLit' or toktype[innerctr] == 'INTLit' or tokvalue[innerctr] in FLOAT or tokvalue[innerctr] in INT or tokvalue[innerctr] in arrmathop):
                                            pass
                                        else:
                                            semanticerrors.append("Semantic Error: Value "+tokvalue[innerctr]+" is not an integer")
                                        innerctr += 1
                                    ctr = innerctr
                    
                                    if (tokvalue[ctr + 1] == ','):
                                        ctr += 2
                                
                                #][x] =
                                elif (tokvalue[ctr + 1] == '['):
                                    ctr += 1
                                    while (tokvalue[ctr] != ']'):
                                        ctr += 1
                                    if (tokvalue[ctr + 1] == '='):
                                        ctr += 2
                                        innerctr = ctr
                                        while (tokvalue[innerctr] != '|' and not (
                                                tokvalue[innerctr] == '}' and tokvalue[innerctr + 1] == ',' and toktype[innerctr + 2] == 'ID')):
                                            if (toktype[innerctr] == 'FLOATLit' or toktype[innerctr] == 'INTLit' or tokvalue[innerctr] in FLOAT or tokvalue[innerctr] in INT or tokvalue[innerctr] in arrmathop):
                                                pass
                                            else:
                                                semanticerrors.append("Semantic Error: Value "+tokvalue[innerctr]+" is not an integer")
                                            innerctr += 1
                                        ctr = innerctr
                    
                                        if (tokvalue[innerctr + 1] == ','):
                                            ctr += 2
                                            
                                elif(tokvalue[ctr+1] == ','):
                                    ctr+=2
                                elif(tokvalue[ctr+1] == '|'):
                                    ctr+=1
                                else:
                                    ctr+=1
                                    
                        
                    
                            #a =
                            elif(tokvalue[ctr + 1] == '='):
                                if(tokvalue[ctr] in INT or tokvalue[ctr] in FLOAT or tokvalue[ctr] in CHAR or tokvalue[ctr] in STR or tokvalue[ctr] in BOOLEAN  or tokvalue[ctr] in VOID):
                                    semanticerrors.append("Semantic Error: Variable "+tokvalue[ctr]+" has already been declared")
                                    ctr+=2
                                else:
                                    INT.append(tokvalue[ctr])
                                    ctr+=2
                                innerctr = ctr
                                while (tokvalue[innerctr] != ',' and tokvalue[innerctr] != '|'):
                                    if (toktype[innerctr] == 'FLOATLit' or toktype[innerctr] == 'INTLit' or tokvalue[innerctr] in FLOAT or tokvalue[innerctr] in INT or tokvalue[innerctr] in mathop):
                                        pass
                                    else:
                                        semanticerrors.append("Semantic Error: Value "+tokvalue[innerctr]+" is not an integer")
                                    innerctr += 1
                                ctr = innerctr
                                if (tokvalue[ctr] == ','):
                                    ctr+=1
                                    
                            elif(tokvalue[ctr+1] == ','):
                                if(tokvalue[ctr] in INT or tokvalue[ctr] in FLOAT or tokvalue[ctr] in CHAR or tokvalue[ctr] in STR or tokvalue[ctr] in BOOLEAN  or tokvalue[ctr] in VOID):
                                    semanticerrors.append("Semantic Error: Variable "+tokvalue[ctr]+" has already been declared")
                                    ctr+=2
                                else:
                                    INT.append(tokvalue[ctr])
                                    ctr+=2
                            elif(tokvalue[ctr+1] == '|'):
                                if(tokvalue[ctr] in INT or tokvalue[ctr] in FLOAT or tokvalue[ctr] in CHAR or tokvalue[ctr] in STR or tokvalue[ctr] in BOOLEAN  or tokvalue[ctr] in VOID):
                                    semanticerrors.append("Semantic Error: Variable "+tokvalue[ctr]+" has already been declared")
                                    ctr+=1
                                else:
                                    INT.append(tokvalue[ctr])
                                    ctr+=1
                                    
                            
                                    
                            else:
                                ctr+=1
                    
                            #ctr+=1
                    
                #########################################################        
                elif (tokvalue[i] == 'FLOAT'):
                    ctr = i+1
                    if(tokvalue[ctr+1] == '('):
                        if(tokvalue[ctr] in INT or tokvalue[ctr] in FLOAT or tokvalue[ctr] in CHAR or tokvalue[ctr] in STR or tokvalue[ctr] in BOOLEAN  or tokvalue[ctr] in VOID):
                            semanticerrors.append("Semantic Error: "+tokvalue[ctr]+" has already been declared")
                            ctr+=1
                            while(tokvalue[ctr] != ')'):
                                ctr+=1
                        else:
                            functionvar = tokvalue[ctr]
                            FLOAT.append(tokvalue[ctr])
                            ctr+=1
                            while(tokvalue[ctr] != ')'):
                                if(tokvalue[ctr] in datatype):
                                    param.append(tokvalue[ctr])
                                    if(tokvalue[ctr+1] in INT or tokvalue[ctr+1] in FLOAT or tokvalue[ctr+1] in CHAR or tokvalue[ctr+1] in STR or tokvalue[ctr+1] in BOOLEAN or tokvalue[ctr+1] in VOID):
                                        semanticerrors.append("Semantic Error: "+tokvalue[ctr]+" has already been declared")
                                    else:
                                        if(tokvalue[ctr] == 'INT'):
                                            INT.append(tokvalue[ctr+1])
                                            
                                        if(tokvalue[ctr] == 'FLOAT'):
                                            FLOAT.append(tokvalue[ctr+1])
                                        
                                        if(tokvalue[ctr] == 'CHAR'):
                                            CHAR.append(tokvalue[ctr+1])
                                        
                                        if(tokvalue[ctr] == 'STR'):
                                            STR.append(tokvalue[ctr+1])
                                        
                                        if(tokvalue[ctr] == 'BOOLEAN'):
                                            BOOLEAN.append(tokvalue[ctr+1])
                                ctr+=1
                            if(param):
                                dictionary[functionvar] = param
                            else:
                                dictionary[functionvar] = ['none']
                            param=[]
                            functionvar=''
                    else:
                        while (tokvalue[ctr] != '|'):
                            #a[
                            if (tokvalue[ctr + 1] == '['):
                                if(tokvalue[ctr] in INT or tokvalue[ctr] in FLOAT or tokvalue[ctr] in CHAR or tokvalue[ctr] in STR or tokvalue[ctr] in BOOLEAN  or tokvalue[ctr] in VOID):
                                    semanticerrors.append("Semantic Error: Variable "+tokvalue[ctr]+" has already been declared")
                                    ctr+=1
                                else:
                                    FLOAT.append(tokvalue[ctr])
                                    ctr+=1
                                while (tokvalue[ctr] != ']'):
                                    ctr += 1
                                #] = {
                                if (tokvalue[ctr + 1] == '='):
                                    ctr += 2
                                    innerctr = ctr
                                    while (tokvalue[innerctr] != '|' and not (
                                            tokvalue[innerctr] == '}' and tokvalue[innerctr + 1] == ',' and toktype[innerctr + 2] == 'ID')):
                                        if (toktype[innerctr] == 'FLOATLit' or toktype[innerctr] == 'INTLit' or tokvalue[innerctr] in FLOAT or tokvalue[innerctr] in INT or tokvalue[innerctr] in arrmathop):
                                            pass
                                        else:
                                            semanticerrors.append("Semantic Error: Value "+tokvalue[innerctr]+" is not a float")
                                        innerctr += 1
                                    ctr = innerctr
                    
                                    if (tokvalue[ctr + 1] == ','):
                                        ctr += 2
                    
                                #][x] =
                                elif (tokvalue[ctr + 1] == '['):
                                    ctr += 1
                                    while (tokvalue[ctr] != ']'):
                                        ctr += 1
                                    if (tokvalue[ctr + 1] == '='):
                                        ctr += 2
                                        innerctr = ctr
                                        while (tokvalue[innerctr] != '|' and not (
                                                tokvalue[innerctr] == '}' and tokvalue[innerctr + 1] == ',' and toktype[innerctr + 2] == 'ID')):
                                            if (toktype[innerctr] == 'FLOATLit' or toktype[innerctr] == 'INTLit' or tokvalue[innerctr] in FLOAT or tokvalue[innerctr] in INT or tokvalue[innerctr] in arrmathop):
                                                pass
                                            else:
                                                semanticerrors.append("Semantic Error: Value "+tokvalue[innerctr]+" is not a float")
                                            innerctr += 1
                                        ctr = innerctr
                    
                                        if (tokvalue[innerctr + 1] == ','):
                                            ctr += 2
                                elif(tokvalue[ctr+1] == ','):
                                    ctr+=2
                                elif(tokvalue[ctr+1] == '|'):
                                    ctr+=1
                                    
                    
                            #a =
                            elif(tokvalue[ctr + 1] == '='):
                                if(tokvalue[ctr] in INT or tokvalue[ctr] in FLOAT or tokvalue[ctr] in CHAR or tokvalue[ctr] in STR or tokvalue[ctr] in BOOLEAN  or tokvalue[ctr] in VOID):
                                    semanticerrors.append("Semantic Error: Variable "+tokvalue[ctr]+" has already been declared")
                                    ctr+=2
                                else:
                                    FLOAT.append(tokvalue[ctr])
                                    ctr+=2
                                innerctr=ctr
                                while (tokvalue[innerctr] != ',' and tokvalue[innerctr] != '|'):
                                    if (toktype[innerctr] == 'FLOATLit' or toktype[innerctr] == 'INTLit' or tokvalue[innerctr] in FLOAT or tokvalue[innerctr] in INT or tokvalue[innerctr] in mathop):
                                        pass
                                    else:
                                        semanticerrors.append("Semantic Error: Value "+tokvalue[innerctr]+" is not a float")
                                    innerctr += 1
                                ctr = innerctr
                                if (tokvalue[ctr] == ','):
                                    ctr+=1
                                    
                            elif(tokvalue[ctr+1] == ','):
                                if(tokvalue[ctr] in INT or tokvalue[ctr] in FLOAT or tokvalue[ctr] in CHAR or tokvalue[ctr] in STR or tokvalue[ctr] in BOOLEAN  or tokvalue[ctr] in VOID):
                                    semanticerrors.append("Semantic Error: Variable "+tokvalue[ctr]+" has already been declared")
                                    ctr+=2
                                else:
                                    FLOAT.append(tokvalue[ctr])
                                    ctr+=2
                            elif(tokvalue[ctr+1] == '|'):
                                if(tokvalue[ctr] in INT or tokvalue[ctr] in FLOAT or tokvalue[ctr] in CHAR or tokvalue[ctr] in STR or tokvalue[ctr] in BOOLEAN  or tokvalue[ctr] in VOID):
                                    semanticerrors.append("Semantic Error: Variable "+tokvalue[ctr]+" has already been declared")
                                    ctr+=1
                                else:
                                    FLOAT.append(tokvalue[ctr])
                                    ctr+=1
                            
                            else:
                                ctr+=1
                            
                  ############################################      
                elif (tokvalue[i] == 'CHAR'):
                    ctr = i+1
                    if(tokvalue[ctr+1] == '('):
                        if(tokvalue[ctr] in INT or tokvalue[ctr] in FLOAT or tokvalue[ctr] in CHAR or tokvalue[ctr] in STR or tokvalue[ctr] in BOOLEAN  or tokvalue[ctr] in VOID):
                            semanticerrors.append("Semantic Error: "+tokvalue[ctr]+" has already been declared")
                            ctr+=1
                            while(tokvalue[ctr] != ')'):
                                ctr+=1
                        else:
                            functionvar = tokvalue[ctr]
                            CHAR.append(tokvalue[ctr])
                            ctr+=1
                            while(tokvalue[ctr] != ')'):
                                if(tokvalue[ctr] in datatype):
                                    param.append(tokvalue[ctr])
                                    if(tokvalue[ctr+1] in INT or tokvalue[ctr+1] in FLOAT or tokvalue[ctr+1] in CHAR or tokvalue[ctr+1] in STR or tokvalue[ctr+1] in BOOLEAN or tokvalue[ctr+1] in VOID):
                                        semanticerrors.append("Semantic Error: "+tokvalue[ctr]+" has already been declared")
                                    else:
                                        if(tokvalue[ctr] == 'INT'):
                                            INT.append(tokvalue[ctr+1])
                                            
                                        if(tokvalue[ctr] == 'FLOAT'):
                                            FLOAT.append(tokvalue[ctr+1])
                                        
                                        if(tokvalue[ctr] == 'CHAR'):
                                            CHAR.append(tokvalue[ctr+1])
                                        
                                        if(tokvalue[ctr] == 'STR'):
                                            STR.append(tokvalue[ctr+1])
                                        
                                        if(tokvalue[ctr] == 'BOOLEAN'):
                                            BOOLEAN.append(tokvalue[ctr+1])
                                ctr+=1
                            if(param):
                                dictionary[functionvar] = param
                            else:
                                dictionary[functionvar] = ['none']
                            param=[]
                            functionvar=''
                    else:
                        while (tokvalue[ctr] != '|'):
                            #a[
                            if (tokvalue[ctr + 1] == '['):
                                if(tokvalue[ctr] in INT or tokvalue[ctr] in FLOAT or tokvalue[ctr] in CHAR or tokvalue[ctr] in STR or tokvalue[ctr] in BOOLEAN  or tokvalue[ctr] in VOID):
                                    semanticerrors.append("Semantic Error: Variable "+tokvalue[ctr]+" has already been declared")
                                    ctr+=1
                                else:
                                    CHAR.append(tokvalue[ctr])
                                    ctr+=1
                                while (tokvalue[ctr] != ']'):
                                    ctr += 1
                                #] = {
                                if (tokvalue[ctr + 1] == '='):
                                    ctr += 2
                                    innerctr = ctr
                                    while (tokvalue[innerctr] != '|' and not (
                                            tokvalue[innerctr] == '}' and tokvalue[innerctr + 1] == ',' and toktype[innerctr + 2] == 'ID')):
                                        if (toktype[innerctr] == 'CHARLit'  or tokvalue[innerctr] in CHAR or tokvalue[innerctr] in charmathop):
                                            pass
                                        else:
                                            semanticerrors.append("Semantic Error: Value "+tokvalue[innerctr]+" is not a character")
                                        innerctr += 1
                                    ctr = innerctr
                    
                                    if (tokvalue[ctr + 1] == ','):
                                        ctr += 2
                    
                                #][x] =
                                elif (tokvalue[ctr + 1] == '['):
                                    ctr += 1
                                    while (tokvalue[ctr] != ']'):
                                        ctr += 1
                                    if (tokvalue[ctr + 1] == '='):
                                        ctr += 2
                                        innerctr = ctr
                                        while (tokvalue[innerctr] != '|' and not (
                                                tokvalue[innerctr] == '}' and tokvalue[innerctr + 1] == ',' and toktype[
                                            innerctr + 2] == 'ID')):
                                            if (toktype[innerctr] == 'CHARLit'  or tokvalue[innerctr] in CHAR or tokvalue[innerctr] in charmathop):
                                                pass
                                            else:
                                                semanticerrors.append("Semantic Error: Value "+tokvalue[innerctr]+" is not a character")
                                            innerctr += 1
                                        ctr = innerctr
                    
                                        if (tokvalue[innerctr + 1] == ','):
                                            ctr += 2
                                elif(tokvalue[ctr+1] == ','):
                                    ctr+=2
                                elif(tokvalue[ctr+1] == '|'):
                                    ctr+=1
                    
                            #a =
                            elif(tokvalue[ctr + 1] == '='):
                                if(tokvalue[ctr] in INT or tokvalue[ctr] in FLOAT or tokvalue[ctr] in CHAR or tokvalue[ctr] in STR or tokvalue[ctr] in BOOLEAN  or tokvalue[ctr] in VOID):
                                    semanticerrors.append("Semantic Error: Variable "+tokvalue[ctr]+" has already been declared")
                                    ctr+=2
                                else:
                                    CHAR.append(tokvalue[ctr])
                                    ctr+=2
                                innerctr = ctr
                                while (tokvalue[innerctr] != ',' and tokvalue[innerctr] != '|'):
                                    if (toktype[innerctr] == 'CHARLit'  or tokvalue[innerctr] in CHAR or tokvalue[innerctr]=='[' or tokvalue[innerctr]==']'):
                                        pass
                                    else:
                                        semanticerrors.append("Semantic Error: Value "+tokvalue[innerctr]+" is not a character")
                                    innerctr += 1
                                ctr = innerctr
                                if (tokvalue[ctr] == ','):
                                    ctr+=1
                                    
                            elif(tokvalue[ctr+1] == ','):
                                if(tokvalue[ctr] in INT or tokvalue[ctr] in FLOAT or tokvalue[ctr] in CHAR or tokvalue[ctr] in STR or tokvalue[ctr] in BOOLEAN  or tokvalue[ctr] in VOID):
                                    semanticerrors.append("Semantic Error: Variable "+tokvalue[ctr]+" has already been declared")
                                    ctr+=2
                                else:
                                    CHAR.append(tokvalue[ctr])
                                    ctr+=2
                            elif(tokvalue[ctr+1] == '|'):
                                if(tokvalue[ctr] in INT or tokvalue[ctr] in FLOAT or tokvalue[ctr] in CHAR or tokvalue[ctr] in STR or tokvalue[ctr] in BOOLEAN  or tokvalue[ctr] in VOID):
                                    semanticerrors.append("Semantic Error: Variable "+tokvalue[ctr]+" has already been declared")
                                    ctr+=1
                                else:
                                    CHAR.append(tokvalue[ctr])
                                    ctr+=1
                                
                            else:
                                ctr+=1
                    
                    
             ################################################   
                    
                elif (tokvalue[i] == 'STR'):
                    ctr = i+1
                    if(tokvalue[ctr+1] == '('):
                        if(tokvalue[ctr] in INT or tokvalue[ctr] in FLOAT or tokvalue[ctr] in CHAR or tokvalue[ctr] in STR or tokvalue[ctr] in BOOLEAN  or tokvalue[ctr] in VOID):
                            semanticerrors.append("Semantic Error: "+tokvalue[ctr]+" has already been declared")
                            ctr+=1
                            while(tokvalue[ctr] != ')'):
                                ctr+=1
                        else:
                            functionvar = tokvalue[ctr]
                            STR.append(tokvalue[ctr])
                            ctr+=1
                            while(tokvalue[ctr] != ')'):
                                if(tokvalue[ctr] in datatype):
                                    param.append(tokvalue[ctr])
                                    if(tokvalue[ctr+1] in INT or tokvalue[ctr+1] in FLOAT or tokvalue[ctr+1] in CHAR or tokvalue[ctr+1] in STR or tokvalue[ctr+1] in BOOLEAN or tokvalue[ctr+1] in VOID):
                                        semanticerrors.append("Semantic Error: "+tokvalue[ctr]+" has already been declared")
                                    else:
                                        if(tokvalue[ctr] == 'INT'):
                                            INT.append(tokvalue[ctr+1])
                                            
                                        if(tokvalue[ctr] == 'FLOAT'):
                                            FLOAT.append(tokvalue[ctr+1])
                                        
                                        if(tokvalue[ctr] == 'CHAR'):
                                            CHAR.append(tokvalue[ctr+1])
                                        
                                        if(tokvalue[ctr] == 'STR'):
                                            STR.append(tokvalue[ctr+1])
                                        
                                        if(tokvalue[ctr] == 'BOOLEAN'):
                                            BOOLEAN.append(tokvalue[ctr+1])
                                ctr+=1
                            if(param):
                                dictionary[functionvar] = param
                            else:
                                dictionary[functionvar] = ['none']
                            param=[]
                            functionvar=''
                    else:
                        while (tokvalue[ctr] != '|'):
                            #a[
                            if (tokvalue[ctr + 1] == '['):
                                if(tokvalue[ctr] in INT or tokvalue[ctr] in FLOAT or tokvalue[ctr] in CHAR or tokvalue[ctr] in STR or tokvalue[ctr] in BOOLEAN  or tokvalue[ctr] in VOID):
                                    semanticerrors.append("Semantic Error: Variable "+tokvalue[ctr]+" has already been declared")
                                    ctr+=1
                                else:
                                    STR.append(tokvalue[ctr])
                                    ctr+=1
                                while (tokvalue[ctr] != ']'):
                                    ctr += 1
                                #] = {
                                if (tokvalue[ctr + 1] == '='):
                                    ctr += 2
                                    innerctr = ctr
                                    while (tokvalue[innerctr] != '|' and not (
                                            tokvalue[innerctr] == '}' and tokvalue[innerctr + 1] == ',' and toktype[innerctr + 2] == 'ID')):
                                        if (toktype[innerctr] == 'STRLit'  or tokvalue[innerctr] in STR or tokvalue[innerctr] in charmathop):
                                            pass
                                        else:
                                            semanticerrors.append("Semantic Error: Value "+tokvalue[innerctr]+" is not a string")
                                        innerctr += 1
                                    ctr = innerctr
                    
                                    if (tokvalue[ctr + 1] == ','):
                                        ctr += 2
                    
                                #][x] =
                                elif (tokvalue[ctr + 1] == '['):
                                    ctr += 1
                                    while (tokvalue[ctr] != ']'):
                                        ctr += 1
                                    if (tokvalue[ctr + 1] == '='):
                                        ctr += 2
                                        innerctr = ctr
                                        while (tokvalue[innerctr] != '|' and not (
                                                tokvalue[innerctr] == '}' and tokvalue[innerctr + 1] == ',' and toktype[
                                            innerctr + 2] == 'ID')):
                                            if (toktype[innerctr] == 'STRLit'  or tokvalue[innerctr] in STR or tokvalue[innerctr] in charmathop):
                                                pass
                                            else:
                                                semanticerrors.append("Semantic Error: Value "+tokvalue[innerctr]+" is not a string")
                                            innerctr += 1
                                        ctr = innerctr
                    
                                        if (tokvalue[innerctr + 1] == ','):
                                            ctr += 2
                                elif(tokvalue[ctr+1] == ','):
                                    ctr+=2
                                elif(tokvalue[ctr+1] == '|'):
                                    ctr+=1
                            
                    
                            #a =
                            elif(tokvalue[ctr + 1] == '='):
                                if(tokvalue[ctr] in INT or tokvalue[ctr] in FLOAT or tokvalue[ctr] in CHAR or tokvalue[ctr] in STR or tokvalue[ctr] in BOOLEAN  or tokvalue[ctr] in VOID):
                                    semanticerrors.append("Semantic Error: Variable "+tokvalue[ctr]+" has already been declared")
                                    ctr+=2
                                else:
                                    STR.append(tokvalue[ctr])
                                    ctr+=2
                                innerctr = ctr
                                while (tokvalue[innerctr] != ',' and tokvalue[innerctr] != '|'):
                                    if (toktype[innerctr] == 'STRLit'  or tokvalue[innerctr] in STR or tokvalue[innerctr]=='[' or tokvalue[innerctr]==']'):
                                        pass
                                    else:
                                        semanticerrors.append("Semantic Error: Value "+tokvalue[innerctr]+" is not a string")
                                    innerctr += 1
                                ctr = innerctr
                                if (tokvalue[ctr] == ','):
                                    ctr+=1
                            elif(tokvalue[ctr+1] == ','):
                                if(tokvalue[ctr] in INT or tokvalue[ctr] in FLOAT or tokvalue[ctr] in CHAR or tokvalue[ctr] in STR or tokvalue[ctr] in BOOLEAN  or tokvalue[ctr] in VOID):
                                    semanticerrors.append("Semantic Error: Variable "+tokvalue[ctr]+" has already been declared")
                                    ctr+=2
                                else:
                                    STR.append(tokvalue[ctr])
                                    ctr+=2
                            elif(tokvalue[ctr+1] == '|'):
                                if(tokvalue[ctr] in INT or tokvalue[ctr] in FLOAT or tokvalue[ctr] in CHAR or tokvalue[ctr] in STR or tokvalue[ctr] in BOOLEAN  or tokvalue[ctr] in VOID):
                                    semanticerrors.append("Semantic Error: Variable "+tokvalue[ctr]+" has already been declared")
                                    ctr+=1
                                else:
                                    STR.append(tokvalue[ctr])
                                    ctr+=1
                                
                            else:
                                ctr+=1
                        
                        
                ############################################################
                        
                elif (tokvalue[i] == 'BOOLEAN'):
                    ctr = i+1
                    if(tokvalue[ctr+1] == '('):
                        if(tokvalue[ctr] in INT or tokvalue[ctr] in FLOAT or tokvalue[ctr] in CHAR or tokvalue[ctr] in STR or tokvalue[ctr] in BOOLEAN  or tokvalue[ctr] in VOID):
                            semanticerrors.append("Semantic Error: "+tokvalue[ctr]+" has already been declared")
                            ctr+=1
                            while(tokvalue[ctr] != ')'):
                                ctr+=1
                        else:
                            functionvar = tokvalue[ctr]
                            BOOLEAN.append(tokvalue[ctr])
                            ctr+=1
                            while(tokvalue[ctr] != ')'):
                                if(tokvalue[ctr] in datatype):
                                    param.append(tokvalue[ctr])
                                    if(tokvalue[ctr+1] in INT or tokvalue[ctr+1] in FLOAT or tokvalue[ctr+1] in CHAR or tokvalue[ctr+1] in STR or tokvalue[ctr+1] in BOOLEAN or tokvalue[ctr+1] in VOID):
                                        semanticerrors.append("Semantic Error: "+tokvalue[ctr]+" has already been declared")
                                    else:
                                        if(tokvalue[ctr] == 'INT'):
                                            INT.append(tokvalue[ctr+1])
                                            
                                        if(tokvalue[ctr] == 'FLOAT'):
                                            FLOAT.append(tokvalue[ctr+1])
                                        
                                        if(tokvalue[ctr] == 'CHAR'):
                                            CHAR.append(tokvalue[ctr+1])
                                        
                                        if(tokvalue[ctr] == 'STR'):
                                            STR.append(tokvalue[ctr+1])
                                        
                                        if(tokvalue[ctr] == 'BOOLEAN'):
                                            BOOLEAN.append(tokvalue[ctr+1])
                                ctr+=1
                            if(param):
                                dictionary[functionvar] = param
                            else:
                                dictionary[functionvar] = ['none']
                            param=[]
                            functionvar=''
                    else:
                        while (tokvalue[ctr] != '|'):
                            #a[
                            if (tokvalue[ctr + 1] == '['):
                                if(tokvalue[ctr] in INT or tokvalue[ctr] in FLOAT or tokvalue[ctr] in CHAR or tokvalue[ctr] in STR or tokvalue[ctr] in BOOLEAN  or tokvalue[ctr] in VOID):
                                    semanticerrors.append("Semantic Error: Variable "+tokvalue[ctr]+" has already been declared")
                                    ctr+=1
                                else:
                                    BOOLEAN.append(tokvalue[ctr])
                                    ctr+=1
                                while (tokvalue[ctr] != ']'):
                                    ctr += 1
                                #] = {
                                if (tokvalue[ctr + 1] == '='):
                                    ctr += 2
                                    innerctr = ctr
                                    while (tokvalue[innerctr] != '|' and not (
                                            tokvalue[innerctr] == '}' and tokvalue[innerctr + 1] == ',' and toktype[innerctr + 2] == 'ID')):
                                        if (tokvalue[innerctr] == 'TRUE' or tokvalue[innerctr] == 'FALSE' or tokvalue[innerctr] in BOOLEAN or tokvalue[innerctr] in charmathop):
                                            pass
                                        else:
                                            semanticerrors.append("Semantic Error: Value "+tokvalue[innerctr]+" is not a boolean")
                                        innerctr += 1
                                    ctr = innerctr
                    
                                    if (tokvalue[ctr + 1] == ','):
                                        ctr += 2
                    
                                #][x] =
                                elif (tokvalue[ctr + 1] == '['):
                                    ctr += 1
                                    while (tokvalue[ctr] != ']'):
                                        ctr += 1
                                    if (tokvalue[ctr + 1] == '='):
                                        ctr += 2
                                        innerctr = ctr
                                        while (tokvalue[innerctr] != '|' and not (
                                                tokvalue[innerctr] == '}' and tokvalue[innerctr + 1] == ',' and toktype[
                                            innerctr + 2] == 'ID')):
                                            if (tokvalue[innerctr] == 'TRUE' or tokvalue[innerctr] == 'FALSE' or tokvalue[innerctr] in BOOLEAN or tokvalue[innerctr] in charmathop):
                                                pass
                                            else:
                                                semanticerrors.append("Semantic Error: Value "+tokvalue[innerctr]+" is not a boolean")
                                            innerctr += 1
                                        ctr = innerctr
                    
                                        if (tokvalue[innerctr + 1] == ','):
                                            ctr += 2
                                elif(tokvalue[ctr+1] == ','):
                                    ctr+=2
                                elif(tokvalue[ctr+1] == '|'):
                                    ctr+=1
                    
                            #a =
                            elif(tokvalue[ctr + 1] == '='):
                                if(tokvalue[ctr] in INT or tokvalue[ctr] in FLOAT or tokvalue[ctr] in CHAR or tokvalue[ctr] in STR or tokvalue[ctr] in BOOLEAN  or tokvalue[ctr] in VOID):
                                    semanticerrors.append("Semantic Error: Variable "+tokvalue[ctr]+" has already been declared")
                                    ctr+=2
                                else:
                                    BOOLEAN.append(tokvalue[ctr])
                                    ctr+=2
                                innerctr = ctr
                                while (tokvalue[innerctr] != ',' and tokvalue[innerctr] != '|'):
                                    if (tokvalue[innerctr] == 'TRUE'  or tokvalue[innerctr] == 'TRUE' or tokvalue[innerctr] in BOOLEAN or tokvalue[innerctr]=='[' or tokvalue[innerctr]==']'):
                                        pass
                                    else:
                                        semanticerrors.append("Semantic Error: Value "+tokvalue[ctr]+" is not a boolean")
                                    innerctr += 1
                                ctr = innerctr
                                if (tokvalue[ctr] == ','):
                                    ctr+=1
                            
                            elif(tokvalue[ctr+1] == ','):
                                if(tokvalue[ctr] in INT or tokvalue[ctr] in FLOAT or tokvalue[ctr] in CHAR or tokvalue[ctr] in STR or tokvalue[ctr] in BOOLEAN  or tokvalue[ctr] in VOID):
                                    semanticerrors.append("Semantic Error: Variable "+tokvalue[ctr]+" has already been declared")
                                    ctr+=2
                                else:
                                    BOOLEAN.append(tokvalue[ctr])
                                    ctr+=2
                            elif(tokvalue[ctr+1] == '|'):
                                if(tokvalue[ctr] in INT or tokvalue[ctr] in FLOAT or tokvalue[ctr] in CHAR or tokvalue[ctr] in STR or tokvalue[ctr] in BOOLEAN  or tokvalue[ctr] in VOID):
                                    semanticerrors.append("Semantic Error: Variable "+tokvalue[ctr]+" has already been declared")
                                    ctr+=1
                                else:
                                    BOOLEAN.append(tokvalue[ctr])
                                    ctr+=1
                                
                            else:
                                ctr+=1
                
                
                if(ctr != 0):
                    i = ctr
            
            elif(toktype[i] == 'ID'):
                if(tokvalue[i+1] == '('):
                    if tokvalue[i] not in dictionary:
                        semanticerrors.append("Semantic Error: Function "+tokvalue[i]+" is not declared")
                        ctr = i
                        while(tokvalue[ctr] != '|'):
                            ctr+=1
                    else:
                        funcid = len(dictionary[tokvalue[i]])
                        ctr=i+1
                        if(tokvalue[ctr] == ')'):
                            pass
                        else:
                            functctr=0
                            
                            while(tokvalue[ctr] != '|'):
                                
                                innerctr = ctr
                                if(functctr+1 <= funcid):
                                    pass
                                else:
                                    functctr+=1
                                    break
                                
                                while(tokvalue[innerctr] != ',' and tokvalue[innerctr] != '|'):

                                    
                                    if(toktype[innerctr] == 'ID'):
                                        if(tokvalue[innerctr] in INT):
                                            if(dictionary[tokvalue[i]][functctr] == 'INT'):
                                                pass
                                            else:
                                                semanticerrors.append("Semantic Error: Argument "+tokvalue[innerctr]+" has incompatible datatype")
                                        elif(tokvalue[innerctr] in FLOAT):
                                            if(dictionary[tokvalue[i]][functctr] == 'FLOAT'):
                                                pass
                                            else:
                                                semanticerrors.append("Semantic Error: Argument "+tokvalue[innerctr]+" has incompatible datatype")
                                        elif(tokvalue[innerctr] in CHAR):
                                            if(dictionary[tokvalue[i]][functctr] == 'CHAR'):
                                                pass
                                            else:
                                                semanticerrors.append("Semantic Error: Argument "+tokvalue[innerctr]+" has incompatible datatype")
                                        elif(tokvalue[innerctr] in STR):
                                            if(dictionary[tokvalue[i]][functctr] == 'STR'):
                                                pass
                                            else:
                                                semanticerrors.append("Semantic Error: Argument "+tokvalue[innerctr]+" has incompatible datatype")
                                        elif(tokvalue[innerctr] in BOOLEAN):
                                            if(dictionary[tokvalue[i]][functctr] == 'BOOLEAN'):
                                                pass
                                            else:
                                                semanticerrors.append("Semantic Error: Argument "+tokvalue[innerctr]+" has incompatible datatype")
                                        else:
                                            semanticerrors.append("Semantic Error: Argument "+tokvalue[innerctr]+" has not yet been declared")
                                    elif(toktype[innerctr] in lits or tokvalue[innerctr] == "TRUE" or tokvalue[innerctr] == "FALSE"):
                                        
                                        if(toktype[innerctr] == "INTLit"):
                                            
                                            if (dictionary[tokvalue[i]][functctr] == 'INT' or dictionary[tokvalue[i]][functctr] == 'FLOAT'):
                                                pass
                                            else:
                                                semanticerrors.append("121Semantic Error: Argument "+tokvalue[innerctr]+
                                                      " has incompatible type")
                                        elif(toktype[innerctr] == "FLOATLit"):
                                            if (dictionary[tokvalue[i]][functctr] == 'FLOAT' or dictionary[tokvalue[i]][functctr] == 'INT'):
                                                pass
                                            else:
                                                semanticerrors.append("Semantic Error: Argument "+tokvalue[innerctr]+
                                                      " has incompatible type")
                                        elif (toktype[innerctr] == "CHARLit"):
                                            if (dictionary[tokvalue[i]][functctr] == 'CHAR'):
                                                pass
                                            else:
                                                semanticerrors.append("Semantic Error: Argument "+tokvalue[innerctr]+
                                                      " has incompatible type")
                                        elif (toktype[innerctr] == "STRLit"):
                                            if (dictionary[tokvalue[i]][functctr] == 'STR'):
                                                pass
                                            else:
                                                semanticerrors.append("Semantic Error: Argument "+tokvalue[innerctr]+
                                                      " has incompatible type")
                                        elif (tokvalue[innerctr] == "TRUE" or tokvalue[innerctr] == "FALSE"):
                                            if (dictionary[tokvalue[i]][functctr] == 'BOOLEAN'):
                                                pass
                                            else:
                                                semanticerrors.append("Semantic Error: Argument "+tokvalue[innerctr]+
                                                      " has incompatible type")
                                    innerctr+=1
                                functctr+=1
                                
                                
                                if(tokvalue[innerctr] == '|'):
                                    ctr = innerctr
                                else:
                                    ctr = innerctr+1
                                #--------#
                            if(functctr != funcid):
                                semanticerrors.append("Semantic Error: Number of argument/s do not match parameters")
                                while(tokvalue[innerctr] != '|'):
                                    innerctr+=1
                        i=ctr
                        
                elif(tokvalue[i] in INT):
                    ctr = i+1
                    if(tokvalue[ctr] in assignop):
                        ctr+=1
                        while(tokvalue[ctr] != '|' and (tokvalue[ctr] != ")" and tokvalue[ctr+1] != "{")):
                            if(toktype[ctr] == 'FLOATLit' or toktype[ctr] == 'INTLit' or tokvalue[ctr] in FLOAT or tokvalue[ctr] in INT or tokvalue[ctr] in mathop):
                                pass
                            else:
                                semanticerrors.append("Semantic Error: Value "+tokvalue[ctr]+" has incompatible type")
                            ctr+=1
                    elif(tokvalue[ctr]=='++' or tokvalue[ctr]=='--'):
                        ctr+=1
                        
                elif(tokvalue[i] in FLOAT):
                    ctr = i+1
                    if(tokvalue[ctr] in assignop):
                        ctr+=1
                        while(tokvalue[ctr] != '|' and (tokvalue[ctr] != ")" and tokvalue[ctr+1] != "{")):
                            if(toktype[ctr] == 'FLOATLit' or toktype[ctr] == 'INTLit' or tokvalue[ctr] in FLOAT or tokvalue[ctr] in INT or tokvalue[ctr] in mathop):
                                pass
                            else:
                                semanticerrors.append("Semantic Error: Value "+tokvalue[ctr]+" has incompatible type")
                            ctr+=1
                    elif(tokvalue[ctr]=='++' or tokvalue[ctr]=='--'):
                        ctr+=1
                        
                elif(tokvalue[i] in CHAR): 
                    ctr = i+1
                    if(tokvalue[ctr] == '='):
                        ctr+=1
                        if(toktype[ctr] == 'CHARLit' or tokvalue[ctr] in CHAR):
                            ctr+=1
                            while(tokvalue[ctr] != '|' and (tokvalue[ctr] != ")" and tokvalue[ctr+1] != "{")):
                                ctr+=1
                        else:
                            semanticerrors.append("Semantic Error: Value "+tokvalue[ctr]+" has incompatible type")
                            while(tokvalue[ctr] != '|' and (tokvalue[ctr] != ")" and tokvalue[ctr+1] != "{")):
                                ctr+=1
                    elif(tokvalue[ctr]=='++' or tokvalue[ctr]=='--' or tokvalue[ctr] in assignop or tokvalue[ctr] in mathop2):
                        ctr+=1
                        semanticerrors.append("Semantic Error: cannot use mathematical operation in char variable")
            
                        
                elif(tokvalue[i] in STR): 
                    ctr = i+1
                    if(tokvalue[ctr] == '='):
                        ctr+=1
                        if(toktype[ctr] == 'STRLit' or tokvalue[ctr] in STR):
                            ctr+=1
                            while(tokvalue[ctr] != '|' and (tokvalue[ctr] != ")" and tokvalue[ctr+1] != "{")):
                                ctr+=1
                        else:
                            semanticerrors.append("Semantic Error: Value "+tokvalue[ctr]+" has incompatible type")
                            while(tokvalue[ctr] != '|' and (tokvalue[ctr] != ")" and tokvalue[ctr+1] != "{")):
                                ctr+=1
                    elif(tokvalue[ctr]=='++' or tokvalue[ctr]=='--' or tokvalue[ctr] in assignop or tokvalue[ctr] in mathop2):
                        ctr+=1
                        semanticerrors.append("semantic error: cannot use mathematical operation in string variable")

                        
                elif(tokvalue[i] in BOOLEAN): 
                    ctr = i+1
                    if(tokvalue[ctr] == '='):
                        ctr+=1
                        #while(tokvalue[ctr] != '|'):
                        if(tokvalue[ctr] == 'TRUE' or tokvalue[ctr] == 'FALSE'or tokvalue[ctr] in BOOLEAN):
                            ctr+=1
                            while(tokvalue[ctr] != '|' and (tokvalue[ctr] != ")" and tokvalue[ctr+1] != "{")):
                                ctr+=1
                        else:
                            semanticerrors.append("Semantic Error: Value "+tokvalue[ctr]+" has incompatible type")
                            #ctr+=1
                            while(tokvalue[ctr] != '|' and (tokvalue[ctr] != ")" and tokvalue[ctr+1] != "{")):
                                ctr+=1
                    elif(tokvalue[ctr]=='++' or tokvalue[ctr]=='--' or tokvalue[ctr] in assignop or tokvalue[ctr] in mathop2):
                        ctr+=1
                        semanticerrors.append("semantic error: cannot use mathematical operation in boolean variable")
                else:
                    semanticerrors.append("Semantic error: Variable "+tokvalue[i]+" is not declared")
                    while(tokvalue[i] != '|' and (tokvalue[ctr] != ")" and tokvalue[ctr+1] != "{")):
                        i+=1
                if(ctr != 0):
                    i = ctr
                
                
                
            elif(tokvalue[i] == '++' or tokvalue[i] == '--'):
                ctr=i+1
                if(toktype[ctr]=='ID'):
                    if(tokvalue[ctr] not in INT and tokvalue[ctr] not in FLOAT):
                        semanticerrors.append("Semantic Error: Variable "+tokvalue[ctr]+" is not an integer or float")
                        
                if(ctr != 0):
                    i = ctr
            elif(tokvalue[i]=='DOJO'):
                while(tokvalue[i]!= '}'):
                    i+=1
                while(tokvalue[i]!='|'):
                    i+=1

            # elif(tokvalue[i] == "IF"):
            #     while(tokvalue[i] != ")" or tokvalue[i+1] != "{"):
            #         if(toktype[i] == "ID"):
            #             if(tokvalue[i] in INT):
            #                 i+=1
            #             elif(tokvalue[i] in INT):
            #                 i += 1
                    
            elif(tokvalue[i]=='RETURN'):
                revctr = i
                ctr = i+1
                while((tokvalue[revctr] not in datatype and tokvalue[revctr]!='VOID') or toktype[revctr+1] !='ID' or tokvalue[revctr+2] != '('):
                    revctr-=1
                if(tokvalue[revctr] == 'INT' or tokvalue[revctr] == 'FLOAT'):
                    while(tokvalue[ctr] != '|'):
                        if (toktype[ctr] == 'FLOATLit' or toktype[ctr] == 'INTLit' or tokvalue[ctr] in FLOAT or tokvalue[ctr] in INT or tokvalue[ctr] in arrmathop):
                            pass
                        else:
                            semanticerrors.append("Semantic Error: Return Value "+tokvalue[ctr]+" does not have compatible datatype")
                        ctr+=1
                            
                elif(tokvalue[revctr] == 'CHAR'):
                    
                    while(tokvalue[ctr] != '|'):
                        if (toktype[ctr] == 'CHARLit'  or tokvalue[ctr] in CHAR or tokvalue[ctr] in charmathop):
                            pass
                        else:
                            semanticerrors.append("Semantic Error: Return Value "+tokvalue[ctr]+" does not have compatible datatype")
                        ctr+=1
                    
                elif(tokvalue[revctr] == 'STR'):
                    while(tokvalue[ctr] != '|'):
                        if (toktype[ctr] == 'STRLit'  or tokvalue[ctr] in STR or tokvalue[ctr] in charmathop):
                            pass
                        else:
                            semanticerrors.append("Semantic Error: Return Value "+tokvalue[ctr]+" does not have compatible datatype")
                        ctr+=1
                
                elif(tokvalue[revctr] == 'BOOLEAN'):
                    while(tokvalue[ctr] != '|'):
                        if (tokvalue[ctr] == 'TRUE'  or tokvalue[ctr] == 'FALSE' or tokvalue[ctr] in BOOLEAN or tokvalue[ctr] in charmathop):
                            pass
                        else:
                            semanticerrors.append("Semantic Error: Return Value "+tokvalue[ctr]+" does not have compatible datatype")
                        ctr+=1
                elif(tokvalue[revctr] == 'VOID'):
                    while(tokvalue[ctr] != '|'):
                        if(tokvalue[ctr] != '(' and tokvalue[ctr] != ')'):
                            semanticerrors.append("Semantic Error: Void cannot have return value")
                        ctr+=1
            
            # elif(tokvalue[i]=='PRINT'):
            #     while(tokvalue[i]!='|'):
            #         i+=1
                
            # elif(tokvalue[i]=='PRINT' or tokvalue[i]=='INPUT' or tokvalue[i]=='RETURN'):
            #     while(tokvalue[i]!='|'):
            #         i+=1
            
            # elif(tokvalue[i]=='IF' or tokvalue[i]=='ELSEIF' or tokvalue[i]=='FOR' or tokvalue[i]=='QUIVER' or tokvalue[i]=='WHILE' ):
            #     while(tokvalue[i]!= '{'):
            #         i+=1
            elif(tokvalue[i]=='QUIVER'):
                i+=2
                if(toktype[i] == 'ID'):
                    if(tokvalue[i] in INT or tokvalue[i] in CHAR):
                        pass
                    else:
                        semanticerrors.append("Semantic Error:  QUIVER can only accept Integer or Character Variable")
                

            
            
            

            
            i+=1 
        for i in INT:
            print(i)
    
    
    def lexical(self):
        self.Label3.configure(text='''Lexical Errors''')
        self.Listbox1.delete(0,tk.END)
        self.Listbox2.delete(0,tk.END)
        self.Button3.configure(state='disabled')
        inputlex = self.Text1.get("1.0",END)
        lexer.input(inputlex)
        
        lexerrors=[]
        tokens=[]
        toks=[]
        previousToken=' '
        previousValue=' '
        tokctr = []
        ctr = 0
        errorsymbol = []
        
        
        flag = False
        for tok in lexer:
            print(tok.type)
            try:
                listVal = delimDict[previousToken]

                if((tok.value not in listVal and tok.type not in listVal) or tok.type=='error'):
                    lexerrors.append('ERROR: Invalid lexeme for \'{}\' '.format(previousValue))
                    tokctr.append(ctr-1)
                if(tok.type == 'error' and flag == False):
                    print(tok.value)
                    for i in tok.value:
                        if ((ord(i)<65 or ord(i)>90) and (ord(i)<97 or ord(i)>122) and (ord(i)<48 or ord(i)>57)):
                            if (i not in symbols):
                                errorsymbol.append(i)
                    flag = True
                previousToken = tok.type
                previousValue = tok.value
                toks.append(tok)
            except:
                previousToken = tok.type
                previousValue = tok.value
                toks.append(tok)
            if(tok.type == 'SPACE' or tok.type == 'error'):
                tokctr.append(ctr)
            if(tok.type != 'INTLit' and tok.type != 'FLOATLit' and tok.type != 'STRLit' and tok.type != 'CHARLit' and tok.type != 'ID'):
                tokens.append("   {:15s} {:20s}".format(tok.value,tok.value))
            else:
                tokens.append("   {:15s} {:20s}".format(tok.value,tok.type))
            ctr+=1

        ctr = 0
        
        # if(flag == True):
        #     self.Button2.configure(state='disabled')
        #     lexerrors.append('ERROR: Unidentified symbol/s {} '.format(errorsymbol))
        #     errorsymbol.clear()
        
        for i in tokens:
            if(ctr not in tokctr):
                self.Listbox1.insert(END, (i))
            ctr+=1

        if(lexerrors):
            self.Button2.configure(state='disabled')
            for i in lexerrors:
                self.Listbox2.insert(END, ("   {:15s}".format(i)))
        else:
            self.Button2.configure(state='normal')
            self.Listbox2.insert(END, ("   {:15s}".format("No Lexical Error")))
            
    def parsergui(self):
        self.Button2.configure(state='disabled')
        self.Label2.configure(text='''''')
        self.Label3.configure(text='''Syntax Analyzer''')
        self.Listbox1.delete(0,tk.END)
        self.Listbox2.delete(0,tk.END)
        inputparse = self.Text1.get("1.0",END)
        global syntaxerror
        global toktype
        global tokvalue
        global tokctr
        global semanticerrors
        #result = parser.parse(inputparse)
        lexi.input(inputparse)
        
        for tok in lexi:
            #print(tok.type, ": ", tok.value)
            toktype.append(tok.type)
            tokvalue.append(tok.value)
        
        
        
        self.program()
        #self.semantic()
        if(syntaxerror):
            self.Listbox2.insert(0,syntaxerror[0])
            for i in syntaxerror:
                print(syntaxerror)
            self.Button3.configure(state='disabled')
    
        else:
            self.Listbox2.insert(0,"No Syntax Error")
            self.Button3.configure(state='normal')
            
        
        
            
        semanticerrors=[]
        syntaxerror=[]
        toktype=[]
        tokvalue=[]
        inputparse=''
        tokctr=0
        
    def semanticgui(self):
        self.Button3.configure(state='disabled')
        self.Label2.configure(text='''''')
        self.Label3.configure(text='''Semantics Analyzer''')
        self.Listbox1.delete(0,tk.END)
        self.Listbox2.delete(0,tk.END)
        inputparse = self.Text1.get("1.0",END)
        global syntaxerror
        global toktype
        global tokvalue
        global tokctr
        global semanticerrors
        #result = parser.parse(inputparse)
        lexi.input(inputparse)
        
        for tok in lexi:
            #print(tok.type, ": ", tok.value)
            toktype.append(tok.type)
            tokvalue.append(tok.value)
        
        
        
        #self.program()
        self.semantic()
        
        
        counter=0
        if(semanticerrors):
            #while(counter<len(semanticerrors)):
            self.Listbox1.insert(0,semanticerrors[0])
        else:
            self.Listbox1.insert(0,"No Semantic Error")
            
        semanticerrors=[]
        syntaxerror=[]
        toktype=[]
        tokvalue=[]
        inputparse=''
        tokctr=0
        
        
        
        
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("1177x727+267+60")
        top.minsize(120, 1)
        top.maxsize(1604, 881)
        top.resizable(1,  1)
        top.title("ARCHER COMPILER")
        top.configure(background="#d9d9d9")

        self.Text1 = tk.Text(top)
        self.Text1.place(relx=0.025, rely=0.206, relheight=0.748, relwidth=0.489)

        self.Text1.configure(background="white")
        self.Text1.configure(font="-family {Courier New} -size 14")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="blue")
        self.Text1.configure(selectforeground="white")
        self.Text1.configure(wrap="word")

        self.Listbox1 = tk.Listbox(top)
        self.Listbox1.place(relx=0.527, rely=0.151, relheight=0.359
                , relwidth=0.455)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(cursor="hand2")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="-family {Courier New} -size 12")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(justify=LEFT)
        scrollbar = Scrollbar(self.Listbox1)
        scrollbar.pack(side = RIGHT, fill = BOTH) 
        self.Listbox1.config(yscrollcommand = scrollbar.set) 
        

        self.Listbox2 = tk.Listbox(top)
        self.Listbox2.place(relx=0.527, rely=0.578, relheight=0.373
                , relwidth=0.453)
        self.Listbox2.configure(background="white")
        self.Listbox2.configure(cursor="hand2")
        self.Listbox2.configure(disabledforeground="#a3a3a3")
        self.Listbox2.configure(font="-family {Courier New} -size 12 -weight bold")
        self.Listbox2.configure(foreground="#000000")
        #self.Listbox2.config(width=10,height=10)
        # scrollbar2 = Scrollbar(self.Listbox2)
        # scrollbar2.pack(side = BOTTOM, fill = X) 
        # #scrollbar2 = Scrollbar(master, orient=HORIZONTAL)
        # self.Listbox2.config(xscrollcommand = scrollbar2.set) 
        


        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.348, rely=0.041, height=32, width=453)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Courier New} -size 24 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''ARCHER COMPILER''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.586, rely=0.11, height=21, width=402)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Courier New} -size 15 -weight bold")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Lexical Analyzer''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.586, rely=0.536, height=21, width=415)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Courier New} -size 16 -weight bold")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Lexical Errors''')

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.025, rely=0.165, height=21, width=168)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Courier New} -size 13 -weight bold")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Enter Code Here:''')

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.229, rely=0.151, height=34, width=107)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#80ff80")
        self.Button1.configure(cursor="hand2")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Courier New} -size 13 -weight bold")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(command=self.lexical)
        self.Button1.configure(text='''Lexical''')

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.331, rely=0.151, height=34, width=97)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#ffff80")
        self.Button2.configure(cursor="hand2")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Courier New} -size 13 -weight bold")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="#ffffff")
        self.Button2.configure(pady="0")
        self.Button2.configure(command=self.parsergui)
        self.Button2.configure(text='''Syntax''')
        self.Button2.configure(state='disabled')
        
        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.423, rely=0.151, height=34, width=97)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#FFC0CB")
        self.Button3.configure(cursor="hand2")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font="-family {Courier New} -size 13 -weight bold")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="#ffffff")
        self.Button3.configure(pady="0")
        self.Button3.configure(command=self.semanticgui)
        self.Button3.configure(text='''Semantics''')
        self.Button3.configure(state='disabled')

if __name__ == '__main__':
    vp_start_gui()
    
    





