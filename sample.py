import random#import random

def run_guess(guess, answer):
    if 0 < guess < 11:
        if  guess == answer:
            print('you are a genius')
            return True
        else:
            print('please enter from 1~10')

#ask the inout from the user
#chaec,  whetehr  the input is 1~10
answer= random.randint(1,10)
while True:
    try:
        guess = int(input('guess  the input number from 1~10 : '))
        if (run_guess(guess,answer)):
            break

    except ValueError:
        print('please enter a  number')
        continue
