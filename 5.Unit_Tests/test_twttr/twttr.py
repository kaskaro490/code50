def main():
   #vowels = ["a","e","i","o","u","A","E","I","O","U"]
   word = input("Input: ")
   print(shorten(word, vowels))



def shorten(word, vowels):

   outputlist = []
   for letter in word:
      if not letter in vowels:
         outputlist.append(letter)

   return ''.join(outputlist)

if __name__ == "__main__":
    main()
