def main():

    percentage = userfraction()
    if  0 >= percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

def userfraction():
    while True:
        try:

            fraction = input("Fraction: ") # Demander d'entrer une fraction
            x, y = fraction.split("/") # Split l'input X/Y

            x = int(x)
            y = int(y)
            if x <= y: # Si x est inférieur ou égal
                return int(round((x*100)/y)) # Convertir et retourner la fraction en pourcentage arrondi à l'intégral le plus proche

        except (ValueError, ZeroDivisionError) as e:
            print(f"{e}")

        except x > y:
            pass

main()

