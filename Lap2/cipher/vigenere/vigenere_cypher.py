class VigenereCipher:

    def __init__(self):
        pass

    def vigenere_encrypt(self, plain_text: str, key: str) -> str:
        encrypted_text = ""
        key_index = 0

        for char in plain_text:
            if char.isalpha():
                # Calculate the key shift based on the corresponding character in the key
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')

                if char.isupper():
                    encrypted_text += chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
                else:
                    encrypted_text += chr((ord(char) - ord('a') + key_shift) % 26 + ord('a'))

                # Increment the key index only for alphabetic characters
                key_index += 1
            else:
                # Keep non-alphabet characters unchanged
                encrypted_text += char

        return encrypted_text

    def vigenere_decrypt(self, encrypted_text: str, key: str) -> str:
        decrypted_text = ""
        key_index = 0

        for char in encrypted_text:
            if char.isalpha():
                # Calculate the key shift based on the corresponding character in the key
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')

                if char.isupper():
                    decrypted_text += chr((ord(char) - ord('A') - key_shift) % 26 + ord('A'))
                else:
                    decrypted_text += chr((ord(char) - ord('a') - key_shift) % 26 + ord('a'))

                # Increment the key index only for alphabetic characters
                key_index += 1
            else:
                # Keep non-alphabet characters unchanged
                decrypted_text += char

        return decrypted_text


# Demo
if __name__ == "__main__":
    cipher = VigenereCipher()
    plain_text = input("Enter the text to encrypt: ")
    key = input("Enter the key: ")

    # Encrypt
    encrypted = cipher.vigenere_encrypt(plain_text, key)
    print(f"Encrypted: {encrypted}")

    # Decrypt
    decrypted = cipher.vigenere_decrypt(encrypted, key)
    print(f"Decrypted: {decrypted}")
