

class Animal:

    def __init__(self, newName):
        # self.name = "Franklin"
        self.name = newName

    def runs(self):
        print("My name is ", self.name," and I run")

class Person:

    def __init__(self):
        self.fname = ""
        self.lastname = ""
        self.ssn=0
        self.height = 0

    def grows(self):
        self.height = self.height + 7 


    def show_off(self):
        print("My name is ", self.fname, " ", self.lastname)

        print("My ssn is ", self.ssn)

        print("My height is ", self.height)


d = Animal("Dog")
d.runs()

franklin = Person()
franklin.fname = "Franklin"
franklin.lastname = "Ngongang"
franklin.ssn = 364633737
franklin.height = 6

franklin.show_off()

franklin.show_off()