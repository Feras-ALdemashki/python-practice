import random
options = ["rock","paper","scissors"]

random_number= random.randrange(len(options))

 

while True :
 U_choice = input("R P C ? ").upper()
 C_guess = options[random_number]
 if( U_choice not in ("R","P","C") ):
    print("not a valid input"), 
 elif(C_guess == "rock" and U_choice == "C" or C_guess == "scissors" and U_choice == "P" or C_guess == "paper" and U_choice == "R"):
    print(f'computer choose {C_guess} you choose {U_choice} computer won! ')
 elif(C_guess == "rock" and U_choice == "P" or C_guess == "scissors" and U_choice == "R" or C_guess == "paper" and U_choice == "C"):
    print(f'computer choose {C_guess} you choose {U_choice} you won! ') 
 else: print("its a draw")
 play_again = input("do you want to play again N/Y ? ").upper()
 if( play_again not in ("Y","N") ):
    print("not a valid input")
 elif(play_again == "N"): break