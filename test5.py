e=int(input("Enter the number of fresh loaves purchased:"))
c=int(input("Enter the number of day old loaves purcased:"))
r=185
e*=185
c*=float(185*60/100)
total=float(e+c)
if(e>0):
    print("Regular loaves price : Rs.",r)
    print("Amount of new loaves:",e)
    print("amount of day old loaves:",float(c))
    print("Total amount:Rs.",total)
else:
    print("its invalid")
