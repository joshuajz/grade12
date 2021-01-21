import random

words = []

with open("Grade 11 Review/words.txt", 'r') as f:
    for line in f.readlines():
        words.append(line.strip("\n"))

random_word = words[random.randint(0, len(words))]

print("Word: ", end='')
print("_ " * len(random_word))

guesses = {'amount': 0, 'guesses': [], 'body_parts': [], 'og_body_parts': ['arm', 'arm', 'leg', 'leg', 'body', 'head', 'hands', 'feet']}

for i in range(len(guesses['og_body_parts'])):
    g = input(f"Guess {i}: ")

    # Guess is Correct
    if g == random_word:
        print("You win!")
        guesses['guesses'].append(g)
        print(f"Guesses: {guesses['guesses']}")
        print(f"Body Parts: {guesses['body_parts']}")
        break
    
    guesses['guesses'].append(g)
    
    # Random bodypart
    guesses['body_parts'].append(guesses['og_body_parts'].pop(random.randint(0, len(guesses['og_body_parts']))))
    
    # Displays to the user
    for letter in random_word:
        if letter == g:
            print(letter, end=" ")
        else:
            print('_', end=' ')
    
    
    print("")


