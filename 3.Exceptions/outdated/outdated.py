import re

def main():

    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

    year = 0
    month = 0
    day = 0

    while True:
        try:
        # Demander à l'utilisateur d'entrer une date au format `MM/DD/YYYY` ou `Month DD, YYYY`.
                userdate = input("Date: ")
                check_date(userdate, months)


        except EOFError:
                break
        except:
                pass # Si l'entrée n'est pas valide, demander de nouveau à l'utilisateur jusqu'à obtenir une date valide.




# Vérifier si l'entrée de l'utilisateur correspond à l'un des deux formats de date (numérique ou textuel).
def check_date(userdate, months):
    pattern = r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(\d{4})$' # S'assurer que les mois et les jours sont formatés avec deux chiffres, en ajoutant des zéros non significatifs si nécessaire (par exemple, "9" devient "09").
    pattern2 = rf'({months.title()}) ([1-9]|[12][0-9]|3[01]), (\d{4})$'
    print("fonction on")
    # Si la date est au format `MM/DD/YYYY`, la diviser en trois parties : mois, jour et année.
    if re.match(pattern, userdate, re.IGNORECASE):
        month = pattern.group(1)  # Mois
        day = pattern.group(2)  # Jour
        year = pattern.group(3)  # Année

        return year, month, day


    # Si la date est au format `Month DD, YYYY`, convertir le mois en son équivalent numérique (par exemple, "January" en "01").
    elif re.match(pattern2, userdate, re.IGNORECASE):
        month_word = pattern2.group(1)  # Mois en lettres
        month = months.index(month_word.title()) + 1  # Convertir le nom du mois en numéro
        day = pattern2.group(2)  # Jour
        year = pattern2.group(3)  # Année

        return year, month, day

    else:
        return False










# Afficher la date au format `YYYY-MM-DD`.

# Utiliser des méthodes de chaînes de caractères comme `split`.
# Utiliser des méthodes de liste comme `index`.
# Utiliser la syntaxe de formatage des chaînes pour ajouter des zéros non significatifs.



main()
