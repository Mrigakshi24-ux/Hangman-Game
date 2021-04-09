import numpy as np
import random
a = np.array((('_','_','_'),('_','_','_'),('_','_','_')))
print('\n'.join(['  '.join([str(i) for i in j]) for j in a]))
l = [0, 1, 2]


def checkRowCol(a1, i1, j1, p1, s1, x1):
    for k in range(3):
            if a[i1][k] == x1 and a[i1][j1]==x1:
                p1 = p1 + 1
            if a[k][j1] == x1 and a[i1][j1]==x1:
                s1 = s1 + 1
    return(p1,s1)
    
            
def checkDiag(a, i, j, c, x):
    for k in range(3):
        for l in range(3):
            if k+l==i+j or k-l==i-j:
                if a[k][l] == a[i][j] and a[i][j] == x:
                    c = c + 1
    return(c)



x = input("Enter a choice between 0 and X : ")
while not(x=='X'or x=='0'):
    x = input("You entered wrong choice!!Enter a choice between 0 and X : ")    
if x == '0':
    y = 'X'
else:
    y = '0'


 
for it in range(5):
    c = 0
    d = 0
    p = 0
    q = 0
    s = 0
    t = 0  
     
    

    i = int(input("Enter the row : "))
    j = int(input("Enter the column : "))
    if it != 0:
        if a[i][j] != '_':
            while a[i][j] != '_':
                print("Enter again..")
                i = int(input("Enter the row : "))
                j = int(input("Enter the column : "))
    
        
    a[i][j] = x
    (p,s)=checkRowCol(a, i, j, p, s, x)
    c= checkDiag(a, i, j, c, x)
    if c > 2 or p > 2 or s > 2:
        z = True 
        break 
    if it==4 and c<=2 and d<=2 and p<=2 and q<=2 and s<=2 and t<=2 :
        z=10
        break
    m = np.random.choice(l)
    n = np.random.choice(l)
    
    if a[m][n] != '_':
        while a[m][n] != '_':
            m = np.random.choice(l)
            n = np.random.choice(l)
    a[m][n] = y
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in a]))
    (q,t)=checkRowCol(a, m, n, q, t, y)
    d=checkDiag(a, m, n, d, y)
    if d > 2 or q > 2 or t > 2:
        z = False
        break
    print(c,d,p,q,s,t)
    
    
    
if z == True:
    print("You won bitch")
if z == False:
    print("Computer won loser")
if z == 10:
    print("Hmm, both equally competitive")
