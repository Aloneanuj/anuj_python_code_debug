# Q6. Ask number of games played in a tournament. Ask the user number 
# of games won and number of games loss. Calculate number of tie and total Points. (1 win= 4 points, 1 tie =2 points) 
import random
guess=None
ran=0
count=0
while(guess!=ran):
    guess= int(input("Guess your number between 0 to 10: "))
    ran= random.randint(0, 10)
    if(guess>=1 and guess <=10):
        if(guess==ran):
            print("---YOU WIN---:--> ",ran)
            print("your total attempt is : ", count)
            # break

        elif(guess<ran):
            count+=1
            print("Your guess was wrong. It was =>: ", ran)
            print(f"It's your {count} Attempt")

        elif(guess>ran):
            count+=1

            print("Your guess was wrong. it was =>: ", ran)
            print(f"It's your {count} Attempt")
    else:
        print("Please give a valid number between 1 to 10 only")

        


    