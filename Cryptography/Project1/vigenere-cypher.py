from string import ascii_uppercase

def vigenere_encrypt(message, key):
    alphabet = ascii_uppercase

    key_repeated = ''.join([
        key[i % len(key)]
        for i in range(len(message))
    ])

    encrypted_text = ''.join([
        alphabet[(alphabet.index(m_char) + alphabet.index(k_char)) % 26]
        for m_char, k_char in zip(message, key_repeated)
    ])

    return encrypted_text

