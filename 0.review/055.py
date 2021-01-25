# Part 1
school = input("School: ")

for letter in school:
    print(f"Give me an {letter}" if letter in ['a', 'e', 'i', 'o', 'u', 'y'] else f"Give me a {letter}")

print("What does that spell?")

# Part 2
sentence = "Shz szlls szashZlls by the sza shorZ"

for letter in sentence:
    print("e" if letter == "z" else 'E' if letter == "Z" else letter, end="")
print('\n')

# Part 3
password = "hello"
for i in range(3):
    print(f"Password Length: {len(password)}")
    guess = input("Guess: ")
    for i in range(len(guess)):
        print(f"{guess[i]} | Correct" if password[i] == guess[i] else f"{guess[i]} | Incorrect")