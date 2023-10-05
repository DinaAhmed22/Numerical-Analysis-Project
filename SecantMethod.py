from tkinter import *
from tkinter import ttk
from math import *
from tkinter import messagebox
Window=Tk()
Window.title("False Position Method")
Window.geometry('1000x600')
Window.config(bg='#050100')
f = ("Helvetica",9,'bold')

def get_Xi():
    Xi=float(XiE.get())
    return Xi
def get_Xm():
    Xm=float(XMinEntry.get())
    return Xm
def get_Epson():
    EPS=float(EpsEntry.get())
    return EPS

def get_Function(x):
    Func=str(eval(entry.get()))
    return Func
##############Main Funtion#######################
def SecantMethod():
    
    Er_=0.0 #intialize Error=0.0
    xiPlus1 = 0.0 #intialize xiplus1 0.0
    xi=get_Xi() #get value of Xi
    XiM1=get_Xm() # get value of XiMinus1
    Ep=get_Epson() #get value of epson
    
    for i in range(100):#:#range till 100(Maximum)
            XIF=get_Function(xi)
            XIFF=float(XIF)
            XIM=get_Function(XiM1)
            XIMF=float(XIM)
            xiPlus1 = xi - (XIFF * (XiM1 - xi)) / (XIMF - XIFF) #xiplus 1 rule in Secant method
            iter.insert(parent='', index='end', iid=i, text='',values=(i,XiM1,XIMF,xi,XIFF,Er_))

            if Er_>Ep or i==0:##if Error is greater than epson or iteration ==0 wil do the following
                Er_ = abs((xiPlus1 - xi) / xiPlus1) * 100
                XiM1 = xi
                xi = xiPlus1
            else:#Else will break loop
                break
    ResultRoot['text']=f"The Root is :{xi} "
    return xi
    
#################GUI#######################################
Frame1=Frame(Window,bg='#EEEDEC',width='300',height='200')
Frame1.pack(side=TOP,padx='20',pady='20')
LabelTitle=Label(Frame1,bg='#EEEDEC',text='Secant Method',fg='red',width='300',font=('Helvetica', 16, 'bold')).pack(padx='20',pady='20')
XiLAbel=Label(Window,text=' Xi',bg='#050100', fg='red',font=('Helvetica', 11, 'bold')).pack(padx='10')
XiE=Entry(Window,width='30',borderwidth=5,justify=CENTER)
XiE.pack(padx='3',pady='3')
XMinLAbel=Label(Window,text=' Xi-1',bg='#050100', fg='red',font=('Helvetica', 11, 'bold')).pack(padx='10')
XMinEntry=Entry(Window,width='30',borderwidth=5,justify=CENTER)
XMinEntry.pack(padx='10',pady='10')
EPSL=Label(Window,text=' Epson',bg='#050100', fg='red',font=('Helvetica', 11, 'bold')).pack(padx='10')
EpsEntry=Entry(Window,width='30',borderwidth=5,justify=CENTER)
EpsEntry.pack(padx='10',pady='10')
Label(Window, text="f(x)",bg='#050100',fg='red',font=('Helvetica', 11, 'bold')).pack()
entry = Entry(Window,borderwidth=5,width='30',justify=CENTER)#Entry BTa3t f(x)
entry.pack(padx='10',pady='10')
ResultRoot=Label(Window,text=' ',bg='#050100',fg='red')
ResultRoot.pack()
##############Table##########################################################
iter=ttk.Treeview(Window,columns=(1,2,3,4,5,6),show='headings',height=8)
iter.pack()
iter.column("1",anchor=CENTER, stretch=NO, width=100)
iter.heading(1,text='i',anchor=CENTER)
iter.column("2",anchor=CENTER, stretch=NO, width=100)
iter.heading(2,text='Xi-1',anchor=CENTER)
iter.column("3",anchor=CENTER, stretch=NO, width=100)
iter.heading(3,text='f(Xi-1)',anchor=CENTER)
iter.column("4",anchor=CENTER, stretch=NO, width=100)
iter.heading(4,text='Xi',anchor=CENTER)
iter.column("5",anchor=CENTER, stretch=NO, width=100)
iter.heading(5,text='f(Xi)',anchor=CENTER)
iter.column("6",anchor=CENTER, stretch=NO, width=100)
iter.heading(6,text='Error',anchor=CENTER)
ButtonRes=Button(Window,text='Determine Root',fg='red',font=('Helvetica', 11, 'bold'),command=SecantMethod).pack(padx='5',pady='5')
style=ttk.Style()
style.theme_use("clam")
style.configure("Treeview",foreground='red')
style.configure('Treeview.Heading', background="red3")
style.map("Treeview",background=[('selected','red')])
Window.mainloop()