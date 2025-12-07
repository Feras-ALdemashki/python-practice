import random

magic_number = random.randint(1, 100)  

while True:
    answer = input("Guess the number (1–100): ")

    if not answer.isdigit():
        print("Please enter a valid number!")
        continue  

    guess = int(answer)

    if guess > magic_number:
        print("Think lower")
    elif guess < magic_number:
        print("Think higher")
    else:
        print(f"Nice! The number is {magic_number}")
        break  
