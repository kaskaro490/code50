def main():
   vowels = ["A","E","I","O","U","a","e","i","o","u"]
   input = input("Input: ")
   outputlist = twttr(input, vowels )
   print(outputlist)
def twttr(input):
   outputlist = []
   for letter in input:
      if not letter in vowels:
         outputlist.append(letter)

   return ''. join(outputlist)

main()
