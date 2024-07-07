
def main():
    time = convert(input("What time it is? "))

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    x,y = time.split(":")
    x = int(x)
    y = int(y)
    yfloat = float(((y*100)/60)/100)
    return float(x + yfloat)



if __name__ == "__main__":
    main()
