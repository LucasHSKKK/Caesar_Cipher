ciphertext = "N qtaj uwtlwfrrnsl zxnsl Udymts"


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
    ciphertext = ciphertext.lower()
    for letter in ciphertext:
        if letter in alphabet:
            position = alphabet.index(letter)
            letter_dc = alphabet[position + key % len(alphabet)]
            decodificated += letter_dc
        else:
            decodificated += " "

    print(decodificated)


decrypt(ciphertext, 5)
