from tkinter import *
import os

# root =Tk()

# # size of box widthxheight
# root.geometry("1000x1000")
# root.minsize(400,400)
# root.maxsize(400,400)

# # ADD Text
# text =Label(text="This is my first GUI")
# text.pack()

# ------------------------------------try--------------------------------
window=Tk()

window.title("TSmart Bot ~ rohan_r.kumar")
# size of box widthxheight
window.geometry('550x200')

text =Label(text="This is Smart Bot")
text.pack

def meet():
    os.system('meetbot.py')
def whats():
    os.system('bot.py')

button1= Button(window, text="Create Link", bg="yellow", fg="black",command=meet).place(x=150, y=80)
# button1.grid()
# button1.pack()
clear= Button(window, text="Send Link", bg="green", fg="white",command=whats).place(x=320,y=80)
# clear.grid()
# clear.pack()

window.mainloop()
# b = Button(root, text="Enter", width=10, height=2, command=button1)
# c = Button(root, text="Clear", width=10, height=2, command=clear)
# b.grid(row=0,column=0, sticky=W)
# c.grid(row=0,column=1, sticky=W)

# textframe = Frame(root)
# textframe.grid(in_=root, row=1, column=0, columnspan=3, sticky=NSEW)
# root.columnconfigure(0, weight=1)
# root.rowconfigure(1, weight=1)

# text = Text(root, width=35, height=15)
# scrollbar = Scrollbar(root)
# scrollbar.config(command=text.yview)
# text.config(yscrollcommand=scrollbar.set)
# scrollbar.pack(in_=textframe, side=RIGHT, fill=Y)
# text.pack(in_=textframe, side=LEFT, fill=BOTH, expand=True)
# _-------------------------------------end-----------------------------

# # ADD IMAGE 
# photo =PhotoImage(file="1.png")
# label=Label(image=photo)
# label.pack()

# root.mainloop()
