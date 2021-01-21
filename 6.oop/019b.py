class Bank:
    bal = 0.00

    def deposit(self, amount):
        Bank.bal += amount
        print(f"New Balance: ${Bank.bal}")

    def withdrawl(self, amount):
        if Bank.bal - amount <= 0:
            print("Invalid Withdrawl.  Would less than or equal to 0.")
        else:
            Bank.bal -= amount
            print(f"New Balance: ${self.bal}")

    def banking(self):
        while True:
            interaction = input("Interaction (deposit/withdraw): ")
            if interaction == "deposit":
                self.deposit(int(input("Amount to deposit: $")))
            elif interaction == "withdraw":
                self.withdrawl(int(input("Amount to withdraw: $")))
            else:
                break


x1 = Bank()
x2 = Bank()
print(f"Bank Account Created.  Current Balance: {x1.bal}")
x1.banking()

print(f"x1: {x1.bal} | x2: {x2.bal}")