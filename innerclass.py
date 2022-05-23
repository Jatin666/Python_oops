class student:
    def __init__(self,name , rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()
        #you can create object of inner class inside the outer class
        #you can create object of inner class outside the outer class provided
        #you use outer class name to call it

    def show(self):
        print(self.name, self.rollno)
        print(self.lap.show())


    class laptop: #laptop is an inner class of student class

        def __init__(self):
            self.brand ='hp'
            self.cpu ='i5'
            self.ram = 8

        def show(self):
            print(self.cpu,self.ram,self.brand)


s1 = student('jatin', 2)
s2 = student('sumo',1)
s1.show()



