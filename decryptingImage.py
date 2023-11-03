from PIL import Image
import binascii
from itertools import count

binaryToLetters = {
    "00000" : " ",
    "00001" : "a",
    "00010" : "b",
    "00011" : "c",
    "00100" : "d",
    "00101" : "e",
    "00110" : "f",
    "00111" : "g",
    "01000" : "h",
    "01001" : "i",
    "01010" : "j",
    "01011" : "k",
    "01100" : "l",
    "01101" : "m",
    "01110" : "n",
    "01111" : "o",
    "10000" : "p",
    "10001" : "q",
    "10010" : "r",
    "10011" : "s",
    "10100" : "t",
    "10101" : "u",
    "10110" : "v",
    "10111" : "w",
    "11000" : "x",
    "11001" : "y",
    "11010" : "z"
}

hexToBinary = {
    "0" : "0000",
    "1" : "0001",
    "2" : "0010",
    "3" : "0011",
    "4" : "0100",
    "5" : "0101",
    "6" : "0110",
    "7" : "0111",
    "8" : "1000",
    "9" : "1001",
    "a" : "1010",
    "b" : "1011",
    "c" : "1100",
    "d" : "1101",
    "e" : "1110",
    "f" : "1111",
}

class ImageDecrypter():
    def __init__(self, image):
        self.hex = self.openImage(image).tobytes().hex()
        self.letters = self.getLettersFromImage()

    def openImage(self, image):
        with open("uploaded_image.png", "wb") as f:
            f.write(image.value)
        img = Image.open("uploaded_image.png")
        return img
    
    def getLettersFromImage(self):
        global hexToBinary
        global binaryToLetters
        
        binSeq = ""
        letters = ""

        for i in count(5, 6):
            binSeq += hexToBinary[self.hex[i]][-1]  #turn the hex of the image to binary and add the last bit to binSeq
            if len(binSeq) == 5:
                if binSeq == "11111":
                    break
                if binSeq not in binaryToLetters:
                    return "Dieses Bild wurde nicht verschlüsselt."
                letters += binaryToLetters[binSeq]
                binSeq = ""

        return letters