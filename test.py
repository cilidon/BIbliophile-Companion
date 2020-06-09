import json
import random
import tkinter as tk
from tkinter import *

global questi
global opti
questi=1.0
opti=0

root=tk.Tk()

p= PanedWindow(root, orient=HORIZONTAL,bg="black")
p.grid(padx=4,pady=3)
lf= LabelFrame(p,height=700,width=600, text='',bg="#1D191B",fg="white",bd=0,labelanchor="n")
lf.grid()

lbl9=Text(lf,takefocus=True,height=700,width=600,bg="black",fg="gray",font="times 12 bold",bd=2)
lbl9.grid(padx=10,pady=10)
lbl9.grid_propagate(False)

with open('DB/quiz_output.txt') as f:
  data = json.load(f)



ran=range(len(data))
print(ran)
for i in ran:
    '''
    lbl9.insert(questi,data[i]['question'])
    #lbl9.configure(text=data[i]['question'])
    
    if(data[i]['similar_words']):
        for j in range(len(data[i]['similar_words'])):
            #print(data[i]['similar_words'][j])
            ran=random.randrange(1,5)
            #print(ran)
            
            if(ran==1):
                #print(data[i]['similar_words'][j])
                Radiobutton(lbl9,text=data[i]['answer'],bg="black").grid(row=opti,column=0)
                Radiobutton(lbl9,text=data[i]['similar_words'][j],bg="black").grid(row=opti,column=1)
                Radiobutton(lbl9,text=data[i]['similar_words'][j],bg="black").grid(row=opti+1,column=0)
                Radiobutton(lbl9,text=data[i]['similar_words'][j],bg="black").grid(row=opti+1,column=1)
                questi=+2.0
                opti=+2
            elif(ran==2):
                #print(data[i]['similar_words'][j])
                Radiobutton(lbl9,text=data[i]['similar_words'][j],bg="black").grid(row=opti,column=0)
                Radiobutton(lbl9,text=data[i]['answer'],bg="black").grid(row=opti,column=1)
                Radiobutton(lbl9,text=data[i]['similar_words'][j],bg="black").grid(row=opti+1,column=0)
                Radiobutton(lbl9,text=data[i]['similar_words'][j],bg="black").grid(row=opti+1,column=1)
                questi+2.0
                opti=+2
            elif(ran==3):
               # print(data[i]['similar_words'][j])
                Radiobutton(lbl9,text=data[i]['similar_words'][j],bg="black").grid(row=opti,column=0)
                Radiobutton(lbl9,text=data[i]['similar_words'][j],bg="black").grid(row=opti,column=1)
                Radiobutton(lbl9,text=data[i]['answer'],bg="black").grid(row=opti+1,column=0)
                Radiobutton(lbl9,text=data[i]['similar_words'][j],bg="black").grid(row=opti+1,column=1)
                questi+2.0
                opti=+2
            else:
                #print(data[i]['similar_words'][j])
                Radiobutton(lbl9,text=data[i]['similar_words'][j],bg="black").grid(row=opti,column=0)
                Radiobutton(lbl9,text=data[i]['similar_words'][j],bg="black").grid(row=opti,column=1)
                Radiobutton(lbl9,text=data[i]['similar_words'][j],bg="black").grid(row=opti+1,column=0)
                Radiobutton(lbl9,text=data[i]['answer'],bg="black").grid(row=opti+1,column=1)
                questi+2.0
                opti=+2
               
    else:
        #print("fill in the blanck")
        Entry(lbl9).grid()

    '''
    
root.configure(height=500,width=400)
root.mainloop()
