t = int(input())
for _ in range(t):
    n = int(input())
    l = []
    fcx = {}
    fcy = {}

    for __ in range((4*n)-1):
        x, y = map(int, input().rstrip().split())
        try:
            fcx[x] += 1
        except KeyError:
            fcx[x] = 1

        try:
            fcy[y] += 1
        except KeyError:
            fcy[y] = 1

    for i in fcx:
        if fcx[i]%2 != 0:
            break

    for j in fcy:
        if fcy[j]%2 != 0:
            break

    print(i,j)