class A :
    def feature1(self):
        print("this is feature 1")
    def feature2(self):

        print("this is feature 2")

class B(A) : #inherited the feature of class A in class B
    def feature3(self):
        print("this is feature 3")
    def feature4(self):
        print("this is feature 4")


class C(B): #c is inheriting from b and a because B is already inherited from A
    def feature5(self):
        print("this is feature5")
s1 = A()

s1.feature1()
s1.feature2()

b1 = B()
b1.feature2()

c1 = C()
c1.feature2() #this is the example of multiple inheritance