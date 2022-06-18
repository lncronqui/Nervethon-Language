from asyncio.windows_events import NULL
import tkinter as tk

from tkinter import ttk
from tkinter import *
from xmlrpc.client import boolean

from lexer3 import *
from syntax_lexer import *
from syntax_analyze import *

from typing import NamedTuple


#creating the window
root= tk.Tk()
root.geometry('1440x768')
root.resizable(FALSE, FALSE)
root.configure(bg='#171717')
root.title('Nervethon')

#Frame Top
frame_top=Frame(root,width=1440,height=70, background='#0F0F0F')
frame_top.grid(row=0, column=0, columnspan=2)

#Photos
photo_imageClear=PhotoImage(file='Clear.png')
photo_imageSemantic=PhotoImage(file='Syntax.png')
photo_imageLexical=PhotoImage(file='Lexical.png')
photo_imageNervethon=PhotoImage(file='Nervy.png')

#Logo
canvasLogo=Canvas(frame_top, width=270, height=55, borderwidth=0, highlightbackground='#0F0F0F', background='#0F0F0F')
canvasLogo.create_image(140,29, image=photo_imageNervethon)
canvasLogo.place(x=20,y=5)

#Frame 1 Top left size
frame1=Frame(root, width=600, height=350, highlightbackground='gray', bg='#121212', highlightcolor='gray', highlightthickness=1)
frame1.place(x=15,y=100)

#Frame 1 Style
style=ttk.Style(frame1)
style.theme_use('alt')
style.configure("Vertical.TScrollbar", troughcolor="#0F0F0F", highlightcolor="#313537", bordercolor="white", arrowcolor="blue")

#Scrollbar and Text area
scrollbar=ttk.Scrollbar(frame1, orient='vertical')
scrollbarh=ttk.Scrollbar(frame1,orient="horizontal")
text_area = Text(frame1, bg='#121212', width = 48, height = 20, font = ("Courier",15), insertbackground='white', fg="White", yscrollcommand=scrollbar.set, xscrollcommand=scrollbarh.set, wrap="none")
scrollbarh.config(command=text_area.xview)
scrollbarh.pack(side=BOTTOM, fill=X)
scrollbar.config(command=text_area.yview)
scrollbar.pack(side=RIGHT, fill=Y)
text_area.pack(side="left")

#Frame 2 - Errors
frame2=Frame(root, width=600, height=100, highlightbackground='gray', bg='#121212', highlightcolor='gray', highlightthickness=1)
frame2.place(x=15,y=615)

scrollbar2=ttk.Scrollbar(frame2, orient='vertical')
Errors = Text(frame2, width = 48, height =6, font = ("Courier",15), bg = "#121212", fg="White", highlightthickness=0, borderwidth=0, state='disabled',  yscrollcommand=scrollbar2.set)
scrollbar2.config(command=Errors.yview)
scrollbar2.pack(side=RIGHT, fill=Y)
Errors.pack(side="left")

#TRIAL INPUT AND OUTPUT
def Take_input():
    Output.configure(state='normal')
    Errors.configure(state='normal')
    OutputTok.configure(state='normal')
    Output.delete(1.0,END)#How to reset text area
    Errors.delete(1.0,END)#How to reset text area
    OutputTok.delete(1.0,END)
    lexer.lineno = 1
    INPUT = text_area.get("1.0", "end-1c")
    lexer.input(INPUT)
    
    
    tokens=[]
    lexerrors=[]
    prevToken = ''
    prevValue = ''
    
    
    while True:
        tok = lexer.token()
        if not tok:
                break
        try:
            listVal = delimDict[prevToken]
            if not(tok.type == 'space'):
                if (tok.value not in listVal and tok.type not in listVal):
                    if(tok.value == '\n'):
                        lexerrors.append("ERROR: '{}' not a delimiter for '{}' at line {}".format('\\n', prevValue, tok.lineno))
                    else:
                        lexerrors.append("ERROR: '{}' not a delimiter for '{}' at line {}".format(tok.value, prevValue, tok.lineno))
                    tokens = tokens[:-1]
            prevToken = tok.type
            prevValue = tok.value
            if tok.type == 'error':
                lexerrors.append("ERROR: Incorrect lexeme '{}' at line {}".format(tok.value, tok.lineno))
                continue
            if tok.type == 'error1':
                lexerrors.append("ERROR: Reserved word '{}' as identifier at line {}".format(tok.value, tok.lineno))
                continue
            if tok.type == 'error2':
                lexerrors.append("ERROR: Invalid lexeme '{}' at line {}".format(tok.value,tok.lineno))
                continue
            if tok.type == 'error3':
                lexerrors.append("error3")
                continue
            tokens.append(tok)
        except:
            prevToken = tok.type
            prevValue = tok.value
            if tok.type == 'error':
                lexerrors.append("ERROR: Incorrect lexeme '{}' at line {}".format(tok.value, tok.lineno))
                continue
            if tok.type == 'error1':
                lexerrors.append("ERROR: Reserved word '{}' as identifier at line {}".format(tok.value, tok.lineno))
                continue
            if tok.type == 'error2':
                lexerrors.append("ERROR: Invalid lexeme '{}' at line {}".format(tok.value,tok.lineno))
                continue
            if tok.type == 'error3':
                lexerrors.append("error3")
                continue
            if tok.type == 'space' or tok.type == 'newline':
                continue
            tokens.append(tok)
            
    
    if(lexerrors):
        Run_Semantic.configure(state = 'disabled')
        for i in lexerrors:
            Errors.insert(END, (i))
            Errors.insert(END, '\n')
    else:
        Run_Semantic.configure(state='normal')
        Errors.insert(END, ("{}".format("No Lexical Error")))
    if(tokens):
        for i in tokens:
            if i.type == 'space' or i.type == 'newline':
                continue
            OutputTok.insert(END, i.type)
            OutputTok.insert(END, '\n')
            Output.insert(END, i.value)
            Output.insert(END, '\n')
    Output.configure(state='disabled')
    OutputTok.configure(state='disabled')
    Errors.configure(state='disabled')
        
    
    
