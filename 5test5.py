n=int(input("ENTER:"))
c=[]
d=0
e=[]
while(n>0):
    b=int(input("Enter a number:"))
    c.append(b)
    d+=1
    if(d==n):
        break
e=c.copy()
c.sort()
for i in range(0,n):
    z=n-1
    if(c[z]==e[i]):
        print(i)
            
        

