import numpy as np
def isSafe(board, x, y):
    for i in range(n):
        if ( board[x][y]==1 or board[i][y]==1 or board[x][i]==1):
            return False
    for i in range(n):
        for j in range(n):
            if (i+j==x+y) or (i-j==x-y):
                if board[i][j]==1:
                    return False
        
            
    return True 
        

n=int(input("Enter the size:"))
board=np.zeros((n,n),dtype=int)
print(board)

def place(board,p):
    if p==n:
        return True
    for i in range(n):
            if isSafe(board,p,i)==True :
                board[p][i]=1
                if place(board,p+1)==True:
                    return True
                
                else:
                    board[p][i]=0
                    
                                
                                
    return False
                
        
            
print()        
if place(board,0)==True:
    print(board)
else:
    print("Solution not found")

        

        

            
