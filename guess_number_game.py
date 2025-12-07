import random

magic_number = random.randint(1, 100)  # pick the number once, outside the loop

while True:
    answer = input("Guess the number (1–100): ")

    # check if input is a valid integer
    if not answer.isdigit():
        print("Please enter a valid number!")
        continue  # go back to the start of the loop

    guess = int(answer)

    if guess > magic_number:
        print("Think lower")
    elif guess < magic_number:
        print("Think higher")
    else:
        print(f"Nice! The number is {magic_number}")
        break  # stop the loop when the guess is correct
