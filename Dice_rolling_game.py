import random

decision= input("do you want to roll the dice Y/N? ").upper()
if decision == "Y":
    print(random.randrange(1,6))
    print(random.randrange(1,6))
elif decision == "N":
    print("tanks for playing!")
else: print(" invalid choice")

