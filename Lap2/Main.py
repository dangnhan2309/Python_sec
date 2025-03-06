# Caesar Cipher Implementation
def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    if mode == "decrypt":
        shift = -shift  # Reverse the shift for decryption

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def use_ceasar():
    plaintext =input("Type down your text: ")
    shift = int(input("Nhap khoa k : "))

    # Encrypt
    encrypted_text = caesar_cipher(plaintext, shift, mode="encrypt")
    print(f"Encrypted Text: {encrypted_text}")
    # Decrypt
    decrypted_text = caesar_cipher(encrypted_text, shift, mode="decrypt")
    print(f"Decrypted Text: {decrypted_text}")

def main():
    use_ceasar()
    print(ord("h"))



if __name__ == "__main__":
    main()