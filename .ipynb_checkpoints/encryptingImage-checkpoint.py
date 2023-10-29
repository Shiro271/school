from PIL import Image
import binascii

letterToBinary = {
    " " : "00000",
    "a" : "00001",
    "b" : "00010",
    "c" : "00011",
    "d" : "00100",
    "e" : "00101",
    "f" : "00110",
    "g" : "00111",
    "h" : "01000",
    "i" : "01001",
    "j" : "01010",
    "k" : "01011",
    "l" : "01100",
    "m" : "01101",
    "n" : "01110",
    "o" : "01111",
    "p" : "10000",
    "q" : "10001",
    "r" : "10010",
    "s" : "10011",
    "t" : "10100",
    "u" : "10101",
    "v" : "10110",
    "w" : "10111",
    "x" : "11000",
    "y" : "11001",
    "z" : "11010"
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

class ImageEncrypter():
    def __init__(self, image, sentence):
        self.hex = None
        self.image = self.openImage(image)
        self.sentence = sentence
        self.sentenceBinSeq = self.sentenceToBinary()
        self.imageBinSeq = self.imageToBinary()
        self.newImageHexSeq = self.binToHex()

    
    def openImage(self, image):
        
        with open("uploaded_image.png", "wb") as f:
            f.write(image.value)
        img = Image.open("uploaded_image.png")
        return img

    
    def imageToBinary(self):
        global hexToBinary
        
        binSeq = ""

        self.hex = self.image.tobytes().hex()
        
        if len(self.hex) < len(self.sentenceBinSeq) * 6:
            print("please upload an image with more pixels")
            return

        
        for i in range(1, len(self.sentenceBinSeq) * 6 + 1):
            binSeq += hexToBinary[self.hex[i - 1]]
            if i % 6 == 0:
                binSeq = binSeq[:-1]                             #delete last Bit and replace it with the Bin of the letter
                binSeq += self.sentenceBinSeq[(i // 6) - 1]

        return binSeq

    def binToHex(self):
        global hexToBinary
        
        hexSeq = ""
        for i in range(4, len(self.imageBinSeq) + 4, 4):
            bin = self.imageBinSeq[i - 4: i]
            hexSeq += self.get_key(bin, hexToBinary)

        hexImage = hexSeq + self.hex[len(hexSeq):]

        binary_data = binascii.unhexlify(hexImage)
        width, height = self.image.size
        
        img = Image.frombytes('RGB', (width, height), binary_data)
        img.save("output.png", "PNG")
        
        return hexImage
    
    def sentenceToBinary(self):
        binSeq = ""
        sentence = self.sentence
        for letter in sentence:
            binSeq += self.letterToBin(letter)
        return binSeq


    def letterToBin(self, letter):
        global letterToBinary
        return letterToBinary[letter]

    def binToLetter(self, bin):
        global letterToBinary
        return self.get_key(bin, letterToBinary)


    def get_key(self, val, dict):
        for key, value in dict.items():
            if val == value:
                return key

