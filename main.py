from array import *
import random
from pandas.util import _validators

#T=[[0,0,0,0,0],[2,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

#print(T[0])
#print(T[1])
line_size=5
col_size=5

T=[]

line=[]
for j in range(0,line_size):
    line.insert(j,0)
    #print(Celia)

for i in range(0,col_size):
    T.insert(i, line.copy())


for i in range(0,col_size):
    print(T[i])
    #print(i)


while(True):
    print("joueur 1 choisissez une colonne")       
    joueur1 = int(input())
    
    for i in range(col_size-1,0,-1):
        if(T[i][joueur1] == 0):
            T[i][joueur1]=1
            break;
    
    
    
    for i in range(0,col_size):
        print(T[i])
        
        
    print("joueur2 choisissez une colonne")
    joueur2 = 1

    j=col_size-1   
    while(j>=0):
        if(T[j][joueur2] == 0):
            T[j][joueur2]=2
            break;
    
        j=j-1
        
    
    for i in range(0,5):
        print(T[i])    

    c=0
    compteurPoint = 4
    currentPoint = 0

    while (j < col_size):
        if(T[j][c]==1):
            jump=0
            currentPoint+=1
            for point in range(j+1,j+compteurPoint):
                Flag_jump=1
                jump += 1
                if(point<col_size and T[point][c] == 1):
                    currentPoint+=1
                    print("Npoint")
            if(Flag_jump):
                j+=jump
                        
    print("point du joueur1")
    print(currentPoint)
                        
                
        
        
    
    
