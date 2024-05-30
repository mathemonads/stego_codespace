"""Main module."""

class Steganography:
    def encode(self, message, bits):
        raise NotImplementedError("Subclasses should implement method: encode")
    def decode(self, embedded_message):
        raise NotImplementedError("Subclasses should implement method: decode")

class Stego1(Steganography):
    def encode(self, message, bits):
        i = 0
        stego = []
        for char in message:
            stego.append(char)
            if char == " " and i < len(bits):
                if bits[i] == "1":
                    stego.append(" ")
                i += 1
        if i < len(bits) and bits[i] == "1":
            stego.append(" ")
        return "".join(stego)

    def decode(self, message):
        bits = []
        c = 0
        for char in message:
            if char == " ":
                c += 1
            else:
                if c == 1:
                    bits.append("0")
                elif c >= 2:
                    bits.append("1")
                c = 0
        if c < 1:
            bits.append("0")
        elif c >= 1:
            bits.append("1")
        return "".join(bits)

class Stego2(Steganography):
    def encode(self, message, bits):
        i = 0
        stego = []
        for char in message:
            if char.isalpha() and i < len(bits):
                if bits[i] == "1":
                    stego.append(char.upper())
                else:
                    stego.append(char.lower())
                i += 1
            else:
                stego.append(char)
        return "".join(stego)

    def decode(self, message):
        bits = []
        for char in message:
            if char.isalpha():
                if char.isupper():
                    bits.append("1")
                else:
                    bits.append("0")
        return "".join(bits)

