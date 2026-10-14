# We are going to write a program that generates a random number and asks the user to guess it.If the players guess is lower than the actual number,the program displays "Lower".similarly,if the player's guess is higher than the actual number,the program displays "Higher". when the user guesses the correct number the program displays the number of guesses the user took to guess the number correctly.


import random
n = random.randint(1,520)
a = -1
guesses = 0
while(a!=n):
    guesses += 1
    a = int(input("Guess the number: "))

    if(a>n):
        print("Lower number please")
    else:
        print("Higher number please")





print(f"You guessed it right in {guesses} guesses!")

# Another way to do this by using for loop is the following:

import random

n = random.randint(1, 100)
max_guesses = 1000  # Set a high upper limit for allowed guesses

for guesses in range(1, max_guesses + 1):
    a = int(input("Guess the number: "))
    
    if a == n:
        print(f"You guessed it right in {guesses} guesses!")
        break  # Stops the loop immediately when the guess is correct
    elif a < n:
        print("Higher number please")  #  if input is lower, prompt for a higher number
    else:
        print("Lower number please")  # if input is higher, prompt for a lower number
