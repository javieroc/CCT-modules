def caesar_cipher(message, key):
    shifted_chars = [
        chr((ord(char) - 65 + key) % 26 + 65) if char.isalpha() else char
        for char in message
    ]
    return ''.join(shifted_chars)
