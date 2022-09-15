g=input("Enter a grade:")
s=int(input("Enter the salary:"))
if(g=="A" or g=="a" and s>11000):
    s1=s*0.05
    print(s+s1,s1)
if(g=="B" or g=="b" and s>11000):
    s1=s*0.10
    print(s+s1,s1)
if(s<=10000 and g=="a"):
    s1=s*0.15
    print(s+s1,s1)
if(s<=10000 and g=="b"):
    s1=s*0.20
    print(s+s1,s1)
if(g=="c"):
    print("NO BONUS!")

