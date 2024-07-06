def main():

    answer = input("Common say something:")
    print(answer.convert(answer))


def convert(answer):

    answer = answer.replace(":)","🙂")
    answer = answer.replace(":(","😐")
    return answer


main()
