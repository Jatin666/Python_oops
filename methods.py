class student:

    school = 'abcsd' #class variable

    def __init__(self,m1,m2,m3):
        #instance varables
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self): #average is instance method because it works with object
        return(self.m1 + self.m2 + self.m3)/3

    @classmethod
    def getSchool(cls): #use cls because we are using with class variables
        return cls.school
    @staticmethod
    def info(): #using static varible and calling it
        print("this is class module we are using...")

s1 = student(17,53,42)
s2 = student(22,88,44)
print(s1.avg())
print(s2.avg())
print(student.getSchool())
student.info()

#if you want to fetch the value of instance variable is accessor methods
#if you want to modify then we use mutator

