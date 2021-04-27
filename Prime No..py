import math as m
x= int(input("Enter no.\n"))
y= m.sqrt(x)
z= x/2
for i in range(2,int(z)): # we can use here x, y and z but y is more efficient and takes less time to run
    if x%i==0:
        print("Not prime")
        break
else:
    print("Prime")