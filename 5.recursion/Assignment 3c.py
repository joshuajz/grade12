def square(length, symbol):
    print(f"{symbol} " * length)
    for i in range(length - 2):
        print(f"{symbol} {'  ' * (length - 2)}{symbol}")
    print(f"{symbol} " * length)

    inc_dec = int(
        input(
            "Would you like to 1) Increase or 2) Decrease the size of the shape?  Type 3 for Quit "
        )
    )
    if inc_dec == 1:
        square(length + int(input("Increase Amount: ")), symbol)
    elif inc_dec == 2:
        square(length - int(input("Decrease Amount: ")), symbol)
    else:
        return


length = int(input("Length of Square: "))
symbol = input("Symbol: ")
square(length, symbol)
print("Quitting.")