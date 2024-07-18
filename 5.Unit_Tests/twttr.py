def main():
   vowels = ["a","e","i","o","u","A","E","I","O","U"]
   word = input("Input: ")
   #outputlist = twttr(input, vowels )
   print(twttr(userinput, vowels))



def shorten(word, vowels):

#def twttr(userinput, vowels ):
   outputlist = []
   for letter in word:
      if not letter in vowels:
         outputlist.append(letter)

   return ''.join(outputlist)

if __name__ == "__main__":
    main()
