class Person:
    def __init__(self, name):
        self.name = name

    def talk(self, comment):
        print(comment)

newMan = Person("Olayinka")

newMan.talk(f"Hi there, my name is {newMan.name}")