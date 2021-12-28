import tkinter as tk

from tkinter import ttk
from tkinter import *

import lexer


#creating the window
root= tk.Tk()
root.geometry('1366x768')
root.resizable(FALSE, FALSE)
root.configure(bg='#171717')
root.title('Nervethon')

#Frame Top
frame_top=Frame(root,width=1366,height=70, background='#0F0F0F')
frame_top.grid(row=0, column=0, columnspan=2)

#Photos
photo_imageClear=PhotoImage(file='Clear.png')
photo_imageSemantic=PhotoImage(file='Semantic.png')
photo_imageLexical=PhotoImage(file='Lexical.png')
photo_imageNervethon=PhotoImage(file='Nervy.png')

#Logo
canvasLogo=Canvas(frame_top, width=270, height=55, borderwidth=0, highlightbackground='#0F0F0F', background='#0F0F0F')
canvasLogo.create_image(140,29, image=photo_imageNervethon)
canvasLogo.place(x=20,y=5)

#Frame 1 Top left size
frame1=Frame(root, width=633, height=350, highlightbackground='gray', bg='#121212', highlightcolor='gray', highlightthickness=1)
frame1.place(x=35,y=100)

#Frame 1 Style
style=ttk.Style(frame1)
style.theme_use('alt')
style.configure("Vertical.TScrollbar", troughcolor="#0F0F0F", highlightcolor="#313537", bordercolor="white", arrowcolor="blue")

#Scrollbar and Text area
scrollbar=ttk.Scrollbar(frame1, orient='vertical')
text_area = Text(frame1, bg='#121212', width = 54, height = 21, font = ("Courier",15), insertbackground='white', fg="White", yscrollcommand=scrollbar.set)
scrollbar.config(command=text_area.yview)
scrollbar.pack(side=RIGHT, fill=Y)
text_area.pack(side="left")


#TRIAL INPUT AND OUTPUT
def Take_input():
    Output.configure(state='normal')
    Errors.configure(state='normal')
    OutputTok.configure(state='normal')
    Output.delete(1.0,END)#How to reset text area
    Errors.delete(1.0,END)#How to reset text area
    OutputTok.delete(1.0,END)
    INPUT = text_area.get("1.0", "end-1c")
    run_code = lexer.run(INPUT)
    check_Error = False
    for result in run_code:
        if result.hasError != "":
            #Frame 2 - Error
            check_Error = True
            Errors.configure(state='normal')
            Errors.insert(END, '\' ')
            Errors.insert(END, result.value)
            Errors.insert(END, ' \' → ')
            Errors.insert(END, result.hasError)
            Errors.insert(END, ' on Line ')
            Errors.insert(END, result.line)
            Errors.insert(END, '\n')
            Output.configure(state='disabled')
            Errors.configure(state='disabled')
        else:
            #Frame 3 - Output
            Output.configure(state='normal')
            OutputTok.configure(state='normal')
            if len(str(result.value)) > 15:
                Output.insert(END, '  ')
                count_letter = 0
                word_list = list(str(result.value))
                output_word = ""
                while count_letter <= 15:
                    char_letter = word_list[count_letter]
                    output_word = output_word + char_letter
                    count_letter += 1
                Output.insert(END, output_word)
                Output.insert(END, '...')
                Output.insert(END, '\n')
            else:
                Output.insert(END, '  ')
                Output.insert(END, result.value)
                Output.insert(END, '\n')
            OutputTok.insert(END, '  ')
            OutputTok.insert(END, result.type)
            OutputTok.insert(END, '\n')
            Output.configure(state='disabled')
            OutputTok.configure(state='disabled')
            Errors.configure(state='disabled')
    if check_Error == False:
        Errors.configure(state='normal')
        Errors.insert(END, 'No Error/s Found')
        Output.configure(state='disabled')
        
#Frame 2 - Errors
frame2=Frame(root, width=633, height=100, highlightbackground='gray', bg='#121212', highlightcolor='gray', highlightthickness=1)
frame2.place(x=35,y=615)

scrollbar2=ttk.Scrollbar(frame2, orient='vertical')
Errors = Text(frame2, width = 54, height =6, font = ("Courier",15), bg = "#121212", fg="White", highlightthickness=0, borderwidth=0, state='disabled',  yscrollcommand=scrollbar2.set)
scrollbar2.config(command=Errors.yview)
scrollbar2.pack(side=RIGHT, fill=Y)
Errors.pack(side="left")

#Frame 3 - Output Lex
frame3=Frame(root, width=520, height=660, highlightbackground='gray', bg='#121212', highlightcolor='gray', highlightthickness=1)
frame3.place(x=725, y=130)
#Frame 4 - Output Token
frame4=Frame(root, width=520, height=660, highlightbackground='gray', bg='#121212', highlightcolor='gray', highlightthickness=1)
frame4.place(x=1045, y=130)


#OUTPUT Lex TEXT AREA
scrollbar3=ttk.Scrollbar(frame3, orient='vertical')
Output = Text(frame3, width = 23, height =28, font = ("Courier",15), bg = "#121212", fg="White", highlightthickness=0, borderwidth=0, state='disabled',  yscrollcommand=scrollbar3.set)
scrollbar3.config(command=Output.yview)
scrollbar3.pack(side=RIGHT, fill=Y)
Output.pack(side="left")

#OUTPUT Lex TEXT AREA
scrollbar4=ttk.Scrollbar(frame4, orient='vertical')
OutputTok = Text(frame4, width = 23, height =28, font = ("Courier",15), bg = "#121212", fg="White", highlightthickness=0, borderwidth=0, state='disabled',  yscrollcommand=scrollbar4.set)
scrollbar4.config(command=OutputTok.yview)
scrollbar4.pack(side=RIGHT, fill=Y)
OutputTok.pack(side="left")

lblLex=Label(root,text="Lexeme", font = ("Nunito",14), fg='white',bg='#171717')
lblLex.place(x=825,y=98)
lblTok=Label(root,text="Token" , font = ("Nunito",14), fg='white',bg='#171717')
lblTok.place(x=1150,y=98) 
lblErr=Label(root,text="Errors", font = ("Nunito",14), fg='white',bg='#171717')
lblErr.place(x=40,y=580)

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
Run_Semantic=Button(frame_top, width=175, height=35, image=photo_imageSemantic, border=0, activebackground='#0F0F0F', background='#0F0F0F', state='disabled')
Run_Semantic.place(x=1139, y =15)


text_area.focus()
root.mainloop()
