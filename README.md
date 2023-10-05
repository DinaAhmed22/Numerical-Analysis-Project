# Numerical-Analysis-Project
#Main Window
from tkinter import *
from tkinter import ttk
from math import *
from tkinter import messagebox
from tkinter.font import BOLD
from PIL import ImageTk,Image
###Taking object From Tkinter############################33
Window=Tk()
Window.title("Numerical Analysis Calculator")
Window.geometry('1000x700')#TAzbet 7agm
Window.config(bg='#050100')###Lon el Saf7a
#####################################################
def nextPage():
    Window.destroy()
    import NumericALPRO
def RulesPage():
    Window.destroy()
    import NumericalRules

f = ("Helvetica",11,'bold')
Frame1=Frame(Window,bg='#EEEDEC',width='300',height='200')
Frame1.pack(side=TOP,padx='20',pady='20')
LabelTitle=Label(Frame1,bg='#EEEDEC',text='Numerical Analysis Calculator',fg='red',width='300',font=('Helvetica', 16, 'bold'))
LabelTitle.pack(padx='10',pady='10')
#Load the image
img= Image.open("hh.png")
#Convert To photoimage
tkimage= ImageTk.PhotoImage(img)
#Display the Image
label=Label(Window,image=tkimage)
label.pack(padx='15',pady='15')
MethodsPage=Button(Window,bg='#EEEDEC',width='50',text='Go',command=nextPage,fg='red',font=f).pack(side=BOTTOM,padx='50',pady='50')
menubar = Menu(Window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Numerical Analysis Rules",command=RulesPage)
filemenu.add_separator()

menubar.add_cascade(label="File", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)
Window.config(menu=menubar)
Window.mainloop()
