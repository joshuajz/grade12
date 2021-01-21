name = input()

length = 0

for letter in name:
    print(letter, end="")
    length+= 1

print(f"Length: {length}")