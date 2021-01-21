def totals(total=0):
    num = input("Enter a Number: ")
    try:
        num = int(num)
    except ValueError:
        if num == "":
            print("Final Total:", total)
            return total

    total = total + num
    print("Total:", total)
    totals(total)


totals()