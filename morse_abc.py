alphabet = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    ' ': ' ',
}

alphabet_reverse = {value: key for key, value in alphabet.items()}


class Morse:
    def encode(self, text):
        """Encode a given text to Morse code."""
        return ' '.join(alphabet[char.upper()] for char in text)

    def decode(self, morse):
        """Decode a given Morse code to text."""
        words = morse.split('   ')  # Morse words are separated by three spaces
        decoded_words = []
        for word in words:
            decoded_chars = ''.join(alphabet_reverse[char] for char in word.split())
            decoded_words.append(decoded_chars)
        return ' '.join(decoded_words)


morse = Morse()
print(morse.encode('SOME TEXT HERE'))
# Expected output: ... --- -- .   - . -..- -   .... . .-. .

print(morse.decode('... --- -- .   - . -..- -   .... . .-. .'))
# Expected output: SOME TEXT HERE

# Decoding the secret message
print(morse.decode('-- .- .-. .-. -.--   -.-. .... .-. .. ... - -- .- ...   .- -. -..   .... .- .--. .--. -.--   -. . .--   -.-- . .- .-.'))
