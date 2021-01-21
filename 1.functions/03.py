def pizza(num):
    print("Welcome to Python Pizza!")

    for i in range(1, num + 1, 1):
        while True:
            toppings = input("How many toppings on pizza #" + str(i) + "? ")

            try:
                toppings = int(toppings)
            except ValueError:
                print("Invalid Input.")
                continue

            top = "toppings" if toppings > 1 else "topping"

            print(
                f"A Pizza with {toppings} {top} costs ${float(8 + (toppings * 0.75))}"
            )
            break


pizza(3)