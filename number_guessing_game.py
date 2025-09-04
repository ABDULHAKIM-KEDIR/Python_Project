import random
random_number = random.randint(1, 100)
while True:
    try:
        number = int(input("Guess the number between 1 and 100: "))
        if random_number > number:
            print("Too high!")

        elif random_number < number:
            print("Too low!")

        else:
            print("Congratulations! You guessed the number. ")
            break
    except ValueError:
        print("please enter a valid number ")
