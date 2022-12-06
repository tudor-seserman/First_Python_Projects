import random

print(
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
 ''')



guess_counter=1

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

def main(guess_counter):
    number=str(random.randint(100,999))
    print(number)
    for x in range(10):
        print(f'Guess #{guess_counter}:')
        guess_counter += 1
        guess = input()
        if len(guess) != 3 or guess.isdigit() == False:
            print(f"{guess} is not a 3 digit number, please try again.")
            continue
        if guess == number:
            return print('You got it!\nDo you want to play again? (yes or no)')
        elif fermi(number, guess) > 0:
            print("Fermi" * fermi(number, guess))
            continue
        elif pico(number, guess) > 0:
            print('Pico' * pico(number, guess))
            continue
        else:
            print('Bagels')
    return print('You did not get it.\nDo you want to play again? (yes or no)')
main(guess_counter)
while input() == 'yes':
    main(guess_counter)

