import random


def start():
    nr = random.randint(1, 6)
    print("Guess the number!")
    ask = int(input())
    while True:
        if ask == nr:
            print("Congratulations the number was", nr)
            break
        else:
            if ask >= nr:
                print("Lower")
                ask = int(input())
            else:
                print("Higher")
                ask = int(input())


start()
print("Do you want to try again? (Yes/No)")
ask2 = input()
while ask2 in ("Yes", "yes", "y"):
    start()
    print("Do you want to try again? (Yes/No)")
    ask2 = input()
print("Bye bye!")
