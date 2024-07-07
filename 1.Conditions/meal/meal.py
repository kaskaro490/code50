
def main():
    usertime = input("What time it is? ")
    x,y = usertime.split(":")
    x = int(x)
    y = int(y)

    answer = wichmeal()
    print(answer)

def convert(time):
    yfloat = float(((y*100)/60)/100)
    time = float(x + yfloat)

def wichmeal(floattime):
    if 7 <= floattime <= 8:
        print("breakfast time")
    elif 12 <= floattime <= 13:
        print("lunch time")
    elif 18 <= floattime <= 19:
        print("dinner time")


if __name__ == "__main__":
    main()
