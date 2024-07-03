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

class ImageEncrypter:
    BIT_CHUNK_SIZE = 6  # Each character will replace the last bit of each 6-bit chunk

    def __init__(self, image, sentence):
        self.hex = None
        self.image = self.open_image(image)
        self.sentence = sentence
        self.sentence_bin_seq = self.sentence_to_binary()
        self.image_bin_seq = self.image_to_binary()
        self.new_image_hex_seq = self.bin_to_hex()

    def open_image(self, image):
        with open("uploaded_image.png", "wb") as f:
            f.write(image.value)
        img = Image.open("uploaded_image.png")
        return img

    def image_to_binary(self):
        bin_seq = ""

        self.hex = self.image.tobytes().hex()
        
        required_length = len(self.sentence_bin_seq) * self.BIT_CHUNK_SIZE
        if len(self.hex) < required_length:
            raise ValueError("Please upload an image with more pixels")

        for i in range(0, required_length, self.BIT_CHUNK_SIZE):
            chunk = ''.join(hexToBinary[self.hex[j]] for j in range(i, i + self.BIT_CHUNK_SIZE))
            bin_seq += chunk[:-1] + self.sentence_bin_seq[i // self.BIT_CHUNK_SIZE]

        return bin_seq

    def bin_to_hex(self):
        hex_seq = ""
        for i in range(0, len(self.image_bin_seq), 4):
            bin_chunk = self.image_bin_seq[i:i + 4]
            hex_seq += self.get_key(bin_chunk, hexToBinary)

        hex_image = hex_seq + self.hex[len(hex_seq):]
        binary_data = binascii.unhexlify(hex_image)
        width, height = self.image.size
        
        img = Image.frombytes(self.image.mode, (width, height), binary_data)
        img.save("output.png", "PNG")
        
        return hex_image

    def sentence_to_binary(self):
        bin_seq = "".join(self.letter_to_bin(letter) for letter in self.sentence)
        bin_seq += "11111"  # stopping bits
        return bin_seq

    @staticmethod
    def letter_to_bin(letter):
        return letterToBinary.get(letter, "00000")  # Default to space if character not found

    @staticmethod
    def get_key(val, dict):
        for key, value in dict.items():
            if val == value:
                return key
        raise ValueError(f"Value {val} not found in dictionary")

# Example usage:
# image = open('path_to_image', 'rb')
# sentence = "hello"
# encrypter = ImageEncrypter(image, sentence)
