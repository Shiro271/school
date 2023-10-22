import plugBoard
import Rotor

class enigma():
    def __init__(self, pairs, Walzenlage, Ringstellung):
        self.plugBoard = plugBoard.PlugBoard(pairs)
        self.rotors = Rotor.Rotors(Walzenlage, Ringstellung)
        

    def code(self, letter):
        letter = self.plugBoard.code(letter)
        letter = self.rotors.code(letter)
        letter = self.plugBoard.code(letter)
        
        return letter