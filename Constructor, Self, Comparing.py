class computer:

    def __init__(self):
        self.name = "Pradumn"
        self.age = 18

    def compare(self, another):
        if self.age == another.age:
            return True
        else:
            return False

c1 = computer()
c1.age = 20
c2 = computer()

if c1.compare(c2):
    print("Same")
else:
    print("Not same")

print(c1.name)
print(c2.name)