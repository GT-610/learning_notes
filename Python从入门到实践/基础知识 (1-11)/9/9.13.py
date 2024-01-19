from random import randint

class Die:
    def __init__(self,sides):
        self.sides=sides

    def roll_die(self):
        self.sides=randint(1,self.sides)

die1=Die(6)
for i in range(0,10):
    die1.roll_die()
    print(die1.sides)

die2=Die(10)
for i in range(0,10):
    die2.roll_die()
    print(die2.sides)

