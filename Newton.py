from tkinter import *
from tkinter import ttk
from math import *
from tkinter import messagebox


Window=Tk()
Window.title("Newton Method")
Window.geometry('1000x700')
Window.config(bg='#050100')
f = ("Helvetica",9,'bold')
#############Getters#####################################################

def get_Xnode():#function to get x0 Mn Entry lama user yd5l Xnode
    Xnode=float(XnodeEntry.get())
    return Xnode
def get_Function(x):
    Func=str(eval(entry.get()))
    return Func
def get_Fdash(x):
    Func=str(eval(entry2.get()))
    return Func

def get_Epson():
    EPS=float(EpsEntry.get())
    return EPS


def prevPage():
    Window.destroy()
    import NumericALPRO
########################################################
#######Main Function###########################################
def newton():
    xo=get_Xnode() #Get Value of Xnode
    e=get_Epson() #Get Value of Epson
    xip1=0.0 #Intialize Xiplus by
    xi=0.0#Intialize Xi by
    er=0.0#Intialize Error by
    for i in range(100):#:#range till 100(Maximum)
        xi=xo #xo will be stored in xi
        FDash=get_Fdash(xi) #Substitue in derivative of Xi
        FDashFi=float(FDash) #Converting substituiton of derivative of Xi to float
        FX=get_Function(xi)#Substitue in Function of Xi
        FXI=float(FX)#Converting substituiton of Function of Xi to float
        c=FXI/FDashFi 
        xip1=xi-c #rule of new xi(XiPlus 1) in Newton Method
        ##Filling table
        iter.insert(parent='', index='end', iid=i, text='',values=(i,xo,FX,FDash,er))

        if er>e or i ==0:##if Error is greater than epson or iteration ==0 wil do the following
            er=abs((xip1-xi)/xip1)*100
            xo=xip1
          

        else: #else will break loop
            break
        ResultRoot['text']=f"The Root is :{xo} "

    return xo
    
	





#######################################################
Frame1=Frame(Window,bg='#EEEDEC',width='300',height='200')
Frame1.pack(side=TOP,padx='20',pady='20')
LabelTitle=Label(Frame1,bg='#EEEDEC',text='Newton Method',fg='red',width='300',font=('Helvetica', 16, 'bold')).pack(padx='20',pady='20')
XnodeL=Label(Window,text=' X0',bg='#050100', fg='red',font=('Helvetica', 11, 'bold')).pack(padx='10')
XnodeEntry=Entry(Window,width='30',borderwidth=5,justify=CENTER)
XnodeEntry.pack(padx='10',pady='10')
EPSL=Label(Window,text=' Epson',bg='#050100', fg='red',font=('Helvetica', 11, 'bold')).pack(padx='10')
EpsEntry=Entry(Window,width='30',borderwidth=5,justify=CENTER)
EpsEntry.pack(padx='10',pady='10')
f=Label(Window, text="f(x)",bg='#050100',fg='red',font=('Helvetica', 11, 'bold')).pack()
entry = Entry(Window,width='30',borderwidth=5,justify=CENTER)
entry.pack(padx='3',pady='3')
fD=Label(Window, text="F Dash (x)",bg='#050100',fg='red',font=('Helvetica', 11, 'bold')).pack()
entry2 = Entry(Window,width='30',borderwidth=5,justify=CENTER)
entry2.pack(padx='3',pady='3')
ButtonRes=Button(Window,text='Determine Root',fg='red',font=('Helvetica', 11, 'bold'),command=newton).pack(padx='5',pady='5')
ResultRoot=Label(Window,text="  ",fg='#e8e8e8',font=('Helvetica', 14, 'bold'),bg='#050100')
ResultRoot.pack()

iter=ttk.Treeview(Window,columns=(1,2,3,4,5),show='headings',height=8)
iter.pack()
iter.column("1",anchor=CENTER, stretch=NO, width=100)
iter.heading(1,text='i',anchor=CENTER)
iter.column("2",anchor=CENTER, stretch=NO, width=100)
iter.heading(2,text='Xi',anchor=CENTER)
iter.column("3",anchor=CENTER, stretch=NO, width=100)
iter.heading(3,text='f(Xi)',anchor=CENTER)
iter.column("4",anchor=CENTER, stretch=NO, width=100)
iter.heading(4,text='f`(Xi)',anchor=CENTER)
iter.column("5",anchor=CENTER, stretch=NO, width=100)
iter.heading(5,text='Error%',anchor=CENTER)
style=ttk.Style()
style.theme_use("clam")
style.configure("Treeview",foreground='red')
style.configure('Treeview.Heading', background="red3")
style.map("Treeview",background=[('selected','red')])
style.map("Treeview")


#########################################################################

Window.mainloop()