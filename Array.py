from array import *

arr = array('i', [])

n = int(input("Enter length\n"))

for i in range(n):
    x = int(input("Enter numbers\n"))
    arr.append(x)

print(arr)
print(sorted(arr)) # This is for sorted the value of array..

val = int(input("Enter value for search\n"))
k=0
for e in arr:
    if e==val:
        print(k)
    k+=1

print(arr.index(val))