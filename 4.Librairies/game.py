import random

def main():

# Prompts the user for a level int . If the user does not input a positive integer, the program should prompt again.
    while True:
        try:
            level = int(input("Level: "))
            num2guess = random.randint(1, level) # Randomly generates an integer between 1 and level
            guess = int(input("Guess: "))
            if not guess < 1:
                if guess == num2guess:
                    print("Just right!")
                    sys.exit()
                elif guess < num2guess:
                    print("Too small!")
                elif guess > num2guess:
                    print("Too large!")

        except ValueError:
            pass


main()
