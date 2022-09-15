l=int(input("Enter number of elements:"))
lst=[]
sum1=0
sum2=0
for i in range(0,l):
    ele=int(input())
    lst.append(ele)
for i in range(0,l):
    if(lst[i]%2==0):
        sum2=sum2+lst[i]**2
    else:
        sum1=sum1+lst[i]**2
l1=[sum1,sum2]
print(l1)
 
