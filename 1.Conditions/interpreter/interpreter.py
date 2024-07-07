def main():

    expression = input("Expression: ")

    x, y, z = expression.split(" ")
    x = float(x)
    z = float(z)

    result = interpreter(x, y, z)

    print(result)


def interpreter(x, y, z):
    if y == "+":
        return x + z
    elif y == "-"
        return x - z
    elif y == "*"
        return x * z
    elif y == "/"
        if z >= 0
            return x / z
        else: print(")


main()