def Run_Syntax():
    Output.configure(state='normal')
    Errors.configure(state='normal')
    OutputTok.configure(state='normal')
    Output.delete(1.0,END)#How to reset text area
    Errors.delete(1.0,END)#How to reset text area
    OutputTok.delete(1.0,END)
    lexer_syntax.lineno = 1
    INPUT = text_area.get("1.0", "end-1c")
    lexer_syntax.input(INPUT)
    lexer_syntax.lineno = 1
    result = parser.parse(INPUT, lexer=lexer_syntax)
    out = result.traverse()
    if errors:
        for i in errors:
            Errors.insert(END, ("ERROR: {}".format(i)))
            Errors.insert(END, '\n')
    else:
        Errors.insert(END, ("{}".format("No Syntax Error")))
        
    if out:
        for x in out:
            # print(x)
            y = x.tabs
            z = 0
            while y > z:
                OutputTok.insert(END, '|__')
                z += 1
            OutputTok.insert(END, x.output)
            OutputTok.insert(END, '\n')
            
    result.clear()
    Output.configure(state='disabled')
    OutputTok.configure(state='disabled')
    Errors.configure(state='disabled')
    Run_Semantic.configure(state = 'disabled')
    

            
    
#Frame 3 - Output Lex
frame3=Frame(root, width=400, height=660, highlightbackground='gray', bg='#121212', highlightcolor='gray', highlightthickness=1)
frame3.place(x=625, y=130)
#Frame 4 - Output Token
frame4=Frame(root, width=850, height=660, highlightbackground='gray', bg='#121212', highlightcolor='gray', highlightthickness=1)
frame4.place(x=870, y=130)
#Frame 5 - Semantic
#frame5=Frame(root, width=400, height=660, highlightbackground='gray', bg='#121212', highlightcolor='gray', highlightthickness=1)
#frame5.place(x=1115, y=130)

#OUTPUT Lex TEXT AREA
scrollbar3=ttk.Scrollbar(frame3, orient='vertical')
Output = Text(frame3, width = 18, height =28, font = ("Courier",15), bg = "#121212", fg="White", highlightthickness=0, borderwidth=0, state='disabled',  yscrollcommand=scrollbar3.set)
scrollbar3.config(command=Output.yview)
scrollbar3.pack(side=RIGHT, fill=Y)
Output.pack(side="left")

#OUTPUT Token TEXT AREA
scrollbar4=ttk.Scrollbar(frame4, orient='vertical')
OutputTok = Text(frame4, width = 44, height =28, font = ("Courier",15), bg = "#121212", fg="White", highlightthickness=0, borderwidth=0, state='disabled',  yscrollcommand=scrollbar4.set)
scrollbar4.config(command=OutputTok.yview)
scrollbar4.pack(side=RIGHT, fill=Y)
OutputTok.pack(side="left")

#OUTPUT Semantic TEXT AREA
#scrollbar5=ttk.Scrollbar(frame5, orient='vertical')
#OutputSem = Text(frame5, width = 18, height =28, font = ("Courier",15), bg = "#121212", fg="White", highlightthickness=0, borderwidth=0, state='disabled',  yscrollcommand=scrollbar5.set)
#scrollbar5.config(command=OutputSem.yview)
#scrollbar5.pack(side=RIGHT, fill=Y)
#OutputSem.pack(side="left")

lblLex=Label(root,text="Lexeme", font = ("Nunito",14), fg='white',bg='#171717')
lblLex.place(x=630,y=98)
lblTok=Label(root,text="Tokens / Syntax" , font = ("Nunito",14), fg='white',bg='#171717')
lblTok.place(x=880,y=98) 
lblErr=Label(root,text="Errors", font = ("Nunito",14), fg='white',bg='#171717')
lblErr.place(x=25,y=580)

#For Clear
def clear_input():
    text_area.delete(1.0,END)#How to reset text area
    Output.configure(state='normal')
    Errors.configure(state='normal')
    OutputTok.configure(state='normal')
    Output.delete(1.0,END)#How to reset text area
    Errors.delete(1.0,END)#How to reset text area
    OutputTok.delete(1.0,END)
    Output.configure(state='disabled')
    Errors.configure(state='disabled')
    OutputTok.configure(state='disabled')
    
#Buttons or inside of Frame_top
Clear=Button(frame_top, width=129, height=32, image=photo_imageClear, border=0, activebackground='#0F0F0F', background='#0F0F0F', command = lambda:clear_input())
Clear.place(x=760, y =16)
Run_Lexical=Button(frame_top, width=175, height=35, image=photo_imageLexical, border=0, activebackground='#0F0F0F', background='#0F0F0F', command = lambda:Take_input())
Run_Lexical.place(x=925, y=15)
Run_Semantic=Button(frame_top, width=175, height=35, image=photo_imageSemantic, border=0, activebackground='#0F0F0F', state='disabled', background='#0F0F0F', command = lambda:Run_Syntax())
Run_Semantic.place(x=1139, y =15)


text_area.focus()
root.mainloop()
