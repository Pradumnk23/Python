pos = -1

def search(list, n):
    i = 0
    while i < len(list):
        if list[i]==n:
            globals() ['pos'] = i
            return True
        i +=1
    return False

list = [1,5,4,7,9,25,45]
n = int(input())
if(search(list, n)):
    print(pos)
else:
    print("Not Found")