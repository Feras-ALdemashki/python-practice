import random
import string


while True:
    
    try:
        password_length = int(input("How long is the password? Please provide a number: "))
        if password_length <= 4:
            print("password must be at least 4 character.")
            continue
        elif password_length > 20:
            print("password cant be more than 20 character")
            continue
    except ValueError:
        print("Please enter a whole number.")
        continue

  
    while True:
        special_characters = input("Should contain special characters? (Y/N): ").strip().upper()
        if special_characters in ("Y", "N"):
            break
        print("Please enter Y or N only.")

    
    while True:
        upper_case = input("Should contain upper case? (Y/N): ").strip().upper()
        if upper_case in ("Y", "N"):
            break
        print("Please enter Y or N only.")

   
    while True:
        digit = input("Should contain digits? (Y/N): ").strip().upper()
        if digit in ("Y", "N"):
            break
        print("Please enter Y or N only.")


    break

print(password_length, special_characters, upper_case, digit)


def password_generator(password_length,special_characters,upper_case,digit):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    special = string.punctuation
    digits = string.digits
    password = []
    if special_characters == "Y":
        password.append(random.choice(special))
    if upper_case == "Y":
        password.append(random.choice(upper))
    if digit == "Y" :
        password.append(random.choice(digits))
    remaining_length =  password_length - len(password) 
    password.extend(random.sample(lower,remaining_length))
    random.shuffle(password)
    password_str = "".join(password) 
    print(password_str)


password_generator(password_length,special_characters,upper_case,digit)