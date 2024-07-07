answer = input("Greeting: ").strip()
firstletter = answer[0]

if answer == "hello":
    print("$100")
elif answer[0] == "h":
    print("$20")
else:
    print("$0")
