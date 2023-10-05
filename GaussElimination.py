from tkinter import *
import numpy as np
window=Tk()
window.config(bg='#050100')
window.geometry('600x700')
window.title("Gauss Elimination")

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
   z=0
   while z<2:
       for j in range(2):
            v=float(r[z][z])#pivot
            print('v= ',v)
            for i in range(1,3,1):
                if i+j<3:
                    print(i)
                    print(j)
                    m=r[i+j][j]/v
                    globals()['f%s%s'%(i+j,j)]=m
                    print('m= ',m)
                    globals()['f%s%s'%(i+j,j)]=m
                    x1=r[i+i*j][i*j-j]-m*r[j][i*j-j]
                    print("i",i)
                    print("j",j)

                    x2=r[i+i*j][i*j-j+1]-m*r[j][i*j-j+1]
                    x3=r[i+i*j][i*j-j+2]-m*r[j][i*j-j+2]
                    x4=r[i+i*j][i*j-j+3]-m*r[j][i*j-j+3]

                    print('x1 ',x1)
                    print('x2 ',x2)
                    print('x3 ',x3)
                    print('x4 ',x4)
                    r[i*j+i][i*j-j]=x1
                    r[i*j+i][i*j-j+1]=x2
                    r[i*j+i][i*j-j+2]=x3
                    r[i*j+i][i*j-j+3]=x4
                    Steps.insert(END,"Matrix")

                    Steps.insert(END,r)
                    Steps.insert(END,"\n","\n","\n","\n")
           
            
               
                    print('Matrix after iteration: ',r)
                else:
                    break

                


            z=z+1
            R3=x4/x3
            print('R3= ',R3)
            
            m21=f10
            m31=f20
            m32=m 
            print('m21=',m21,'m31=',m31,'m32=',m32)
            Steps.insert(END,"The Coeficients of Matrix are :")
            Steps.insert(END,"\n")
            Steps.insert(END,f10)
            Steps.insert(END,"\n","\n","\n","\n")  
            Steps.insert(END,f20)
            Steps.insert(END,"\n","\n","\n","\n")  

            Steps.insert(END,m) 
            Steps.insert(END,"\n","\n","\n","\n") 
            R2=(r[1][3]-r[1][2]*R3)/r[1][1]  
            R1=(r[0][3]-r[0][1]*R2-r[0][2]*R3)/r[0][0] 
            Steps.insert(END,r)
            Steps.insert(END,"\n","\n","\n","\n") 

            print("X1,X2,X3",R1," ",R2," ",R3)

            Result['text']=f"After Solving The System ,(X1,X2,X3): {R1,R2,R3}"




            
           

ButtonGetX=Button(window,text="Solve System",bg='white',fg='red',command=Get_GE).grid(row=9,column=2,padx='20',pady='20')
Result=Label(window,text="   ",fg='red',bg='#050100')
Result.grid(row=10,column=2,padx='20',pady='20')
Steps = Text(window, height =25,width = 100,bg = "white")
Steps.grid(row=11,column=2)

window.mainloop()