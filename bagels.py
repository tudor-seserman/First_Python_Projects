import random

#print(
'''
Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
I have thought up a number.
 You have 10 guesses to get it.
 '''#)
#number=str(random.randint(100,999))
guess_counter=1

def Rdigit1(guess, number):
    ' '.join(['Pico' for x in guess if x in number])

    

def Pdigit(guess, number):
    ' '.join(['Fermi' for x in range(len(number)) if number[x] == guess[x]])




def main(guess_counter):
    number=str(random.randint(100,999))
    print(number)
    for x in range(10):
        print(f'Guess #{guess_counter}:')
        guess_counter += 1
        guess = input()
        if guess == number:
            return print('You got it!\nDo you want to play again? (yes or no)')
        elif bool([x for x in range(len(number)) if number[x] == guess[x]]) == True:
            print(' '.join(['Fermi' for x in range(len(number)) if number[x] == guess[x]]))
            #print(Pdigit(guess, number))
            continue
        elif bool([x for x in guess if x in number]) == True:
            print(' '.join(['Pico' for x in guess if x in number]))
            continue
        else:
            print('Bagels')
    return print('You did not get it.\nDo you want to play again? (yes or no)')
main(guess_counter)
while input() == 'yes':
    main(guess_counter)

