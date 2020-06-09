import json
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
from PIL import Image,ImageTk
from functools import partial
from tkinter import messagebox
import qa_main
import topic_find
#import wikitrivia.scripts.wikitrivia
import summ
import json
import random
qu=[]

with open('DB/quiz_output.txt') as f:
  data = json.load(f)


for i in data:
    qu.append(i['similar_words'])

print(qu)

root=tk.Tk()
root.geometry("1100x600")
root.configure(bg="white")
#root.resizable(0,0)
screenw=root.winfo_screenwidth()
screenh=root.winfo_screenheight()

#title
root.title("Bibliophile Companion")

#icon
photo = PhotoImage(file = "icons/book.gif")
root.iconphoto(False, photo)

#menu
w = Menu(root)
w.configure(bg="black",fg="gray",bd=1)  
file=Menu(w,tearoff=0)
file.add_command(label="open")
w.add_cascade(label="file",menu=file)
w.add_command(label="edit")
w.add_command(label="faq")

#partioning
p = PanedWindow(root,width=1100,height=600, orient=HORIZONTAL,bg="black",bd=2)
p.pack(padx=4,pady=3,expand=1,fill=BOTH)
#p.pack_propagate(False)

f1 = LabelFrame(p, text='',height=600,width=70,bg="yellow",fg="white",bd=0,labelanchor="n")
f4 = LabelFrame(p, text='',height=600,width=140,bg="red",fg="white",bd=0,labelanchor="n")  
f2 = LabelFrame(p, text='',height=600,width=950,bg="blue",fg="white",bd=0)


Grid.rowconfigure(p, 0, weight=1)
#Grid.columnconfigure(p, 0, weight=1)
#Grid.columnconfigure(p, 1, weight=1)
Grid.columnconfigure(p, 2, weight=1)
f1.grid(column=0,row=0,sticky='N'+'S'+'W')

f4.grid(column=1,row=0,sticky='N'+'S'+'W'+'E')

f2.grid(column=2,row=0,sticky='N'+'S'+'W'+'E')

f4.grid_remove()

gradient=LabelFrame(f2,height=500,width=950,bg="gray")
f3=LabelFrame(f2,text="",height=100,width=950,bg="white",fg="white",bd=0,labelanchor="n")
Grid.rowconfigure(f2, 0, weight=3)
Grid.rowconfigure(f2, 1, weight=1)
Grid.columnconfigure(f2, 0, weight=1)
gradient.grid(row=0,column=0,sticky='N'+'S'+'W'+'E')
f3.grid(row=1,column=0,sticky='N'+'S'+'W'+'E')
gradient.grid_propagate(False)

lbl9=Text(gradient,bg="red",fg="gray",height=500,width=950,font="times 24 bold",spacing1=1,wrap=WORD,bd=2)
#lbl9.insert('1.0',"drag and drop")
Grid.rowconfigure(gradient, 0, weight=1)
Grid.columnconfigure(gradient, 0, weight=1)
lbl9.grid(column=0,row=0)
#lbl9.pack(padx=10,pady=10)

radiovar=StringVar(value="1")

r1=Radiobutton(lbl9,text="12",variable = radiovar,value=1,bg="black",fg="white",selectcolor="black",activebackground="black",activeforeground="white")
r2=Radiobutton(lbl9,text="23",variable = radiovar,value=2,bg="black",fg="white",selectcolor="black",activebackground="black",activeforeground="white")
r3=Radiobutton(lbl9,text="34",variable = radiovar,value=3,bg="black",fg="white",selectcolor="black",activebackground="black",activeforeground="white")
r4=Radiobutton(lbl9,text="45",variable = radiovar,value=4,bg="black",fg="white",selectcolor="black",activebackground="black",activeforeground="white")
r1.configure(text="amount")
r1.pack()
r2.pack()
r3.pack()
r4.pack()
root.configure(menu=w)
root.mainloop()

'''
    q=qasea.get()
    lbl9.insert(END,"\n"+q)
    qasea.delete(0,END)
'''
