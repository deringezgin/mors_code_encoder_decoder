from os import system
from datetime import datetime as dt


def clear():
    """Function for clearing the screen"""
    _ = system("clear")


# Mors Code Chart
codes = {
    "A": "._",
    "B": "_...",
    "C": "_._.",
    "D": "_..",
    "E": ".",
    "F": ".._.",
    "G": "__.",
    "H": "....",
    "I": "..",
    "J": ".___",
    "K": "_._",
    "L": "._..",
    "M": "__",
    "N": "_.",
    "O": "___",
    "P": ".__.",
    "R": "__._",
    "S": "...",
    "T": "_",
    "U": ".._",
    "V": "..._",
    "W": ".__",
    "X": "_.._",
    "Y": "_.__",
    "Z": "__..",
    " ": "/",
    "": " "
}

work = True
# Looping through the program
while work:
    print("--- Mors Code Converter ---\n")
    log_txt = ""
    preference = ""
    # Determining the intent of the user
    while preference not in ["encode", "decode", "log"]:
        preference = input("Would you like to encode or decode text?: ").lower()
        # Being sure about valid entry
        if preference not in ["encode", "decode", "log"]:
            print("Invalid Entry. Write Encode, Decode")

    # Taking user input
    if preference in ["encode", "decode"]:
        txt = input(f"\nPlease enter the text you'd like to {preference}:\n").upper()

        message = ""
        # Encoding or Decoding
        if preference == "encode":
            for char in txt:
                char = codes[char]
                message += char + " "
        elif preference == "decode":
            txt = txt.split()
            for char in txt:
                char = list(codes.keys())[list(codes.values()).index(char)]
                message += char
        print(message.lower())

        # Saving the user log to a txt file
        log_txt += dt.now().strftime("%B %d %Y %H:%M:%S") + " --> " + "".join(txt) + " --> " + message.lower()
        with open(file="log.txt", mode="a") as file:
            file.write(log_txt)
            file.write("\n")

        # Asking the user if he'd like to continue
        if input("Would you like to do another work? Yes / No: ").lower() == "no":
            work = False
            clear()
        clear()

    # Showing the log data
    elif preference == "log":
        with open(file="log.txt", mode="r") as file:
            print(file.read())
