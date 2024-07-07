def main():
  okcoins = ["5","10","25"]
  due = 50
  while due > 0:
    insert_coin = int(input("Insert a coin: "))
    if insert_coin in okcoins:
      due -= insert_coin
      print("Amount due: " + due)
  if due <= 0:
    print("Change owed: " + due.abs())


main ()
