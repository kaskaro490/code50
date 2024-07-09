def main():

    percentage = userfraction()
    if  percentage <= 1:
        print("E")
    if percentage >= 99:
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
            if x <= y: # Si x
                return int(round((x*100)/y)) # Convertir et retourner la fraction en pourcentage arrondi à l'intégral le plus proche

        except (ValueError, ZeroDivisionError) as e:
            print(f"{e}")

        except x > y:
            pass

main()

