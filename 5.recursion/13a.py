def sum_vals(number):
    if number == 0:
        return 0
    else:
        return number % 10 + sum_vals(number // 10)


number = int(input("Enter number: "))
print(sum_vals(number))