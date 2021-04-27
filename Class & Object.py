class computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("The config is", self.cpu, self.ram)

com1 = computer('i5 proc', '8 Gb ram')
com2 = computer('Ryzen proc', '8 Gb ram')

com1.config()
com2.config()

