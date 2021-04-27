import math as m
x= int(input("Enter no.\n"))
ans =1
for i in range(1,x+1):
    ans *= i
    # print(ans) this line will print all ans as it is inside the for loop
print(ans)

for i in range(-1, -x):
    ans *= i
    # This for loop is in descending order like n(n-1)_______3.2.1
print(ans)