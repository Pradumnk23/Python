pos = -1

def search(list2, n):
    l = 0;
    u = len(list2) - 1
    while l <= u:
        mid = (l+u)//2

        if list2[mid] == n:
            globals() ['pos'] = mid
            return True
        else:
            if list2[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False

list = [1,5,4,7,9,25,45]
list2 = sorted(list)
print(list2)
n = int(input())
if(search(list2, n)):
    print(pos)
else:
    print("Not Found")