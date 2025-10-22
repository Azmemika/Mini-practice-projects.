import random

def guess():
    random_number = random.randint(1, 10)
    while True:
        gu = int(input("Guess the number between 1 and 10: "))
        if gu == random_number:
            print("You have guessed it!")
            break
        elif gu > random_number:
            print("You're too high")
            continue
        elif gu < random_number:
            print("You're too low")
            continue
        elif gu > 10 and gu < 1:
            print("Enter between 1 and 10")
            continue
        else:
            continue
    
    return

guess()
