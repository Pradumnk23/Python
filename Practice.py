import math
def get(x):
    for i in range(2, math.sqrt(x)):
        if x%i == 0:
            return x/i
    return 1

def sol():
    x,y = int(input())
    if(x<y):
        x, y = y, x
    if(x==y):
        print("0")
        return
    c= 0
    while x != 1:
        c += 1
        x = get(x)
        m[x] = c

    c = 0
    while !m.count(y):
        c+=1
        y = get(y)
    print(c + m[y])

sol()