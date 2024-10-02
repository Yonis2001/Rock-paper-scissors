import random

user_wins=0
computer_wins=0

choice =["rock" ,"paper","scissors"]
choice[0]
while True:
    user_input= input("Choose Rock/Paper/Scissors or press E to exit ").lower()
    if user_input =="e":
        break
    if user_input not in ["rock" ,"paper","scissors"]:
        continue #Continue makes the user try again .Not in checks if what the user wrote is not valid

    random_number = random.randint(0,2)
    #rock:0,paper:1,scissors:2
    computer_guess = choice[random_number]
    print("Computer chose",computer_guess+".")
    

    if user_input == "rock" and computer_guess=="scissors":
        print("You won!")
        user_wins+=1
    
    elif user_input == "paper" and computer_guess=="rock":
        print("You won!")
        user_wins+=1
    elif user_input == "scissors" and computer_guess=="paper":
        print("You won!")
        user_wins+=1
    else:
        print("You lost")
        computer_wins+=1



print("You scored",user_wins,"wins")
print("computer scored",computer_wins,"wins")
print("Bye")