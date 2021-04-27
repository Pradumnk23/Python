import sys

#sys.setrecursionlimit(990)

print(sys.getrecursionlimit())

i = 0

def game():
    global i
    i+=1
    print("Hello", i)
    game()

game()