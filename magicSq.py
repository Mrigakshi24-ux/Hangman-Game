a=list(map(int, input().split()))
b=list(map(int, input().split()))
c=list(map(int, input().split()))
l=[a,b,c]
l1=[]
for i in l:
    for j in i:
        l1.append(j)
print(l1)
n=[
    [8, 1, 6, 3, 5, 7, 4, 9, 2],
    [6, 1, 8, 7, 5, 3, 2, 9, 4],
    [4, 9, 2, 3, 5, 7, 8, 1, 6],
    [2, 9, 4, 7, 5, 3, 6, 1, 8],
    [8, 3, 4, 1, 5, 9, 6, 7, 2],
    [4, 3, 8, 9, 5, 1, 2, 7, 6],
    [6, 7, 2, 1, 5, 9, 8, 3, 4],
    [2, 7, 6, 9, 5, 1, 4, 3, 8]
]

d=[]
for i in n:
    u=[]
    c=0
    
    for j in range(len(i)):
        c=c+abs(i[j]-l1[j])
        
        
    
    d.append(c)

print(min(d))
    
    
