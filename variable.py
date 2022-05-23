class car :

    wheels = 4 #class variables or static variables


    def __init__(self): #if you define variable inside the inint it will be instnace variable
        self.mileage = 10
        self.company = "BMW"



c1 = car()
c2 = car()

car.wheels = 5 #it is as class namespace

print(c1.company , c1.mileage, c1.wheels)