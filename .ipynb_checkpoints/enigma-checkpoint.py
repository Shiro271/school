import plugBoard
import Rotor

class enigma():
    def __init__(self, pairs, Walzenlage, Ringstellung):
        self.plugBoard = plugBoard.PlugBoard(pairs)
        self.rotors = Rotor.Rotors(Walzenlage, Ringstellung)
        

    def code(self, sentence):
        coded = ""
        for letter in sentence:
            if letter == " ":
                coded += " "
                continue
            letter = self.plugBoard.code(letter)
            letter = self.rotors.code(letter)
            letter = self.plugBoard.code(letter)
            coded += letter
        return coded
    