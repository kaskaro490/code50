def main():

    expression = input("Expression: ")

    x, y, z = expression.split(" ")
    x = float(x)
    z = float(z)

    print(expression)


def interpreter(x, y, z):
    if y == "+":
        return x + z

main()


