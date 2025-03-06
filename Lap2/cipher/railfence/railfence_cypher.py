class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text: str, num_rails: int) -> str:
        if not isinstance(num_rails, int) or num_rails <= 0:
            raise ValueError("Number of rails must be a positive integer.")

        rails = [''] * num_rails
        rail_index = 0
        direction = 1  # 1 for down, -1 for up

        for char in plain_text:
            rails[rail_index] += char
            rail_index += direction

            # Change direction at the top or bottom rail
            if rail_index == 0 or rail_index == num_rails - 1:
                direction *= -1

        # Join the rails to form the ciphertext
        cipher_text = ''.join(rails)
        return cipher_text

    def rail_fence_decrypt(self, cipher_text: str, num_rails: int) -> str:
        if not isinstance(num_rails, int) or num_rails <= 0:
            raise ValueError("Number of rails must be a positive integer.")

        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1

        # Calculate the length of each rail
        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            rail_index += direction

            if rail_index == 0 or rail_index == num_rails - 1:
                direction *= -1

        # Create the rails by slicing the cipher text
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(cipher_text[start:start + length])
            start += length

        # Reconstruct the plain text
        plain_text = ''
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            plain_text += rails[rail_index][0]  # Take the first character from the current rail
            rails[rail_index] = rails[rail_index][1:]  # Remove the used character
            rail_index += direction

            if rail_index == 0 or rail_index == num_rails - 1:
                direction *= -1

        return plain_text

# Demo
if __name__ == "__main__":
    cipher = RailFenceCipher()
    plain_text = input("Enter the text to encrypt: ")
    num_rails = int(input("Enter the number of rails: "))

    # Encrypt
    encrypted = cipher.rail_fence_encrypt(plain_text, num_rails)
    print(f"Encrypted: {encrypted}")

    # Decrypt
    decrypted = cipher.rail_fence_decrypt(encrypted, num_rails)
    print(f"Decrypted: {decrypted}")
