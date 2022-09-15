s=input("Enter a word:")
count=0
s=s[::-1]
for i in s:
    if i!=" ":
        s1=len(s)
        count+=1
    else:
        break
print(count)

