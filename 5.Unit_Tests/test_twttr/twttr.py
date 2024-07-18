def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(word, vowels=None):
    if vowels is None:
        vowels = ["a","e","i","o","u","A","E","I","O","U"]

    outputlist = []
    for letter in word:
        if letter not in vowels:
            outputlist.append(letter)

    return ''.join(outputlist)

if __name__ == "__main__":
    main()
