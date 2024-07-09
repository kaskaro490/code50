def main():

    percentage = userfraction()
    if  0<= percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

def userfraction(): # Fonction de conversion de fraction en pourcentage arrondi
    while True:
        try:

            fraction = input("Fraction: ") # Demander d'entrer une fraction
            x, y = fraction.split("/") # Split l'input X/Y

            x = int(x)
            y = int(y)
            if x <= y: # Si x est inférieur ou égal à y, envoyer le résultat
                return int(round((x*100)/y)) # Convertir et envoyer le résultat arrondi à l'intégral le plus proche

        except (ValueError, ZeroDivisionError) as e:
            pass

        except x > y:
            pass

main()

