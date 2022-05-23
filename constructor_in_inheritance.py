class A:
    def __init__(self): #constructor
        print("in A init")

    def feature1(self):
        print("this is feature 1")
    def feature2(self):

        print("this is feature 2")

class B(A) : #inherited the feature of class A in class B

    def __init__(self):
        super().__init__() #for calling the A constructor from B using super()
        print("in B init")
    def feature3(self):
        print("this is feature 3")
    def feature4(self):
        print("this is feature 4")


#even we have the object of B we can call the constructor of A but if there is no constructor in B
a1 = B()
#when you run the code it will first check whether there is constructor of b or not

