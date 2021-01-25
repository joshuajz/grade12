import random


class myClass:
    def __init__(self):
        self.lyrics = [
            "row, row, row your boat",
            "Gently down the stream",
            "Merrily, merrily, merrily, merrily",
            "Life is but a dream",
        ]

    def randomize(self):
        random.shuffle(self.lyrics)

    def printLyrics(self):
        for lyric in self.lyrics:
            print(lyric)


x = myClass()

x.printLyrics()
x.randomize()
print("\n\n")
x.printLyrics()
