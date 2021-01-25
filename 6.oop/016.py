class calc:
    def __init__(self, num_input):
        nums = num_input.split(" ")
        self.num1 = int(nums[0])
        self.num2 = int(nums[1])

    def add(self):
        print(f"{self.num1} + {self.num2} = {self.num1 + self.num2}")

    def subtract(self):
        print(f"{self.num1} - {self.num2} = {self.num1 - self.num2}")

    def multiply(self):
        print(f"{self.num1} * {self.num2} = {self.num1 * self.num2}")

    def divide(self):
        print(f"{self.num1} / {self.num2} = {self.num1 / self.num2}")


print("Input the numbers:")
x = calc(f"{input('num1: ')} {input('num2: ')}")
while True:
    operator = input("Operator: ")
    if operator == "+":
        x.add()
    elif operator == "-":
        x.subtract()
    elif operator == "*":
        x.multiply()
    elif operator == "/":
        x.divide()
    else:
        break