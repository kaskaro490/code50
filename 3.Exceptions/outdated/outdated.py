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

    while True:
        try:
        # Demander à l'utilisateur d'entrer une date au format `MM/DD/YYYY` ou `Month DD, YYYY`.
                userdate = input("Date: ").title()
                print(f"{userdate}")
                result = check_date(userdate, months)
                year, month, day = result

                print(f"{year}-{month}-{day}")
        except EOFError:
                break
        #except:
         #      print("error") # Si l'entrée n'est pas valide, demander de nouveau à l'utilisateur jusqu'à obtenir une date valide.




# Vérifier si l'entrée de l'utilisateur correspond à l'un des deux formats de date (numérique ou textuel).
def check_date(userdate, months):
    pattern = r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(\d{4})$' # S'assurer que les mois et les jours sont formatés avec deux chiffres, en ajoutant des zéros non significatifs si nécessaire (par exemple, "9" devient "09").
    pattern2 = rf'({"|".join(months)}) ([1-9]|[12][0-9]|3[01]), (\d{4})$'
    print("fonction on")
    # Si la date est au format `MM/DD/YYYY`, la diviser en trois parties : mois, jour et année.
    if re.match(pattern, userdate, re.IGNORECASE):
        match = re.match(pattern, userdate, re.IGNORECASE)
        month = match.group(1)  # Mois
        day = match.group(2)  # Jour
        year = match.group(3)  # Année




    # Si la date est au format `Month DD, YYYY`, convertir le mois en son équivalent numérique (par exemple, "January" en "01").
    elif re.match(pattern2, userdate, re.IGNORECASE):
        match = re.match(pattern2, userdate, re.IGNORECASE)
        month_word = match.group(1)  # Mois en lettres
        month = months.index(month_word.title()) + 1  # Convertir le nom du mois en numéro
        day = match.group(2)  # Jour
        year = match.group(3)  # Année

    return year, month, day



main()
