
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
    # Added to make spaces not trigger untranslatable character
    " ": " "
}




def alphabet_to_morse(user_input: str) -> str:
    translation_error = False
    morse_code_translation: str = ""

    if user_input == "" or user_input == " ":
        return "Please enter something you'd like translated"
    for char in user_input.upper():
        try:
            morse_code_translation += morse_code_dict[char] + " "
        except KeyError:
            morse_code_translation += char + '*' + " "
            translation_error = True
    if translation_error:
        print(
            "the characters that could not be translated have been marked with an asterisk (*)."
        )
    return str(morse_code_translation)

def morse_to_alphabet(user_input: str) -> str:
    reverse_morse_dict: dict[str, str] = {v: k for k, v in morse_code_dict.items()}
    translation_error = False
    morse_word: str = ""
    alphabet_translation: str = ""
    
    if user_input == "" or user_input == " ":
        return "Please enter something you'd like translated"

    for char in user_input:
        try:
            if char in morse_code_dict.values():
                if char != " ":
                    morse_word += char
                if char == "   ":
                    alphabet_translation += reverse_morse_dict[morse_word]
                    print(morse_word)
                    morse_word = ""
            
        except KeyError:
            alphabet_translation += char + "*"
            translation_error = True
    if translation_error:
        print(
            "the characters that could not be translated have been marked with an asterisk (*)."
        )
    return str(alphabet_translation)

test = "hello my name"
test2 = ".... . .-.. .-.. ---   -- -.--   -. .- -- . "
print(alphabet_to_morse(user_input=test))
print(morse_to_alphabet(user_input=test2))
