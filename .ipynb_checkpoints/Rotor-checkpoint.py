import random

class Rotors():
    def __init__(self, Walzenlage, Ringstellung):

        self.coded = Ringstellung[0]
        self.r1 = {'a': 'u', 'b': 'x', 'c': 'p', 'd': 'd', 'e': 'v', 'f': 'z', 'g': 'm', 'h': 'l', 'i': 'f', 'j': 'n', 'k': 'o', 'l': 'i', 'm': 'q', 'n': 'w', 'o': 'b', 'p': 's', 'q': 'j', 'r': 'k', 's': 'y', 't': 'e', 'u': 'g', 'v': 'r', 'w': 'h', 'x': 'c', 'y': 't', 'z': 'a'}
        self.r2 = {'a': 'z', 'b': 'c', 'c': 't', 'd': 'b', 'e': 'w', 'f': 'j', 'g': 'd', 'h': 'l', 'i': 'v', 'j': 'k', 'k': 'o', 'l': 'f', 'm': 'q', 'n': 'm', 'o': 'p', 'p': 'a', 'q': 'r', 'r': 'i', 's': 'n', 't': 'y', 'u': 'h', 'v': 's', 'w': 'u', 'x': 'e', 'y': 'g', 'z': 'x'}
        self.r3 = {'a': 'y', 'b': 's', 'c': 'j', 'd': 'k', 'e': 'q', 'f': 'x', 'g': 'c', 'h': 'w', 'i': 'u', 'j': 'v', 'k': 'z', 'l': 'e', 'm': 'i', 'n': 'm', 'o': 'l', 'p': 'd', 'q': 'o', 'r': 't', 's': 'r', 't': 'p', 'u': 'h', 'v': 'a', 'w': 'b', 'x': 'n', 'y': 'g', 'z': 'f'}
        self.r4 = {'a': 'h', 'b': 'q', 'c': 'd', 'd': 'x', 'e': 'p', 'f': 'r', 'g': 'i', 'h': 'j', 'i': 'c', 'j': 'l', 'k': 'f', 'l': 'm', 'm': 'b', 'n': 'u', 'o': 's', 'p': 'o', 'q': 'a', 'r': 'k', 's': 'v', 't': 't', 'u': 'n', 'v': 'w', 'w': 'z', 'x': 'y', 'y': 'e', 'z': 'g'}
        self.r5 = {'a': 'q', 'b': 'm', 'c': 'c', 'd': 'o', 'e': 'i', 'f': 'w', 'g': 'e', 'h': 't', 'i': 'z', 'j': 'p', 'k': 'j', 'l': 'd', 'm': 'y', 'n': 'a', 'o': 'x', 'p': 'u', 'q': 's', 'r': 'l', 's': 'f', 't': 'h', 'u': 'k', 'v': 'g', 'w': 'v', 'x': 'b', 'y': 'r', 'z': 'n'}
        
        self.reflector = {'a': 's', 'b': 'q', 'c': 't', 'd': 'l', 'e': 'm', 'f': 'p', 'g': 'h', 'h': 'x', 'i': 'u', 'j': 'i', 'k': 'b', 'l': 'f', 'm': 'n', 'n': 'd', 'o': 'e', 'p': 'z', 'q': 'k', 'r': 'g', 's': 'w', 't': 'r', 'u': 'o', 'v': 'a', 'w': 'y', 'x': 'v', 'y': 'j', 'z': 'c'}

        self.rotors = [self.r1, self.r2, self.r3, self.r4, self.r5]

        self.Walzenlage = Walzenlage

        for i in range(3):
            self.rotate(self.rotors[i], Ringstellung[i])


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

    
    def randomize(self, repetitions, rotor):
        for _ in range(repetitions):
            x = random.choice(list(rotor.keys()))
            y = random.choice(list(rotor.keys()))

            rotor[x], rotor[y] = rotor[y], rotor[x]

    def code(self, letter):
        for r in self.Walzenlage:
            rotor = self.rotors[r - 1]
            letter = rotor[letter]
        letter = self.reflector[letter]
        for i in range(len(self.Walzenlage) - 1, -1, -1):
            rotor = self.rotors[self.Walzenlage[i] - 1]
            letter = rotor[letter]


        self.rotate(self.rotors[self.Walzenlage[0]], 1) #rotate first rotor
        self.coded += 1
        if self.coded % 26 == 0:
            self.rotate(self.rotors[self.Walzenlage[1]], 1) #rotate second rotor
        if self.coded % 26 ** 2 == 0:
            self.rotate(self.rotors[self.Walzenlage[2]], 1) #rotate second rotor
        
        return letter


    
    def rotate(self, rotor, reps):
        for i in range(reps):
            for letter in rotor:
                if letter == "a":
                    prev = "a"
                    continue
                rotor[prev], rotor[letter] = rotor[letter], rotor[prev]
                prev = letter