 #! Initializing the ball position
ballPosition = [' ', 'O', ' ']

#! Shuffle the ball position
from random import shuffle
def shuffle_ball(ballList):
    shuffle(ballList)
    return ballList

#! Get user guess
def user_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input('Enter your guess (0,1,2): ')
    return int(guess)

#! Check user guess with the ball position
def check_guess(ballList, guess):
    if ballList[guess] == 'O':
        print("Hurray, you win!")
        print(ballList)
    else:
        print("Better luck next time!")
        print(ballList)
        core_game()

#! Complete Gamwe
def core_game():
    ballList = shuffle_ball(ballPosition)
    userGuess = user_guess()
    check_guess(ballList, userGuess)

#* Function Call
core_game()