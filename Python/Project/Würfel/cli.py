import random


def roll():
    dy = random.randint(1, 6)
    print(dy)


while True:
    roll()
    print("Roll again? (Yes/No)")
    ask = input()
    if ask in ("Yes", "yes", "y"):
        continue
    else:
        print("Then fuck off!")
        break
