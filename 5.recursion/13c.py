def common_denom(num1, num2, divide):
    # print(num1, num2, divide)
    if divide == 0:
        print("No Lowest Common Denominator")
    elif num1 % divide == 0 and num2 % divide == 0:
        print("Lowest Common Denominator: ", divide)
    else:
        common_denom(num1, num2, divide - 1)


n1 = int(input("n1: "))
n2 = int(input("n2: "))
common_denom(n1, n2, n1 * n2)