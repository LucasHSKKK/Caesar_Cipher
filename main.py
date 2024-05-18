ciphertext = "Dtz ini f ltti otg"


def decrypt(ciphertext, key):
    decodificated = ""
    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    alphabet_upper = [letter_lower.upper() for letter_lower in alphabet]
    for letter in ciphertext:
        if letter in alphabet:
            position = alphabet.index(letter)
            letter_dc = (position + key) % len(alphabet)
            decodificated += alphabet[letter_dc]
        elif letter in alphabet_upper:
            position = alphabet_upper.index(letter)
            letter_dc = (position + key) % len(alphabet_upper)
            decodificated += alphabet_upper[letter_dc]
        else:
            decodificated += " "

    print(decodificated)


decrypt(ciphertext, -5)
