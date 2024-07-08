def main():

    try:
        # demander d'entrer une fraction
        fraction = input("Fraction: ")
        # Split l'input en X/Y
        x, y = fraction.split("/")
        x = int(round(x))
        y = int(round(y))
        print(f"{x} and {y}")

        # Convertir la fraction en pourcentage arrondi à l'intégral le plus proche
        percentage = (x*100)/y


        # Boucler et redemander un input si l'input est supérieur à 100% ou en cas de  ZeroDivisionError et ValueError

    except:
        print("error")

    else:
        print(f"{percentage}%")

main()

