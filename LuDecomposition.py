from os import remove#remove elements from matrix
from tkinter import *
import numpy as np
window=Tk()
window.config(bg='#050100')
window.geometry('600x700')
window.title("Lu Decomposition")

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
   
   z=0
   while z<2:
       for j in range(2):
            v=float(r[z][z])#pivot
            print('v= ',v)
            for i in range(1,3,1):
                if i+j<3:
                    #print(i)
                    #print(j)
                    m=r[i+j][j]/v
                    globals()['f%s%s'%(i+j,j)]=m
                    #print('***********','f%s%s'%(i+j,j))
                    #print('m= ',m)
                    x1=r[i+i*j][i*j-j]-m*r[j][i*j-j]
                    #print("i",i)
                    #print("j",j)
          # Result['text']=f"{x1} "

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
               
                    print('Matrix after iteration: ',r)
                else:
                    break




                
            z=z+1
           
            r3=x4/x3
            # print('root 3= ',r3)
            #print('m21= ',f10)
            #print('m31= ',f20)
            #print('m32= ',m)
            v=r
            remove
            m21=f10
            m31=f20
            m32=m
            
            #print('The final matrix after Gauss: ',v)
            #print('coef are:',m21,m31,m32)
            ###########
            # To get the matrix U
            u=[]
            for i in range(3):
                k=[]
                for j in range(3):
                    k.append(v[i][j])
                u.append(k)
            

           

            print('The U Matrix: ',u)
            o=u
            
            l=[]
            for i in range(3):
                w=[]
                for j in range(3):
                    w.append(u[i][j])
                l.append(w)

            l[0][0]=1
            l[0][1]=0
            l[0][2]=0
            l[1][0]=m21
            l[1][1]=1
            l[1][2]=0
            l[2][0]=m31
            l[2][1]=m32
            l[2][2]=1
            

            print ('The L matrix:',l)
            # C1,C2 and C3 calculations(Forward substitution)LC=B
            c1=b1/l[0][0]
            c2=(b2-l[1][0]*c1)/l[1][1]
            c3=(b3-l[2][0]*c1-l[2][1]*c2)/l[2][2]
            print('c1= ',c1,'c2= ',c2,'c3= ',c3)
            CResult['text']=f"(C1,C2,C3): {c1,c2,c3}"


            #Solving the system UX=C

            print('The U Matrix: ',u)
            print(o)
            co3=c3/u[2][2]
            print(u[2][2])
            print(b3)
            co2=(c2-u[1][2]*co3)/u[1][1]
            co1=(c1-u[0][1]*co2-u[0][2]*co3)/u[0][0]
                
            Steps.insert(END,"The Coeficients of Matrix are :")
            Steps.insert(END,"\n")
            Steps.insert(END,f10)
            Steps.insert(END,",")  
            Steps.insert(END,f20)
            Steps.insert(END,",")  
            Steps.insert(END,m) 
            Steps.insert(END,",") 
            Steps.insert(END,"Matrix after Gauss:")
            Steps.insert(END,"\n","\n","\n","\n")
            Steps.insert(END,v)
            Steps.insert(END,"\n","\n","\n","\n")
            Steps.insert(END,"Upper Matrix:")
            Steps.insert(END,"\n","\n","\n","\n")
            Steps.insert(END,u)
            Steps.insert(END,"\n","\n","\n","\n")
            Steps.insert(END,"L matrix:")
            Steps.insert(END,"\n","\n","\n","\n")
            Steps.insert(END,l)  
            Steps.insert(END,"\n","\n","\n","\n")
            #print('x1= ',co1,'x2= ',co2,'x3= ',co3)
            #print(b1,b2,b3)
            Result['text']=f"After Solving The System ,(X1,X2,X3) : {co1,co2,co3}"







#######################################################################################################3            
ButtonGetX=Button(window,text="Solve System",bg='white',fg='red',command=Get_GE).grid(row=9,column=2,padx='20',pady='20')
Result=Label(window,text="   ",fg='red',bg='#050100')
Result.grid(row=10,column=2,padx='20',pady='20')
CResult=Label(window,text="   ",fg='red',bg='#050100')
CResult.grid(row=9,column=1,padx='20',pady='20')
Steps = Text(window, height =25,width = 100,bg = "white")
Steps.grid(row=11,column=2)

window.mainloop()