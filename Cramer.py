from os import remove#remove elements from matrix
from tkinter import *
import numpy as np
window=Tk()
window.config(bg='#050100')
window.geometry('600x700')
window.title("Cramer's Rules")

def getmatrix():
    matrix=[]
    for row in rows:
        a=[]
        for col in row:
            m = col.get()
            
            a.append(int(m))
           

            #print(m)
        #print(a)
        matrix.append(a)
    print(matrix)
    return(matrix)    

        



rows = []
for i in range(3):
    cols = []
    for j in range(4):
        e = Entry(window,width=10,bd=5,justify=CENTER)
        e.grid(row=i, column=j,padx='10',pady='10')
        cols.append(e)
    rows.append(cols)
def Get_GE():
    r= getmatrix()
    b1=r[0][3]
    b2=r[1][3]
    b3=r[2][3]
    B=np.array([b1,b2,b3])
    print ('The matrix ',r)
    print('B',B)
    #Determine The A Matrix
    a=[]
    for i in range(3):
        k=[]
        for j in range(3):
            k.append(r[i][j])
        a.append(k)
            
    print('The A Matrix: ',a)  
    #Determin D
    A=np.array(a)
    print('np array',A)
    D=int(np.linalg.det(A))
    print('The determinant D: ',D)
    Steps.insert(END,"det(D):")
    Steps.insert(END,D)
    Steps.insert(END,"\n","\n","\n","\n") 


    A1=np.array(a)
    A1[0:3,0]=B
    Steps.insert(END,A1)
    Steps.insert(END,"\n","\n","\n","\n") 
    print('A1: ',A1)
    D1=int(np.linalg.det(A1))
    print('The determinant D1: ',D1)
    Steps.insert(END,"det(D1):")
    Steps.insert(END,D1)
    Steps.insert(END,"\n","\n","\n","\n") 


    A2=np.array(a)
    A2[0:3,1]=B
    Steps.insert(END,A2)
    Steps.insert(END,"\n","\n","\n","\n") 
    print('A2: ',A2)
    D2=int(np.linalg.det(A2))
    print('The determinant D2: ',D2)
    Steps.insert(END,"det(D2):")
    Steps.insert(END,D2)
    Steps.insert(END,"\n","\n","\n","\n") 


    A3=np.array(a)
    A3[0:3,2]=B
    Steps.insert(END,A3)
    Steps.insert(END,"\n","\n","\n","\n") 

    print('A3: ',A3)
    D3=round(np.linalg.det(A3),1)
    print('The determinant D3: ',D3)
    Steps.insert(END,"det(D3):")
    Steps.insert(END,D3)
    Steps.insert(END,"\n","\n","\n","\n") 


    x1=D1/D
    x2=D2/D
    x3=D3/D
    Steps.insert(END,'x1=D1/D')
    Steps.insert(END,"\n","\n","\n","\n")
    Steps.insert(END,'x2=D2/D')
    Steps.insert(END,"\n","\n","\n","\n")
    Steps.insert(END,'x1=D3/D')
    Steps.insert(END,"\n","\n","\n","\n")
    print('x1 x2 x3 are ',x1,'  ',x2,'   ',x3)
    Result['text']=f"After Solving The System ,(X1,X2,X3) : {x1,x2,x3}"

#######################################################################################################3            
ButtonGetX=Button(window,text="Solve System",bg='white',fg='red',command=Get_GE).grid(row=9,column=2,padx='20',pady='20')
Result=Label(window,text="   ",fg='red',bg='#050100')
Result.grid(row=10,column=2,padx='20',pady='20')
Steps = Text(window, height =25,width =100,bg = "white")
Steps.grid(row=11,column=2)

window.mainloop()