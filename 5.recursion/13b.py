def star(maxval, start=1):
    if start == maxval:
        return
    else:
        print("*" * start)
        star(maxval, start=start + 1)


amount = int(input("N: "))
star(amount)