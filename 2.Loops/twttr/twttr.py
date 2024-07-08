def main():
   vowels = ["a","e","i","o","u"]
   userinput = input("Input: ")
   outputlist = twttr(input, vowels )
   print(outputlist)
def twttr(userinput, vowels ):
   outputlist = []
   for letter in userinput:
      if not letter in vowels:
         outputlist.append(letter)

   return ''. join(outputlist)

main()
