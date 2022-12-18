import random

# print(
# '''
# Bagels, a deductive logic game.
# By Al Sweigart al@inventwithpython.com
# I am thinking of a 3-digit number. Try to guess what it is.
# Here are some clues:
# When I say:    That means:
#   Pico         One digit is correct but in the wrong position.
#   Fermi        One digit is correct and in the right position.
#   Bagels       No digit is correct.
# I have thought up a number.
#  You have 10 guesses to get it.
#  ''')

def fermi(number, guess):
    count=0
    for x in range(3):
         if number[x] == guess[x]:
            count+=1
    return count


def pico(number, guess):
    count=0
    for x in guess:
        if x in number:
            count+=1
    return count

guess = input()

def main(number, guess, guess_counter):
    #number=str(random.randint(100,999))
    #print(number)
    for x in range(10):
        print(f'Guess #{guess_counter}:')
        guess_counter += 1
       # if len(guess) != 3 or guess.isdigit() == False:
       #    return f"{guess} is not a 3 digit number, please try again."
        if guess == number:
            return 'You got it!\nDo you want to play again? (yes or no)'
        elif fermi(number, guess) > 0:
            return "Fermi" * fermi(number, guess)
        elif pico(number, guess) > 0:
            return 'Pico' * pico(number, guess)
        else:
            return 'Bagels'
    return 'You did not get it.\nDo you want to play again? (yes or no)'
#print(main(guess_counter))

# while input() == 'yes':
#     main(guess_counter)

