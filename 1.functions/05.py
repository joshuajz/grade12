def hello():
    while True:
        while True:
            try:
                lang = int(
                    input("Choose a language: 1. English | 2. French | 3. Spanish ")
                )
            except ValueError:
                print("Invalid Input (1-3)")
                continue

            if not (1 <= lang and lang <= 3):
                print("Invalid Input (1-3)")
                continue

            break

        if lang == 1:
            print("The word is 'Hello'")
        elif lang == 2:
            print("The word is 'Bonjour'")
        elif lang == 3:
            print("The word is 'Hola'")

        try:
            cont = int(input("Continue? 1. Yes | 2. No "))
        except ValueError:
            print("Invalid Input (1-2)")
            continue

        if cont not in [1, 2]:
            print("Invalid Input (1-2)")
            continue

        if cont == 1:
            continue
        elif cont == 2:
            return


hello()