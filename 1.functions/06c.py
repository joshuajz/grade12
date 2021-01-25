def center(sentence, width):
    length = len(sentence)

    width_each_side = (width - length) / 2

    print("_" * int(width_each_side), end="")
    print(sentence, end="")
    print("_" * int(width_each_side), end="")


center(input("Sentence: "), int(input("Width: ")))