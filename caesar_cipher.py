def shift_character(char, shift):
    if char.isupper():
        return chr((ord(char) + shift - 65) % 26 + 65)
    elif char.islower():
        return chr((ord(char) + shift - 97) % 26 + 97)
    return char

def caesar_cipher(text, shift, mode='encrypt'):
    if mode == 'decrypt':
        shift = -shift

    result = ''.join(shift_character(char, shift) for char in text)

    return result

def main():
    mode = input("Do you want to 'encrypt' or 'decrypt' the message? ").strip().lower()
    text = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))
    result = caesar_cipher(text, shift, mode)
    print(f"The resulting text is: {result}")

if __name__ == "__main__":
    main()
