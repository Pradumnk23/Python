class parent:
    def last_name(self):
        print('Kumar')

class child(parent):
    def first_name(self):
        print('Pradumn')
    def last_name(self):
        print('Mukund')
# Here even after heritance last_name kumar is not printing , bcz we have given the class child its own last_name

pradumn = child()
pradumn.first_name()
pradumn.last_name()

# 2nd Example
class A:
    def feature1(self):
        print("Feature 1 is working")
    def feature2(self):
        print("Feature 1 is working")

class B(A):
    def feature3(self):
        print("Feature 3 is working")
    def feature4(self):
        print("Feature 4 is working")
class C(B): # if b was not the inheritance of a then we can write C(A,B) - Known as multilevel inheritance
    def feature5(self):
        print("Feature 5 is working")

a1 = A()
a1.feature1()
a1.feature2()
b1 = B()
b1.feature2()
b1.feature3()
c1 = C()
c1.feature4()
c1.feature5()