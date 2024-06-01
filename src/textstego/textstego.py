
""" Main module. """

class Steganography:
    def encode(self, message, bits):
        raise NotImplementedError("Subclasses should implement method: encode")
    def decode(self, embedded_message):
        raise NotImplementedError("Subclasses should implement method: decode")

class Stego1(Steganography):
    # if value is a 0, we do not change the white space, if value is a 1, add a space to the whitespace.
    def encode(self, message: str, bits: str = "") -> str: 

        """Method to encode a message into the cover text using a rule described in the program.
        Students: Can you figure out how this method works?

        Args:
            message (str): Value to hide the information into 
            bits (str, optional): String of bits to hide into the message. Defaults to "", or no message.

        Returns:
            str: Stego message embedded with hidden bits.  
        """
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

    def decode(self, message: str) -> str: 
        """Method to decode the hidden message from the stego text.

        Args:
            message (str): Message with hidden information 

        Returns:
            str: Hidden message as a string of 0s and 1s. 
        """
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
    # if value is a 0, the value is lowercases, if value is a 1, it is capitalized.
    def encode(self, message: str, bits: str = "") -> str:
        """Method to encode a message into the cover text using a rule described in the program.
        Students: Can you figure out how this method works?

        Args:
            message (str): Value to hide the information into 
            bits (str, optional): String of bits to hide into the message. Defaults to "", or no message.

        Returns:
            str: Stego message embedded with hidden bits.  
        """
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

    def decode(self, message: str) -> str:
        """Method to decode the hidden message from the stego text.

        Args:
            message (str): Message with hidden information 

        Returns:
            str: Hidden message as a string of 0s and 1s. 
        """
        bits = []
        for char in message:
            if char.isalpha():
                if char.isupper():
                    bits.append("1")
                else:
                    bits.append("0")
        return "".join(bits)

