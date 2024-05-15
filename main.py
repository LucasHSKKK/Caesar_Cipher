ciphertext = "N qtaj uwtlwfrrnsl zxnsl Udymts"
decodificated = []


def decrypt(ciphertext, key):

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
            print(position)


decrypt(ciphertext, 5)
