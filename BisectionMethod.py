
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
Window=Tk()
Window.title("Bisection Method")
Window.geometry('1000x700')
Window.config(bg='#050100')
f = ("Helvetica",9,'bold')
############Commands######################################
##Get Entries #####################
def get_XLower():
    Xlo=float(XLowerEntry.get())
    return Xlo
def get_Xupper():
    Xu=float(XUpperEntry.get())
    return Xu
def get_Epson():
    EPS=float(EpsEntry.get())
    return EPS

def get_Function(x):
    Func=str(eval(entry.get()))
    return Func
#

######Main Function##########################
def bisect():
    xl=get_XLower()
    xu=get_Xupper()
    ep=get_Epson()

    xr=0.0
    xrold=0.0
    Err0r=0.0
    i=0
    while  True:
        xrold=xr
        print(xl)
        print(xu)
        xr=(xl+xu)/2
        FXL=get_Function(xl)
        FXU=get_Function(xu)
        FXLI=float(FXL)
        FXUI=float(FXU)
        
        PolyCheck=FXLI*FXUI
        if PolyCheck>=0:
            messagebox.showwarning("Warning!!","Has No Solution")
            exit()
        FXR=get_Function(xr)
        FXRI=float(FXR)
        Err0r=abs((xr-xrold)/xr)*100
        if i==0:
            iter.insert(parent='', index='end', iid=i, text='',values=(i,xl,FXLI,xu,FXUI,xr,FXRI,' '))
        else:
          iter.insert(parent='', index='end', iid=i, text='',values=(i,xl,FXLI,xu,FXUI,xr,FXRI,Err0r))
        sign_check=FXLI*FXRI
        if sign_check>0:
             xl=xr
        elif sign_check<0:
            xu=xr
        else:
            ResultRoot['text']=f"The Root is :{xr} "
            return xr
            break


        i=i+1
        

        if Err0r<=ep:
            break
     
    ResultRoot['text']=f"The Root is :{xr} "

    
    return xr 


######################################################
##################GUI ##############################
Frame1=Frame(Window,bg='#EEEDEC',width='300',height='200')
Frame1.pack(side=TOP,padx='20',pady='20')
LabelTitle=Label(Frame1,bg='#EEEDEC',text='Bisection Method',fg='red',width='300',font=('Helvetica', 16, 'bold'))
LabelTitle.pack(padx='5',pady='5')
XlowerLAbel=Label(Window,text=' X lower',bg='#050100', fg='red',font=('Helvetica', 11, 'bold')).pack(padx='10')
XLowerEntry=Entry(Window,borderwidth=5,width='30',justify=CENTER)
XLowerEntry.pack(padx='5',pady='5')
XUpperLAbel=Label(Window,text=' X Upper',bg='#050100', fg='red',font=('Helvetica', 11, 'bold')).pack(padx='10')
XUpperEntry=Entry(Window,borderwidth=5,width='30',justify=CENTER)
XUpperEntry.pack(padx='5',pady='5')
EPSL=Label(Window,text=' Epson',bg='#050100', fg='red',font=('Helvetica', 11, 'bold')).pack(padx='10')
EpsEntry=Entry(Window,borderwidth=5,width='30',justify=CENTER)
EpsEntry.pack(padx='5',pady='5')

f=Label(Window, text="f(x)",bg='#050100',fg='red',font=('Helvetica', 11, 'bold')).pack()
entry = Entry(Window,borderwidth=5,width='30',justify=CENTER)
entry.pack(padx='10',pady='10')


#####Table##################

iter=ttk.Treeview(Window,columns=(1,2,3,4,5,6,7,8),show='headings',height=9)
iter.pack()
iter.column("1",anchor=CENTER, stretch=NO, width=100)
iter.heading(1,text='i')
iter.column("2",anchor=CENTER, stretch=NO, width=100)
iter.heading(2,text='Xl')
iter.column("3",anchor=CENTER, stretch=NO, width=100)
iter.heading(3,text='f(Xl)')
iter.column("4",anchor=CENTER, stretch=NO, width=100)
iter.heading(4,text='Xu')
iter.column("5",anchor=CENTER, stretch=NO, width=100)
iter.heading(5,text='f(Xu)')
iter.column("6",anchor=CENTER, stretch=NO, width=100)
iter.heading(6,text='Xr')
iter.column("7",anchor=CENTER, stretch=NO, width=100)
iter.heading(7,text='f(Xr)')
iter.column("8",anchor=CENTER, stretch=NO, width=100)
iter.heading(8,text='Error%')
ButtonRes=Button(Window,text='Determine Root',fg='red',font=('Helvetica', 11, 'bold'),command=bisect).pack(padx='5',pady='5')
ResultRoot=Label(Window,text=" ",fg='#e8e8e8',font=('Helvetica', 14, 'bold'),bg='#050100')
ResultRoot.pack()
style=ttk.Style()
style.theme_use("clam")
style.configure("Treeview",foreground='red')
style.configure('Treeview.Heading', background="red3")
style.map("Treeview",background=[('selected','red')])
#################################################################################################################################################3



Window.mainloop()