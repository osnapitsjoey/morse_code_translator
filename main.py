morse_code_dict: dict[str, str] = {
    # Letters
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    # Numbers
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    # Symbols
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    '"': ".-..-.",
    "$": "...-..-",
    "@": ".--.-.",
}


def alphabet_to_morse(user_input: str) -> str:
    translation_error = False
    morse_code_translation: str = ""
    for char in user_input.upper():
        if char in morse_code_dict:
            morse_code_translation += morse_code_dict[char] + " "
        elif char == " ":
            morse_code_translation += "  "
        elif char not in morse_code_dict and char != " ":
            morse_code_translation += char + "*"
            translation_error = True
    if translation_error:
        print(
            "Non translatable characters have been left in, with an asterisk next to them."
        )
    return morse_code_translation


def morse_to_alphabet(user_input: str) -> str:
    reverse_morse_dict: dict[str, str] = {v: k for k, v in morse_code_dict.items()}
    sentence: str = ""
    words = user_input.strip().split(sep="   ")
    translation_error = False
    for words in words:
        letters = words.split(sep=" ")
        for letter in letters:
            if letter in reverse_morse_dict:
                sentence += reverse_morse_dict[letter]
            else:
                translation_error = True
                sentence += "*"
        sentence += " "
    if translation_error:
        print("Non translatable characters have been replaced with asterisks")
    return sentence.strip().capitalize()


def translate_cli() -> None:
    while True:
        try:
            initialize: str = input(
                "Press (A) to translate a message to morse code\nPress (B) to translate morse code to letters\nPress (E) to exit\n"
            ).lower()
            if initialize.startswith("e"):
                print("Goodbye.")
                break

            phrase_to_translate: str = input(
                "Enter the word or phrase you'd like to translate\n"
            )

            if initialize.startswith("a") or initialize.startswith("b"):
                if initialize.startswith("a"):
                    result: str = alphabet_to_morse(user_input=phrase_to_translate)
                    print(f"Morse code generated\n {result}\n")

                elif initialize.startswith("b"):
                    result: str = morse_to_alphabet(user_input=phrase_to_translate)
                    print(f"your decoded message\n {result}\n")

            else:
                raise ValueError("Invalid Option")

        except ValueError as ve:
            print(f"Error: {ve}")
            print("Please choose A, B, or E.\n")
            translate_cli()
        except Exception as e:
            print(f"Unexpected error: {e}")
            print("Something went wrong. Restarting...\n")
            translate_cli()


if __name__ == "__main__":
    translate_cli()
