class student:
    school = 'mzm'
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def schoolname(cls):
        return cls.school

    @staticmethod
    def info():
        print("Hello class")

s1 = student(31, 54, 65)
s2 = student(62, 32, 45)
print(s1.avg())
print(s2.avg())

print(student.schoolname())
student.info()