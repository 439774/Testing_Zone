# youtuber = "alisher"


# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")


# adj = input("Adjective: ")
# ver1 = input("Verb: ")
# verb2 = input("Verb: ")
# famous_person = input("Famous person: ")

# madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
#     I love to {ver1}. Stay hydrated and {verb2} like you are {famous_person}"

# print(madlib)

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}:"))
        if guess < random_number:
            print('sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high')
        
    print(f'Yay, congrats. You have guess the number {random_number} correctly.')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

        print(f'Yay! The computer guessed your number, {guess}, correctly!')

computer_guess(100)
