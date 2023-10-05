from tkinter import *
from tkinter import ttk
from math import *
from tkinter import messagebox
from tkinter.font import BOLD
root=Tk()
root.title("Numerical Analysis Calculator")
root.geometry('1000x700')###TAzbet 7agm
root.config(bg='#050100')###Lon el Saf7a
abelX=Label(root,text='Numerical Analysis Rules',bg='#f2e9de',fg='red',width='300',font=('Helvetica', 18, 'bold')).pack(side=TOP,padx='20',pady='20')#اتزم تعمل pack عشان تظهر
nb=ttk.Notebook(root,width='600',height='700')
Frame1=Frame(nb)
nb.add(Frame1,text='Chapter 1')
Frame2=Frame(nb)

nb.pack()


LabelCH1Rules=Label(Frame1,text='Chapter 1 Rules',fg='red',font=('Helvetica', 16, 'bold'))
LabelCH1Rules.pack()
separator = ttk.Separator(Frame1, orient='horizontal')
separator.pack(fill='x')
LabelBisectionMethodRule=Label(Frame1,text='Bisection Method',fg='red',font=('Helvetica', 14, 'bold')).pack(padx='3',pady='3')
separator = ttk.Separator(Frame1, orient='horizontal')
separator.pack(ipadx='90')
Labelxrrule=Label(Frame1,text='Xr=(xl+xu)/2',fg='red',font=('Helvetica', 11, 'bold')).pack(padx='3',pady='3')
LabelBisectionErrorrule=Label(Frame1,text='Error=(xrnew-xrold/xrnew)*100',fg='red',font=('Helvetica', 11, 'bold')).pack(padx='3',pady='3')
separator = ttk.Separator(Frame1, orient='horizontal')
separator.pack(ipadx='200')
LabelFalsePositionMethodrule=Label(Frame1,text='False Position Method',fg='red',font=('Helvetica', 14, 'bold')).pack(padx='3',pady='3')
separator = ttk.Separator(Frame1, orient='horizontal')
separator.pack(ipadx='90')
Labelxrrule=Label(Frame1,text='Xr=xu-(f(xu)*(xl-xu)/f(xl)-f(xu))',fg='red',font=('Helvetica', 11, 'bold')).pack(padx='3',pady='3')
LabelFalsePositionErrorrule=Label(Frame1,text='error=(xrnew-xrold/xrnew)*100%)',fg='red',font=('Helvetica', 11, 'bold')).pack(padx='3',pady='3')
separator = ttk.Separator(Frame1, orient='horizontal')
separator.pack(ipadx='200')
LabelSimpleFixedPointMethodRule=Label(Frame1,text='Simple Fixed Point Method',fg='red',font=('Helvetica', 14, 'bold')).pack(padx='3',pady='3')
separator = ttk.Separator(Frame1, orient='horizontal')
separator.pack(ipadx='90')
Labelsimplifyequationfirst=Label(Frame1,text='Simplify equation first',fg='red',font=('Helvetica', 11, 'bold')).pack(padx='3',pady='3')
Labelxiplus1rule=Label(Frame1,text='xi+1=f(xi)',fg='red',font=('Helvetica', 11, 'bold')).pack(padx='3',pady='3')
LabelSimpleFixedPointErrorrule=Label(Frame1,text='error=(xinew-xiold/xinew)*100',fg='red',font=('Helvetica', 11, 'bold')).pack(padx='3',pady='3')
LabelNewtonMethodRule=Label(Frame1,text='Newton Method',fg='red',font=('Helvetica', 14, 'bold')).pack()
separator = ttk.Separator(Frame1, orient='horizontal')
separator.pack(ipadx='90')
Labelfirst=Label(Frame1,text='First get derivative of f(x)',fg='red',font=('Helvetica', 11, 'bold')).pack()
Labelxiplus1rule=Label(Frame1,text='xi-(f(xi)/fdash(xi))',fg='red',font=('Helvetica', 11, 'bold')).pack()
LabelNewtonErrorrule=Label(Frame1,text='error=(xinew-xiold/xinew)*100',fg='red',font=('Helvetica', 11, 'bold')).pack()
separator = ttk.Separator(Frame1, orient='horizontal')
separator.pack(ipadx='200')
LabelSecantMethodRule=Label(Frame1,text='Secant Method',fg='red',font=('Helvetica', 14, 'bold')).pack(padx='3',pady='3')
separator = ttk.Separator(Frame1, orient='horizontal')
separator.pack(ipadx='90')
Labelxiplus1rule=Label(Frame1,text='Xi=1=Xi-(f(Xi)(Xi-1-Xi))/(f(Xi-1) )-f(Xi))',fg='red',font=('Helvetica', 11, 'bold')).pack(padx='3',pady='3')
LabelSecantErrorrule=Label(Frame1,text='error=(xinew-xiold/xinew)*100',fg='red',font=('Helvetica', 11, 'bold')).pack(padx='3',pady='3')
root.mainloop()
