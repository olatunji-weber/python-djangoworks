class Mamal:
    def walk(self):
        return "Walking...."

class Dog(Mamal):
    pass

class Cat(Mamal):
    pass

bingo = Dog()
print(f"The dog is {bingo.walk()}")
kitty = Cat()
print(f"The cat is {kitty.walk()}")