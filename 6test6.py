n=int(input("Enter a number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        j=j*0.01
        print(j*10, end=" ")
    print()
        
