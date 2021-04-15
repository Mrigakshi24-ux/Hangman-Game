from itertools import permutations
l1=[1,2,3,4,5]
dict={(1,2):1,(1,3):2,(2,3):4,(2,1):1,(3,1):2,(1,4):2,(1,5):3,(4,1):2,(5,1):3,(2,4):2,(2,5):3,(4,2):2,(5,2):3,(3,2):4,
      (3,4):3,(4,3):3,(3,5):2,(5,3):2,(4,5):3,(5,4):3}
c=False

x=[]

p= permutations(l1)
for i in list(p):
    d=0
    y=0
    print(i)
    
    for j in range(0,len(i)-1):
        for l in dict:
                if l==(i[j],i[j+1]) and i[j+1]!=None:
                    dict[l]
                    
                    c=True
                    break
        if c==True:
            d=d+dict[l]
            
        if j==len(i)-2:
            y=(i[0],i[len(i)-1])
            d=d+dict[y]
               
    print(d)
    x.append(d)  
print(x)
print(min(x))


