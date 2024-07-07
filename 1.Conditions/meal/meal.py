
def main():
    usertime = input("What time it is? ")
    x,y = usertime.split(":")
    x = int(x)
    y = int(y)

    answer = time.wichmeal()
    print(answer)

def convert(time):
    yfloat = float(((y*100)/60)/100)
    time = float(x + yfloat)

def wichmeal(time):
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


if __name__ == "__main__":
    main()
