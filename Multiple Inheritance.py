class Mario:
    def jump(self):
        print('I can jump')

class Chicken:
    def eat(self):
        print("After dinner, i gets bigger and can't jump") # double quotes bcz there is 't in can't..

class thussar(Mario, Chicken):
    pass

fat = thussar()
fat.jump()
fat.eat()