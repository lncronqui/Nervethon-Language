import tkinter as tk

from tkinter import ttk
from tkinter import *

import lexer


#creating the window
root= tk.Tk()
root.resizable(FALSE, FALSE)
root.configure(bg='#171717')
root.title('Nervethon')

#Frame Top
frame_top=Frame(root,width=1356,height=70, background='#0F0F0F')
frame_top.grid(row=0, column=0, columnspan=2)

#Photos
photo_imageSemantic=PhotoImage(file='Semantic.png')
photo_imageLexical=PhotoImage(file='Lexical.png')
photo_imageNervethon=PhotoImage(file='Nervy.png')

#Logo
canvasLogo=Canvas(frame_top, width=270, height=55, borderwidth=0, highlightbackground='#0F0F0F', background='#0F0F0F')
canvasLogo.create_image(140,29, image=photo_imageNervethon)
canvasLogo.place(x=20,y=5)


#Frame 1 Top left size
frame1=Frame(root, width=633, height=400, highlightbackground='#ffffff', highlightthickness=1)
frame1.grid(row=2, column=0,padx=25, pady=25)

#Frame 1 Style
style=ttk.Style(frame1)
style.theme_use('alt')
style.configure("Vertical.TScrollbar", troughcolor="#0F0F0F", highlightcolor="#313537", bordercolor="white", arrowcolor="blue")

#Scrollbar and Text area
scrollbar=ttk.Scrollbar(frame1, orient='vertical')
text_area = Text(frame1, bg='#121212', width = 66, height = 23, font = ("Times New Roman",15), fg="White", yscrollcommand=scrollbar.set)
scrollbar.config(command=text_area.yview)
scrollbar.pack(side=RIGHT, fill=Y)
text_area.pack(side="left")


#TRIAL INPUT AND OUTPUT
def Take_input():
    INPUT = text_area.get("1.0", "end-1c")
    for result in lexer.run(INPUT):
        if result.hasError == False:
            #Frame 3 - Output
            None
        else:
            #Frame 2 - Output
            None
    
    if(INPUT == "120"):
        Output.configure(state='normal')
        Output.delete(1.0,END)
        Output.insert(END, 'Correct')
        Output.configure(state='disabled')
    else:
        Errors.configure(state='normal')
        Errors.delete(1.0,END)
        Errors.insert(END, "Wrong answer")
        Errors.configure(state='disabled')
        

        
#Frame 2 - Errors
frame2=Frame(root, width=633, height=100, highlightbackground='#ffffff', bg='#121212', highlightthickness=1)
frame2.grid(row=3, column=0, padx=25, pady=25, ipadx=25, ipady=25)

Errors = Text(frame2, width = 50, height = 30, font = ("Times New Roman",15), bg = "#121212", fg="White", highlightthickness=0, borderwidth=0)

#Frame 3 - Output
frame3=Frame(root, width=520, height=660, highlightbackground='#ffffff', background='#121212', highlightthickness=1)
frame3.grid(row=1, column=1, rowspan = 6, columnspan = 2, padx=25, pady=25, ipadx=25, ipady=25)

scrollbar=ttk.Scrollbar(frame3, orient='vertical')
scrollbar.config(command=text_area.yview)
scrollbar.pack(side=RIGHT, fill=Y)
text_area.pack(side="left")


#OUTPUT TEXT AREA
Output = Text(frame3, width = 50, height = 30, font = ("Times New Roman",15), bg = "#121212", fg="White", highlightthickness=0, borderwidth=0)


#Buttons or inside of Frame_Top
Run_Button=Button(frame_top, width=175, height=35, image=photo_imageLexical, border=0,background='#0F0F0F', command = lambda:Take_input())
Run_Button.place(x=925, y=15)
Run_Button1=Button(frame_top, width=175, height=35, image=photo_imageSemantic, border=0,background='#0F0F0F', state='disabled')
Run_Button1.place(x=1139, y =15)

Errors.pack()
Output.pack()
text_area.focus()
root.mainloop()