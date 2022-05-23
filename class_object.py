#classes and objects

class computer:
#special method
    def __init__(self, cpu, ram): #init inititalised the variables
        self.cpu = cpu
        self.ram = ram


    def config(self): #self is an object youre passing
        print("config is ", self.cpu, self.ram)


comp1 = computer('i5', 16) #cpu, ram
comp2 = computer("Ryzen 3", 8)

#computer.config(comp1) #calling the class with using object comp1
comp1.config() #common method to call the class
comp2.config()


