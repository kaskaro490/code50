def main():
  okcoins = [5,10,25]
  due = 50
  while due > 0:
    insert_coin = int(input("Insert a coin: "))
    if insert_coin in okcoins:
      due -= int(insert_coin)
      print(f"Amount Due: {due}")
    else:
      print(f"Amount Due: {due}")
  if due <= 0:
    print(f"Change Owed: {abs(due)}")

main()
