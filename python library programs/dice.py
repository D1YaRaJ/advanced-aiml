import random

n=input("Type roll to roll the dice:")
if n=="roll":
    num=random.randint(1,6)
    print("number on dice is:",num)
else:
    print("Invalid input")