
class Codec:
    def encode(self, strs) -> str:
        """Encodes a list of strings to a single string.
        """

        encoded = ""

        for s in strs:

            encoded += str(len(s)) + "#" + s        # encode each string as length + # + s to read it later

        return encoded


    def decode(self, s: str):
        """Decodes a single string to a list of strings.
        """
        decoded = []

        i = 0

        while i < len(s):

            j = i

            while s[j] != "#":        # get integer, it can be more than one digit integer

                j += 1

            length = int(s[i:j])
                                        # j + 1 to skip # and taking everything from j + 1 till length

            decoded.append(s[j + 1 : j + 1 + length])

            i = j + 1 + length    # incrementing i for next word


        return decoded




