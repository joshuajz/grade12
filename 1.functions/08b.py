import math

# Function to ask the user for an integer
def get_int(dialog):
    while True:
        try:
            response = int(input(dialog))
        except ValueError:
            print("Invalid Input")
            continue

        return response


def gallons_paint(sq_ft):
    gallons = sq_ft / 115
    return gallons


def hours_calc(gallons):
    return gallons * 8


def cost_paint(price, gallons):
    return price * gallons


def labor_cost(hours):
    return 20 * hours


def round_extra(gallons):
    decimal_split = str(gallons).split(".")
    decimal = gallons - float(decimal_split[0])
    if decimal >= 0.75:
        return True
    else:
        return False


def main():
    sq_ft = get_int("Square Feet: ")
    price = get_int("Price of Paint per Gallon: ")
    gallons_og = gallons_paint(sq_ft)
    round_bool = round_extra(gallons_og)
    gallons = math.ceil(gallons_og)
    gallons += 1 if round_bool else 0
    hours = hours_calc(gallons)
    cost_of_paint = cost_paint(price, gallons)
    labor = labor_cost(hours)

    total = cost_of_paint + labor

    print(f"Extra Gallon of Paint: {round_bool}")
    print(f"Gallons of Paint Required: {gallons:.2f}")
    print(f"Hours of Labor: {hours:.2f}")
    print(f"Cost of Paint: ${price:.2f}")
    print(f"Labor Charges: ${labor:.2f}")
    print(f"Total Cost of Paint: ${cost_of_paint:.2f}")
    print(f"Total: ${total:.2f}")


main()