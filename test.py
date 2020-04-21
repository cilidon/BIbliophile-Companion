import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
from PIL import Image,ImageTk
from functools import partial

def work(event):
    print("it worked")
    gradient.filename=filedialog.askopenfilenames(initialdir="C:/Users/manda/Desktop",title="select file",filetypes=(("pdf","*.pdf"),("document","*.doc")))

def color_config(widget, color, event):
    widget.configure(foreground=color)

def imgcolor_config(widget, color, event):
    widget.configure(image=color)

root=tk.Tk()
#title
root.title("Bibliophile Companion")

#icon
photo = PhotoImage(file = "book.gif")
root.iconphoto(False, photo)

#menu
w = Menu(root)  
file=Menu(w,tearoff=0)
file.add_command(label="open")
w.add_cascade(label="file",menu=file)
w.add_command(label="edit")
w.add_command(label="faq")

#partioning
p = PanedWindow(root, orient=HORIZONTAL,bg="black")
p.pack(padx=4,pady=3)
f1 = LabelFrame(p, text='BOOKS', width=100, height=600,bg="black",fg="white",bd=0,labelanchor="n")
photo=ImageTk.PhotoImage(Image.open("bookbg.jpg"))
f2 = LabelFrame(p, text='', width=700, height=400,bg="#1D191B",fg="white",bd=0,labelanchor="n")
f4 = LabelFrame(p, text='', width=200, height=600,bg="black",fg="white",bd=0,labelanchor="n")  
f3=LabelFrame(f2,text="", width=700,height=200,bg="#1D191B",fg="white",bd=0,labelanchor="n")
p.add(f1)
p.add(f2)
p.add(f4)
f3.pack(side=BOTTOM)
gradient=Label(f2,height=420,width=696,bg="black")
gradient.pack(fill=BOTH )

#content

#f1
lbl1=Label(f1,text="book 1",takefocus=True,pady=20,bg="black",fg="gray",font="times 24 bold")
lbl1.bind("<Enter>", partial(color_config, lbl1, "#ffffff"))
lbl1.bind("<Leave>", partial(color_config, lbl1, "gray"))
lbl1.grid(row=0)
lbl1.bind("<Button-1>",work)
lbl2=Label(f1,text="book 2",takefocus=True,pady=20,bg="black",fg="gray",font="times 24 bold")
lbl2.bind("<Enter>", partial(color_config, lbl2, "#ffffff"))
lbl2.bind("<Leave>", partial(color_config, lbl2, "gray"))
lbl2.grid(row=1)
lbl2.bind("<Button-1>",work)
lbl3=Label(f1,text="book 3",takefocus=True,pady=20,bg="black",fg="gray",font="times 24 bold")
lbl3.bind("<Enter>", partial(color_config, lbl3, "#ffffff"))
lbl3.bind("<Leave>", partial(color_config, lbl3, "gray"))
lbl3.grid(row=2)
lbl3.bind("<Button-1>",work)
lbl4=tk.Label(f1,text="book 4",takefocus=True,pady=20,cursor='CIRCLE',padx=50,bg="black",fg="gray",font="times 24 bold")
lbl4.bind("<Enter>", partial(color_config, lbl4, "#ffffff"))
lbl4.bind("<Leave>", partial(color_config, lbl4, "gray"))
lbl4.grid(row=3)
lbl4.bind("<Button-1>",work)

#f2
lbl9=Label(gradient,text="drag and drop",takefocus=True,bg="black",fg="gray",font="times 24 bold")
#lbl9.grid(column=0,row=0,padx=10,pady=20)
lbl9.pack(padx=10,pady=100)

addbut_white=ImageTk.PhotoImage(Image.open("addbut_white.png").resize((50,50)))
addbut_gray=ImageTk.PhotoImage(Image.open("addbut_gray.png").resize((50,50)))
lbl8=Label(gradient,image=addbut_gray,takefocus=True,bg="black",fg="gray",font="times 24 bold")
lbl8.bind("<Enter>", partial(imgcolor_config, lbl8, addbut_white))
lbl8.bind("<Leave>", partial(imgcolor_config, lbl8, addbut_gray))
#lbl8.grid(column=1,row=1,padx=10,pady=20)
lbl8.pack(padx=10,pady=10,side=RIGHT )
lbl8.bind("<Button-1>",work)

#f4
qa_white=ImageTk.PhotoImage(Image.open("qa_white.png").resize((60,50)))
qa_gray=ImageTk.PhotoImage(Image.open("qa_gray.png").resize((60,50)))
quiz_gray=ImageTk.PhotoImage(Image.open("quiz_gray.png").resize((50,50)))
quiz_white=ImageTk.PhotoImage(Image.open("quiz_white.png").resize((50,50)))
ppt_white=ImageTk.PhotoImage(Image.open("ppt_white.png").resize((50,50)))
ppt_gray=ImageTk.PhotoImage(Image.open("ppt_gray.png").resize((50,50)))
lbl5=Label(f4,image=qa_gray,takefocus=True,bg="black",fg="gray",font="times 24 bold")
lbl5.bind("<Enter>", partial(imgcolor_config, lbl5, qa_white))
lbl5.bind("<Leave>", partial(imgcolor_config, lbl5, qa_gray))
lbl5.grid(row=0,padx=10,pady=20)
lbl5.bind("<Button-1>",work)
lbl6=Label(f4,image=quiz_gray,takefocus=True,bg="black",fg="gray",font="times 24 bold")
lbl6.bind("<Enter>", partial(imgcolor_config, lbl6, quiz_white))
lbl6.bind("<Leave>", partial(imgcolor_config, lbl6, quiz_gray))
lbl6.grid(row=1,padx=10,pady=20)
lbl6.bind("<Button-1>",work)
lbl7=Label(f4,image=ppt_gray,takefocus=True,bg="black",fg="gray",font="times 24 bold")
lbl7.bind("<Enter>", partial(imgcolor_config, lbl7, ppt_white))
lbl7.bind("<Leave>", partial(imgcolor_config, lbl7, ppt_gray))
lbl7.grid(row=2,padx=10,pady=20)


#adjustment
"""Frame1.rowconfigure(0,weight=1)
Frame1.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)
"""

root.configure(menu=w)
root.mainloop()
