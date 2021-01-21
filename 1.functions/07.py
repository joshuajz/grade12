import random

# Function to ask the user for an integer
def get_int(dialog):
    while True:
        try:
            response = int(input(dialog))
        except ValueError:
            print("Invalid Input")
            continue

        return response


def main():
    N = get_int("How many people are in the party? ")
    cost = random_total(N)

    print("Reciept:\n__________________")
    for i in range(N):
        print(f"Person {i}: ${cost[i]:.2f}")
    print("__________________")

    print(f"Auto Gratuity: {'0%' if N < 8 else '15%'}")
    subtotal = sum(cost) * (1 if N < 8 else 1.15)
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Taxes: ${subtotal * 0.13:.2f}")
    print(f"Total: ${subtotal * 1.13:.2f}")
    total = subtotal * 1.13

    tip = input("Would you like to tip a percentage (%) or a dollar amount ($): ")
    if tip == "%":
        tip_amnt = get_int("Percentage: ")
        total *= 1 + (tip_amnt * 0.01)
    else:
        tip_amnt = get_int("$")
        total += tip_amnt

    print(f"Total w/ Tip: ${total:.2f}")


def random_total(N):
    total = []
    for i in range(N):
        total.append(random.randint(12, 20) + (random.randint(0, 99) * 0.01))
    return total


main()