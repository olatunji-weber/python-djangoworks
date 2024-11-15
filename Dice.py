import random

class Dice:
    def roll_dice(self):
        num1 = random.randint(1,6)
        num2 = random.randint(1,6)
        return  (num1, num2)


roller = Dice()
print( f"You rolled: { roller.roll_dice() }" )
