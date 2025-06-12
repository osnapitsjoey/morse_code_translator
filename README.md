
# Morse Code Translator

A simple Python command-line tool to translate between English text and Morse code. Supports letters, numbers, and common punctuation.

## Features

- Translate English (letters, numbers, symbols) to Morse code
- Decode Morse code back to English text
- Handles unsupported characters gracefully, marking them with an asterisk (`*`)
- Easy-to-use command-line interface

## Usage

1. **Run the script:**

   ```bash
   python main.py
   ```

2. **Follow the prompts:**
   - Press `A` to translate text to Morse code.
   - Press `B` to translate Morse code to text.
   - Press `E` to exit.

3. **Example:**
   ```
   Press (A) to translate a message to morse code
   Press (B) to translate morse code to letters
   Press (E) to exit

   Enter the word or phrase you'd like to translate
   Hello, World!

   Morse code generated
   .... . .-.. .-.. --- --..--   .-- --- .-. .-.. -.. -.-.--
   ```

   ```
   Press (A) to translate a message to morse code
   Press (B) to translate morse code to letters
   Press (E) to exit

   Enter the word or phrase you'd like to translate
   .... . .-.. .-.. ---   .-- --- .-. .-.. -..

   your decoded message
   Hello world
   ```

## Requirements

- Python 3.10 or later

## How it works

- **Alphabet to Morse:** Each letter, digit, or symbol is mapped to its Morse code equivalent. Spaces between words are represented by three spaces in Morse.
- **Morse to Alphabet:** Each Morse code sequence is converted back to its corresponding character. Unrecognized sequences are marked with an asterisk.

## Error Handling

- Any unsupported or untranslatable character is either left with an asterisk or replaced with one in the output, and a helpful message is printed.

## License

This project is open-source and available under the [MIT License](LICENSE).

---


![blog-morse-code-151223](https://github.com/user-attachments/assets/217a244e-3ce5-44c7-b771-73157ab14b12)


Made with ❤️ by [osnapitsjoey](https://github.com/osnapitsjoey)
```
