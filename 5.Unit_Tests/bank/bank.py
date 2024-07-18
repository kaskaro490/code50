

def main():
answer = input("Greeting: ").strip().lower()
firstletter = answer[0]

if answer == "hello" or answer.startswith("hello"):
    print("$0")
elif answer[0] == "h":
    print("$20")
else:
    print("$100")



def value(greeting):
    ...


if __name__ == "__main__":
    main()
