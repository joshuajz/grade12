class bank:
    def __init__(self):
        self.bal = 0.00

    def deposit(self, amount):
        self.bal += amount
        print(f"New Balance: ${self.bal}")

    def withdrawl(self, amount):
        if self.bal - amount <= 0:
            print("Invalid Withdrawl.  Would less than or equal to 0.")
        else:
            self.bal -= amount
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


x = bank()
print(f"Bank Account Created.  Current Balance: {x.bal}")
x.banking()