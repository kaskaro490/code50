def main():

    percentage = userfraction()
    if 0 == percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

def userfraction():
    while True:
        try:
            # demander d'entrer une fraction
            fraction = input("Fraction: ")
            # Split l'input X/Y
            x, y = fraction.split("/")
            if not x > y:
                x = int(x)
                y = int(y)

                # Convertir la fraction en pourcentage arrondi à l'intégral le plus proche

                return int(round((x*100)/y))


            # Boucler et redemander un input si l'input est supérieur à 100% ou en cas de  ZeroDivisionError et ValueError

        except (ValueError, ZeroDivisionError) as e:
            print(f"{e}")



main()

