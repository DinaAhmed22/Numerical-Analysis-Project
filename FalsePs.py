
from tkinter import *
from tkinter import ttk
from math import *
from tkinter import messagebox
from math import *



Window=Tk()
Window.title("False Position Method")
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

######Main Function##########################
def false():
    xl=get_XLower() #Getting XL Value 
    xu=get_Xupper() #Getting XU Value 
    ep=get_Epson() #Getting Epson Value 
    xr=0.0 #intialize xr=0.0
    xrold=0.0 #intialize xrold=0.0
    Err0r=0.0 #intialize Error  =0.0
    i=0 #intialize iter =0.0
    while  True: 
        xrold=xr #Xr will be stored in xrold
        FXL=get_Function(xl) #Substitue Function with Xl
        FXU=get_Function(xu) #Substitue Function with XU
        FXLI=float(FXL) #converting FXL to float
        FXUI=float(FXU) #converting FXUto float
        xr = xu - (FXUI * (xl - xu) / (FXLI - FXUI)) #Rule of Xr in False
        PolyCheck=FXLI*FXUI #Multiply FXLI with FXUI to check Polynomial has a solution or not
        ##If PolyCheck <0 it will have a solution
        if PolyCheck>=0:##if Polynomial greater than or equal zero wont have a solution
            messagebox.showwarning("Warning!!","Has No Solution") #If condition that ploycheck is greater than or equal zero is true it will give a warning to the user and wont solve polynomial
            exit()
        FXR=get_Function(xr) 
        FXRI=float(FXR)
        Err0r=abs((xr-xrold)/xr)*100 #calculating Error
        ##Entering Data in Treeview(table)
        if i==0:
            iter.insert(parent='', index='end', iid=i, text='',values=(i,xl,FXLI,xu,FXUI,xr,FXRI,' '))
        else:
          iter.insert(parent='', index='end', iid=i, text='',values=(i,xl,FXLI,xu,FXUI,xr,FXRI,Err0r))
        ##Multiply FXLI and FXRI before going to the next iteration to know new values of XL and Xu
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
LabelTitle=Label(Frame1,bg='#EEEDEC',text='False Position Method',fg='red',width='300',font=('Helvetica', 16, 'bold'))
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


ButtonRes=Button(Window,text='Determine Root',fg='red',font=('Helvetica', 11, 'bold'),command=false).pack(padx='5',pady='5')
ResultRoot=Label(Window,text=" ",fg='#e8e8e8',font=('Helvetica', 14, 'bold'),bg='#050100')
ResultRoot.pack()


style=ttk.Style()
style.theme_use("clam")

style.configure("Treeview",foreground='red')
style.configure('Treeview.Heading', background="red3")
style.map("Treeview",background=[('selected','red')])






Window.mainloop()