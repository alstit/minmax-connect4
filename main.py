from array import *
import random
import copy


#T=[[0,0,0,0,0],[2,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

#print(T[0])
#print(T[1])

window_size = 4

def point(T,line_size,col_size,player):   

#    colPoint = []
    
    #print("player is")
    #print(player)
    score = 0   
#    for i in range(0,line_size,1):
#        colPoint.append(0)
        
        
        
    window = []
    for i in range(0,window_size,1):
        window.append(0)    
        
    #colonne search
    for i in range(0,line_size-1,1):
        for j in range(0,col_size-window_size+1,1):
            l=0
            for k in range(j,j+window_size,1):
                window[l]= T[k][i]
                l+=1
            if window.count(player) == 4:
                score += 4           
            if window.count(player) == 3 and window.count(0)==1:
                score += 3
            else :
                score += 0      
            #colPoint[i] += score
    
    #line search
    
    for i in range(0,col_size,1):
        for j in range(0,line_size-window_size+1,1):
            window = T[i][j:j+window_size]
            #print("window")
            #print(window)
            #print(i)
            if window.count(player) == 4:
                score += 4     
                #colPoint[j+window_size-1]+=score                     
            elif window.count(player) == 3 and window.count(0)==1 :
                #print("hello")
                if i !=col_size-1 :
                    if T[i+1][window.index(0)] == player :
                        score += 3
                elif i == col_size-1 :  
                    
                    score += 3   
                else :
                    score += 0
                #colPoint[j+window.index(0)] += score
            else :
                score += 0       
    
    
   # print("colPoint =")
   # print(score)
    return score

def pickBestMove(T, line_size, col_size,depthMAX , player, ai,isAI,k,l): 
    depth = depthMAX
    Tnext = copy.deepcopy(T)
    results = []
    move = []
    score=[]
    scoreOnly = []
    
    #print("depth = ")
    #print(depth)

    if depth == 0 : 
        pointListAI=point(Tnext, line_size, col_size, ai) 
        pointListPLAYER2=point(Tnext, line_size, col_size, player) 
        
 
        move.append(pointListAI - 2*pointListPLAYER2)
        move.append(k)
        move.append(l)
            #print("move =")
            #print(move)
        return move


    for j in range(0,line_size):
        for i in range(col_size-1,-1,-1):
            if(Tnext[i][j] == 0):
                Tnext[i][j]=ai        
                if isAI : 
                    results.append(pickBestMove(Tnext, line_size, col_size , depth - 1, ai , player,not isAI,i,j))
                
                else :
                    results.append(pickBestMove(Tnext, line_size, col_size , depth - 1, player , ai,not isAI,i,j))
                break;
            
            
        
    for bestMove in results :

        #print("bestmove = ")
        #print(bestMove)
        score.append(bestMove)
        #print("score = ")
        #print(score)
        
    for scoreTab in score:
        scoreOnly.append(scoreTab[0])
    
    #if isAI :
    BestScore = max(scoreOnly)
    
    #else : 
    #    BestScore = min(scoreOnly)
    
    for scoreTab in score:
        if scoreTab[0] == BestScore:
            return scoreTab                            
        





def isvalidPosition(T,col):

    if T[0][col]==0:
        return True
    else:
         return False

def main():
    line_size=20
    col_size=20

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

        

                    
        playing = True
        while(playing):
            print("joueur 1 choisissez une colonne")       
            joueur1 = int(input())
            if isvalidPosition(T, joueur1):
                playing =False
                for i in range(col_size-1,-1,-1):
                        if(T[i][joueur1] == 0):
                            T[i][joueur1]=1
                            break;
            else : print("chosse another row")
        
        
        for i in range(0,col_size):
            print(T[i])
            
            
        print("joueur2 choisissez une colonne")

        score,x,joueur2 = pickBestMove(T,line_size,col_size,2,2,1,1,0,0)

        print(joueur2)
        for i in range(col_size-1,-1,-1):
            if(T[i][joueur2] == 0):
                T[i][joueur2]=2
                break;
            
        
        for i in range(0,5):
            print(T[i])    


 

if __name__ == '__main__':
    main()