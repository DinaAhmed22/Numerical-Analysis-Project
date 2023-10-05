from tkinter import *
from tkinter import ttk
from math import *
from tkinter import messagebox
Window=Tk()
Window.title("Simple Fixed Point Method")
Window.geometry('1000x700')
Window.config(bg='#050100')
f = ("Helvetica",9,'bold')
def get_Func(x):#function to get Epson Mn Entry lama user yd5l Function
    f=str(eval(entry.get()))#eval De  heya  Built in Function el hata5od Math Equation mn user 
    return f
def get_Xnode():#function to get x0 Mn Entry lama user yd5l Xnode
    Xnode=float(XnodeEntry.get())
    return Xnode
def get_Epson(): #function to get Epson Mn Entry lama user yd5l eps
    EPS=float(EpsEntry.get())
    return EPS

#######################Main Function #################################
def SimpleFixedP():
    X0=get_Xnode()#Get Xnode value from user
    Ep=get_Epson()#Get Epson value from user
    XiP1=0.0#intialize Xiplus1=0.0
    xi=0.0#intialize Xi=0.0
    Er_=0.0#intialize Error=0.0
    for i in range(100):#range till 100(Maximum)
        

        xi=X0 ##Xnode will be stored in new variable xi
        XiP1=get_Func(X0) #Xiplus1 will be equal the substituiton in Function of X0
        XIP1F=float(XiP1) #Converting XiPlus 1 to float

        #if i==0:#Iam Filling Table with insert Function (Synatx Tablename.insert())
        #iter.insert(parent='', index='end', iid=i, text='',values=(i,xi,XIP1F,Er_,' '))
        #else:
        iter.insert(parent='', index='end', iid=i, text='',values=(i,xi,XIP1F,Er_))
        
        if Er_>Ep or i==0:##if Error is greater than epson or iteration ==0 wil do the following
            Er_ = abs((XIP1F - xi) /XIP1F) * 100 #Calculate Error
            X0=XIP1F #XIP1f will be stored in X0
        
        else: ##Else will break loop
            break
    ResultRoot['text']=f"The Root is :{X0} "
    return xi
 

#######GUI Built in in Tkinter###############
Frame1=Frame(Window,bg='#EEEDEC',width='300',height='200')
Frame1.pack(side=TOP,padx='20',pady='20')
LabelTitle=Label(Frame1,bg='#EEEDEC',text='Simple Fixed Point Method',fg='red',width='300',font=('Helvetica', 16, 'bold')).pack(padx='20',pady='20')
XnodeL=Label(Window,text=' X0',bg='#050100', fg='red',font=('Helvetica', 11, 'bold')).pack(padx='10')
XnodeEntry=Entry(Window,width='30',borderwidth=5,justify=CENTER)
XnodeEntry.pack(padx='10',pady='10')
EPSL=Label(Window,text=' Epson',bg='#050100', fg='red',font=('Helvetica', 11, 'bold')).pack(padx='10')
EpsEntry=Entry(Window,width='30',borderwidth=5,justify=CENTER)
EpsEntry.pack(padx='10',pady='10')
f=Label(Window, text="f(x)[Simplified]",bg='#050100',fg='red',font=('Helvetica', 11, 'bold')).pack()
entry = Entry(Window,width='30',borderwidth=5,justify=CENTER)
entry.pack(padx='10',pady='10')
ResultRoot=Label(Window,text=' ',bg='#050100',fg='red')
ResultRoot.pack()

####Table Built in in Tkinter#####################
iter=ttk.Treeview(Window,columns=(1,2,3,4),show='headings',height=8)
iter.pack()
iter.column("1",anchor=CENTER, stretch=NO, width=100)
iter.heading(1,text='i',anchor=CENTER)
iter.column("2",anchor=CENTER, stretch=NO, width=100)
iter.heading(2,text='Xi',anchor=CENTER)
iter.column("3",anchor=CENTER, stretch=NO, width=100)
iter.heading(3,text='f(Xi)',anchor=CENTER)
iter.column("4",anchor=CENTER, stretch=NO, width=100)
iter.heading(4,text='Error%',anchor=CENTER)
ButtonRes=Button(Window,text='Determine Root',fg='red',font=('Helvetica', 11, 'bold'),command=SimpleFixedP).pack(padx='5',pady='5')#pady we padx ab3ad command bktbha 3shan ynfx function lama bados button(like Java)
style=ttk.Style()
style.theme_use("clam")
style.configure("Treeview",foreground='red')
style.configure('Treeview.Heading', background="red3")
style.map("Treeview",background=[('selected','red')])
#####################################################################
Window.mainloop()