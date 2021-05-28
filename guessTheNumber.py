import random

number = random.randint(1, 100)
countOfTries = 0
guess = None
print(number)

while(guess != number):
    countOfTries += 1
    print("Let's play a game. Guess the number from 1 to 100: ", end = '')
    guess = int(input())
    if guess > number:
        print("Your guess is too high. Try one more time:")
    elif guess < number:
        print("Your guess is too low. Try one more time:")
    else:
        print(f"Congratulations. You've guessed the number in the {countOfTries} try.")        