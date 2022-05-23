class computer:


    def __init__(self):
        self.name = "jatin"
        self.age = 25

    def update(self): #for updating the age self is acting as a pointer

        self.age = 30

    def compare(self, c2):
        if self.age == c2.age :
            return True
        else:
            return False

#everytime you create an object it allocate to new space
#size of the object is depend upon the size of the variable

c1 = computer()
c1.age = 30
c2= computer()

if c1.compare(c2):
    print("They are same")
else :
    print("they are different")


c1.update() #self is refering to an object

print(c1.name)
print(c1.age)

