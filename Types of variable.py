class car:
    wheels = 4

    def __init__(self):
        self.mil = 10
        self.br = 'Audi'

c1 = car()
c2 = car()
car.wheels = 5 # Used class for changing value
c1.mil = 8

print(c1.mil, c1.br, c1.wheels)
print(c2.mil, c2.br, c2.wheels)
# If we want to change the wheels, we have to use class name not object, e.g : car.wheels = 5
