
class PlugBoard():
    def __init__(self, pairs):
        self.Alphabet = {
            "a" : "a",
            "b" : "b",
            "c" : "c",
            "d" : "d",
            "e" : "e",
            "f" : "f",
            "g" : "g",
            "h" : "h",
            "i" : "i",
            "j" : "j",
            "k" : "k",
            "l" : "l",
            "m" : "m",
            "n" : "n",
            "o" : "o",
            "p" : "p",
            "q" : "q",
            "r" : "r",
            "s" : "s",
            "t" : "t",
            "u" : "u",
            "v" : "v",
            "w" : "w",
            "x" : "x",
            "y" : "y",
            "z" : "z"
        }
        if len(pairs) != 0:
            for pair in pairs:
                self.conect(pair[0], pair[1])

    def conect(self, l1, l2):
        self.Alphabet[l1], self.Alphabet[l2] = self.Alphabet[l2], self.Alphabet[l1]

    def code(self, letter):
        return self.Alphabet[letter]