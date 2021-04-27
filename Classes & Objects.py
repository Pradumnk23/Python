class Enemy:
    life = 3

    def attack(self):
        print("Issh")
        self.life -= 1

    def checklife(self):
        if self.life <= 0:
            print("Dead")
        else:
            print(str(self.life) + " Life left")

enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()

# If we will write enemy1.attack one more time it will becomes =0 and prints dead instead of how many life left..
# It will not effect on enemy2 as it has 3 life left..

enemy1.checklife()
enemy2.checklife()