#duck typing
class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class Myeditor:
    def execute(self):
        print("SPELL CHECK")


class Laptop :
    def code(self,ide):
        ide.execute()

ide = Myeditor()

lap1 = Laptop()
lap1.code(ide)