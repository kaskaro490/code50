import random

def main():

# Prompts the user for a level int . If the user does not input a positive integer, the program should prompt again.
    while True:
        try:
            level = int(input("Level: "))
            num2guess = random.randint(1, level) # Randomly generates an integer between 1 and level
            guess = int(input("Guess: "))

                if guess == num2guess:
                    print("Just right!")
                elif guess < num2guess
                    print("Too small!")
                elif guess > num2guess:
                    print("Too large!")
        except guess < 1:
            pass
        except guess != int:
            pass


# If the user does not input a positive integer, the program should prompt again.

# inclusive, using the random module.
# Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
# If the guess is larger than that integer, the program should output Too large! and prompt the user again.
# If the guess is the same as that integer, the program should output Just right! and exit.



main()
