
from tkinter import *
from tkinter import ttk
from math import *
from tkinter import messagebox
from tkinter.font import BOLD
from PIL import ImageTk,Image
###Taking object From Tkinter############################33
Window=Tk()
Window.title("Numerical Analysis Calculator")
Window.geometry('1000x700')###TAzbet 7agm
Window.config(bg='#050100')###Lon el Saf7a
Window.resizable(0,0)
f = ("Helvetica",11,'bold')
####COMMANDS############################################
def nextPage():
    #Window.destroy()
    import BisectionMethod
   

def nextPageX():
    Window.destroy()
    import FalsePs
def nextPageSS():
    Window.destroy()
    import SecantMethod
def nextPageSimp():
    Window.destroy()
    import SimpleFixedPoint
def nextPageN():
    Window.destroy()
    import Newton
def nextGauss():
    Window.destroy()
    import GaussElimination
def nextCramer():
    Window.destroy()
    import Cramer 
def nextLUDEC():
    Window.destroy()
    import LuDecomposition
########################################################################GUI#############################33

Frame1=Frame(Window,bg='#EEEDEC',width='300',height='200')
Frame1.pack(side=TOP,padx='20',pady='20')
LabelTitle=Label(Frame1,bg='#EEEDEC',text='Numerical Analysis Calculator',fg='red',width='300',font=('Helvetica', 16, 'bold'))
LabelTitle.pack(padx='10',pady='10')
Fra=Frame(Window,bg='#EEEDEC',width='300',height='700')
Fra.pack(padx='100',pady='100')

LabelFChoose=Label(Fra,bg='#EEEDEC',text='Choose a Method ',fg='red',font=('Helvetica', 14, 'bold')).pack(side=TOP,padx='10',pady='10')
BisectButt=Button(Fra,bg='#EEEDEC',width='50',text='Bisection Method',command=nextPage,font=f).pack(padx='3',pady='3')
FalswButt=Button(Fra,bg='#EEEDEC',width='50',text='False Position Method',command=nextPageX,font=f).pack(padx='3',pady='3')
SimpleButton=Button(Fra,bg='#EEEDEC',width='50',text='Simple Fixed Point',font=f,command=nextPageSimp).pack(padx='3',pady='3')
SecantButton=Button(Fra,bg='#EEEDEC',width='50',text='Secant Method',font=f,command=nextPageSS).pack(padx='3',pady='3')
NewtonButton=Button(Fra,bg='#EEEDEC',width='50',text='Newton Method',font=f,command=nextPageN).pack(padx='3',pady='3')
GaussButton=Button(Fra,bg='#EEEDEC',width='50',text='Gauss Elimination',font=f,command=nextGauss).pack(padx='3',pady='3')
LUButton=Button(Fra,bg='#EEEDEC',width='50',text='LU Decomposition',font=f,command=nextLUDEC).pack(padx='3',pady='3')
CramerButton=Button(Fra,bg='#EEEDEC',width='50',text='Cramer Rule',font=f,command=nextCramer).pack(padx='1',pady='1')
Window.mainloop()