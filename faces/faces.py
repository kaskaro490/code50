
def convert(answer,replacements):

    convert_table = str.maketrans(replacements)
    return answer.translate(convert_table)

replacements = {
":)":"🙂",
":(":"😐",
}

answer = input("Common say something:")
answernew = convert(answer,replacements)
print("answernew")

