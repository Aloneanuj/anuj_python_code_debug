# Generate a random number between 1 and 100.
import random
guess = int(input("Enter the number : "))

random_number= random.randint(1, 10)
while(guess == random_number):
    if(guess == random_number):
        print("Your guess is wrong. Th Number was : ", random_number)
