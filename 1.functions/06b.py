def square(charchter, amount):
    for i in range(amount):
        print(charchter, end=" ")
    print()

    for i in range(amount - 2):
        print(charchter, end="")
        for i in range(amount - 2):
            print(" ", end=" ")
        print(" ", end="")
        print(charchter, end="")
        print()

    for i in range(amount):
        print(charchter, end=" ")


square(input("Charchter: "), int(input("Number: ")))
