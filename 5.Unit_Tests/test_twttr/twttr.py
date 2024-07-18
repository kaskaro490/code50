def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    vowels = "aeiouAEIOU"
    return ''.join([letter for letter in word if letter not in vowels])

if __name__ == "__main__":
    main()
