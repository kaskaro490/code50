def main():

    percentage = userfraction()
    if percentage == 0:
        print("E")
    elif percentage > 99:
        print("F")
    else:
        print(f"{percentage}%")

def userfraction():
    while True:
        try:
            # demander d'entrer une fraction
            fraction = input("Fraction: ")
            # Split l'input en X/Y
            x, y = fraction.split("/")
            x = float(x)
            y = float(y)

            # Convertir la fraction en pourcentage arrondi à l'intégral le plus proche
            percentage = int(round((x*100)/y))


            # Boucler et redemander un input si l'input est supérieur à 100% ou en cas de  ZeroDivisionError et ValueError

        except (ValueError, ZeroDivisionError) as e:
            print(f"{e}")

        else:
            break
    return percentage

main()

