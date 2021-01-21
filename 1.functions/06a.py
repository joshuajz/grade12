cad_to_eur = 0.64
cad_to_pound = 0.59
cad_to_usd = 0.76
cad_to_peso = 16.21


def eur(cad: float) -> float:
    return cad * cad_to_eur


def pound(cad: float) -> float:
    return cad * cad_to_pound


def usd(cad: float) -> float:
    return cad * cad_to_usd


def peso(cad: float) -> float:
    return cad * cad_to_peso


def main():
    while True:
        try:
            amnt = float(input("How much would you like to convert? "))
        except ValueError:
            print("Invalid Input")
            continue

        try:
            currency = int(
                input("What currency? 1. Euro | 2. Pound | 3. USD | 4. Peso ")
            )
        except ValueError:
            print("Invalid Input")
            continue

        if not (1 <= currency and currency <= 4):
            print("Invalid Input (1-4)")
            continue

        break

    if currency == 1:
        print(f"${amnt} is {eur(amnt)} in Euros.")
    elif currency == 2:
        print(f"${amnt} is {pound(amnt)} in Pounds.")
    elif currency == 3:
        print(f"${amnt} is ${usd(amnt)} USD.")
    elif currency == 4:
        print(f"${amnt} is {peso(amnt)} in Pesos.")

    while True:
        try:
            cont = int(input("Continue? 1. Yes | 2. No "))
        except ValueError:
            print("Invalid Input")
            continue

        if cont not in [1, 2]:
            print("Invalid input")
            continue

        break

    if cont == 1:
        main()
    else:
        print("Goodbye")
        return


main()