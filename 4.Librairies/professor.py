import random
import sys

def main():

    level = int(get_level("Level: ")) # Prompt the user to enter a level (1, 2 or 3) until a valid entry is received.

    attempts = 0
    good_answers = 0
    wrong_answers = 0

    while True:
        try:
            if good_answers + wrong_answers != 10: # Number of problems less than 10
                attempts = 0
                x = generate_integer(level) # Generate a random x between 0 and 9
                y = generate_integer(level) # Generate a random y between 0 and 9

                while attempts < 4: # Number of attempts between 1 and 3
                    try:
                        answer = int(input(f"{x} + {y} = "))

                        if answer == (x + y):
                            good_answers += 1
                            break
                        elif attempts == 2:
                            wrong_answers += 1
                            print(x+y)
                            break
                        else:
                            print("EEE")
                            attempts += 1

                    except ValueError:
                        pass
                    except EOFError:
                        break
                    except:
                        pass
            else:
                return print(good_answers)

        except EOFError:
            break
        except ValueError:
            pass



def generate_integer(level): # Return a randomly generated non-negative integer with the number of digits specified according to the level.

    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level ==3:
        return random.randint(100,999)
    else:
        raise ValueError

def get_level(l): # Validate user level entry, returning 1, 2 or 3.
        while True:
            try:
                level = int(input(l))

                if 0 < level < 4: # Check the validity of the level requested.
                    return level
                else:
                    raise ValueError
            except ValueError:
                print("value error")
                pass
            except EOFError:
                break






if __name__ == "__main__":
    main()




