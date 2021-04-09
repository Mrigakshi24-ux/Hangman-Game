import random
print("Welcome. let's play hangman")
a=['sell','play','come','out','int','char','stiff','long','print','now','no','big']
b=random.choice(a)

x=[]
for i in range (len(b)):
    x.append('*')
y=''.join(x)
print(y)

n=1
guess=5
while guess!=0:
    c=input(f"Enter your choice no {n}:")
    if len(c)>1:
        while (len(c)!=1):
            c=input("Enter again as it was an invalid choice:")
    for i in range(len(b)):
        if c==b[i]:
            x[i]=c
            y=''.join(x)
    print(y)
        
    if y==b:
        break
    n=n+1
    guess=guess-1
    print("Remaining guesses:",guess)
if guess==0:
    print("Sorry you could'nt guess")
elif guess==0 and y==b or y==b:
    print("You guessed the right word:",y)

    
        

