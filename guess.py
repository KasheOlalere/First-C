print ('Welcome')
print ('What is your name: ')
name = input()
print ('Hello '+ name)
import random
number = random.randint(1,20)
guessTaken = 0
while guessTaken < 6:
        print ('Take a Guess:')
        guess = input()
        guess = int(guess)
        guessTaken = guessTaken + 1
        if guess > number + 5:
                print ('Your guess is too high')
        elif guess > number:
                print ('You are close,Try again')
        elif guess < number -5:
                print ('Your guess is too low')
        elif guess < number:
                print('You are close, Try again')
        elif guess == number:
                break
if guess== number:
        guessTaken = str(guessTaken)
        print ('You guessed my number in ' +guessTaken + ' tries')
if guess!= number:
        print ('nice try, but the number i was thinking of was '+ number)
            
