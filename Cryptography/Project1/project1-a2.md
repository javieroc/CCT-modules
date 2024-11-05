## CCT College Dublin

|                        |                                    |
|------------------------|------------------------------------|
| **Module Title:**      | Master of Science in Cybersecurity |
| **Assessment Title:**  | Cryptography Theory and Practice   |
| **Lecturer Name:**     | Dr. Naila Aslam                    |
| **Student Full Name:** | Javier Alfonso Ocampo              |
| **Student Number:**    | 2024328                            |


### Part 1: Basic cryptography techniques

#### Task 1

Message: ILIKECCTCOLLEGEDUBLIN

Key: 4


The expression `(ord('I') 65 + 4) % 26 + 65 = M` illustrates how to shift the character **'I'** by 4 positions in the Caesar Cipher. It starts by converting **'I'** to its ASCII value (73), subtracting 65 to map the alphabet (so **'I'** becomes 8), and then adding the shift value of 4, resulting in 12. The `% 26` operation keeps the result within the alphabet range, and adding 65 converts it back to the ASCII value, yielding **'M'**. This process effectively shifts **'I'** to **'M'**.

All the transformations:

I shifted by 4 = M

L shifted by 4 = P

I shifted by 4 = M

K shifted by 4 = O

E shifted by 4 = I

C shifted by 4 = G

C shifted by 4 = G

T shifted by 4 = X

C shifted by 4 = G

O shifted by 4 = S

L shifted by 4 = P

L shifted by 4 = P

E shifted by 4 = I

G shifted by 4 = K

E shifted by 4 = I

D shifted by 4 = H

U shifted by 4 = Y

B shifted by 4 = F

L shifted by 4 = P

I shifted by 4 = M

N shifted by 4 = R

The encrypted message is: MPMOIGGXGSPPIKIHYFPMR

The code goes like this:

```python
    def caesar_cipher(message, key):
        shifted_chars = [
            chr((ord(char) 65 + key) % 26 + 65) if char.isalpha() else char
            for char in message
        ]
        return ''.join(shifted_chars)
```


#### Task 2

Vigenère Cipher: Encrypting the message `IHOPEYOUAREDOINGWELL` using the Vigenère Cipher with the key `KEY`.

Prepare the Key

The key `KEY` is repeated to match the length of the message, which is 20 characters. So, the repeated key is: `KEYKEYKEYKEYKEYKEYKE`

Each letter in the message is shifted by the corresponding letter in the key. The shift is based on the alphabetical position of the key letter (A=0, B=1, ..., Z=25).

Character Shifts and Encrypted Characters:

`I` (8) + `K` (10) = `S` (18)

`H` (7) + `E` (4) = `L` (11)

`O` (14) + `Y` (24) = `M` (12)

`P` (15) + `K` (10) = `Z` (25)

`E` (4) + `E` (4) = `I` (8)

`Y` (24) + `Y` (24) = `W` (22)

`O` (14) + `K` (10) = `Y` (24)

`U` (20) + `E` (4) = `Y` (24)

`A` (0) + `Y` (24) = `Y` (24)

`R` (17) + `K` (10) = `B` (1)

`E` (4) + `E` (4) = `I` (8)

`D` (3) + `Y` (24) = `B` (1)

`O` (14) + `K` (10) = `Y` (24)

`I` (8) + `E` (4) = `M` (12)

`N` (13) + `Y` (24) = `L` (11)

`G` (6) + `K` (10) = `Q` (16)

`W` (22) + `E` (4) = `A` (0)

`E` (4) + `Y` (24) = `C` (2)

`L` (11) + `K` (10) = `V` (21)

`L` (11) + `E` (4) = `P` (15)

Combining all the encrypted characters gives the encrypted Message: `SLMZIWYYYBIBYMLQACVP`

```python
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
```

### Part 2: Symetric and asymetric cryptography techniques

#### Task 1: RSA

To generate RSA keys we need to follow these steps:

1. Choose two primes, `P=23` and `Q=29`

2. Get `n` by multiplying `P` and `Q`:
     ```
     n = P * Q = 23 * 29 = 667
     ```

3. Calculate `phi(n)`:
     ```
     phi(n) = (P - 1) * (Q - 1)
     ```
   - Substitute values:
     ```
     phi(n) = (23 - 1) * (29 - 1) = 22 * 28 = 616
     ```

4. Choose a public exponent `e`:
   - Select `e` such that `1 < e < phi(n)` and `gcd(e, phi(n)) = 1`.
   - A common choice is `e = 3`.
   - We check that `gcd(3, 616) = 1` , so `e = 3` is valid.

5. Calculate the private exponent `d`:
   - Find `d`, the *modular inverse* of `e` with respect to phi(n), satisfying:
     ```
     d * e = 1 (mod phi(n))
     ```
   - For this example, d = 411 (since 411 * 3 % 616 = 1 ).

6. Key Pair:
   - Public Key: `(e,n)=(3,667)`
   - Private Key: `(d,n)=(411,667)`


RSA algorithm use a public-key cryptography to offer a dependable system for safe data transfer. RSA provides encryption and decryption of messages using its public and private key pair, guaranteeing that only the intended receiver may access the information. The difficulty of separating the secret numbers from the public key is the strength of RSA.


#### Task 2: DES Algorithm


Step-by-Step Overview

1. Key Generation:
   - DES uses a 56-bit key (typically entered as a 64-bit key, with 8 bits for parity).
   - Initial Permutation (PC-1): The key is permuted to rearrange bits.
   - Split & Rotate: The key is split into two 28-bit halves, rotated, and recombined in 16 rounds to create 48-bit subkeys for each encryption round.

2. Initial Permutation (IP):
   - The 64-bit plaintext is permuted in a fixed order to rearrange its bits.

3. 16 Rounds of Encryption:
   - For each round, the following steps are applied:
     - Expansion: The 32-bit right half of data is expanded to 48 bits.
     - Key Mixing: The expanded half is XORed with the round’s subkey.
     - Substitution (S-Boxes): This XORed result is reduced to 32 bits using 8 S-boxes, each mapping 6 bits to 4 bits.
     - Permutation (P): The 32-bit output is permuted.
   - Round Swap: After the right half is processed, it’s XORed with the left half, and the halves are swapped.

4. Final Permutation (IP^-1):
   - After 16 rounds, a final permutation (inverse of the initial permutation) is applied to obtain the 64-bit ciphertext.

5. Output:
   - The final result is the encrypted 64-bit block of ciphertext.


DES encrypts data in a structured, repetitive way, using key mixing, substitution, and permutation in each round, making it highly systematic but vulnerable to modern cryptographic analysis.
