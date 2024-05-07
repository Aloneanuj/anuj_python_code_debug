import random
option = ["rock", "paper", "scissor"]
computer_guess = random.choice(option)
user_guess: str = input("Enter your option: ")

if user_guess =="rock" and computer_guess == "paper" :
    print(f"computer win, it was {computer_guess}")
elif user_guess =="paper" and computer_guess == "rock":
    print(f"computer win, it was {computer_guess}")
elif user_guess =="scissor" and computer_guess == "paper":
    print(f"computer win, it was {computer_guess}")
elif user_guess == computer_guess:
    print("----You WON--------")
else:
    print("Please enter a valid value")
