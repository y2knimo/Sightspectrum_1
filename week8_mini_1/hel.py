##number guessing game:

import random
print("!!!Welcome to Number Guessing game!!!")
secret_pin = random.randint(1,100)


guess=0
attempts=0
while guess != secret_pin:
    guess=int(input("enter your guess(between 1 to 100):"))
    attempts == 5
    if guess > secret_pin:
        print("too high")
        if attempts == 5:
            print("sorry,something went wrong")
    elif guess <secret_pin:
        print("too low")
print(f"congrats!you guessed the number{secret_pin} correctly in {attempts} attempts ")

