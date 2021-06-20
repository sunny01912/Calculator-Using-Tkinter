from tkinter import *
from math import *
def click(event):
    global scvalue
    text=event.widget.cget('text')
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(scvalue.get())
            except:
                value="Invalid Input"
        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()



root=Tk()
root.wm_iconbitmap("cc.jpg")
root.geometry("450x700")
root.title("Calculator")

scvalue=StringVar()
screen=Entry(root,font="lucida 40 bold",textvariable=scvalue,state='disabled')
screen.pack(fill=X,padx=10,pady=5,ipadx=8)

f=Frame(root,background="grey")
f.pack()
for i in range(9,6,-1):
    b=Button(f,text=f"{i}",font="lucida 30 bold",padx=11)
    b.bind("<Button-1>",click)
    b.pack(side=LEFT,padx=10,pady=10)
f=Frame(root,background="grey")
f.pack()
for i in range(6,3,-1):
    b=Button(f,text=f"{i}",font="lucida 30 bold",padx=11)
    b.bind("<Button-1>",click)
    b.pack(side=LEFT,padx=10,pady=10)
f=Frame(root,background="grey")
f.pack()
for i in range(3,0,-1):
    b=Button(f,text=f"{i}",font="lucida 30 bold",padx=11)
    b.bind("<Button-1>",click)
    b.pack(side=LEFT,padx=10,pady=10)
f=Frame(root,background="grey")
f.pack()
b=Button(f,text="0",font="lucida 30 bold",padx=9.5)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=10,pady=10)
b=Button(f,text="C",font="lucida 30 bold",padx=9)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=10,pady=10)
b=Button(f,text="=",font="lucida 30 bold",padx=9.5)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=10,pady=10)


f=Frame(root,background="grey")
f.pack()
b=Button(f,text="+",font="lucida 30 bold",padx=13)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=10,pady=10)
b=Button(f,text="-",font="lucida 30 bold",padx=13)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=10,pady=10)
b=Button(f,text="*",font="lucida 30 bold",padx=13)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=10,pady=10)


f=Frame(root,background="grey")
f.pack()
b=Button(f,text="/",font="lucida 30 bold",padx=15)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=10,pady=10)

b=Button(f,text="%",font="lucida 25 bold",padx=15,pady=10)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=10,pady=10)
b=Button(f,text=".",font="lucida 30 bold",padx=15,pady=0)
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=10,pady=10)













root.mainloop()