

def main():
    greeting = input("Greeting: ").strip().lower()
²   value = value(greeting)
    print(f"${value}")


def value(greeting):

    firstletter = answer[0]
    greeting = greeting.strip().lower()
    if greeting == "hello" or greeting.startswith("hello"):
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
