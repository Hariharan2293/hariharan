n=int(input("Enter a number:"))
if(n<=999):
    a=int(n/100)
    b=int(n%100)
    c=int(b/10)
    d=int(n%10)
    print(a,c,d)
    print(d,c,a)
    print(c,d,a)
    print(c,a,d)
    print(d,a,c)
    print(a,d,c)
if(n>=1000):
    o=int(n/1000)
    p=int(n%1000)
    q=int(p/100)
    r=int(p%100)
    s=int(r/10)
    t=int(r%10)
    print(o,q,s,t)
    print(t,s,q,o)
    print(q,s,o,t)
    print(t,s,o,q)
    print(s,q,t,o)
    print(t,o,s,q)
    print(s,o,q,t)
if(n<0):
    print("POSITIVE NUMBER REQUIRED!")

    
    
    
