class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key: str) -> list:
        """
        Creates a 5x5 Playfair cipher matrix from the given key.
        """
        # Validate the input key
        if not key.isalpha():
            raise ValueError("Key must contain only alphabetic characters")

        # Prepare the key: Replace "J" with "I" and convert to uppercase
        key = key.replace("J", "I").upper()

        # Remove duplicates while maintaining the order
        key_letters = []
        seen = set()
        for letter in key:
            if letter not in seen:
                key_letters.append(letter)
                seen.add(letter)

        # Add remaining letters of the alphabet (excluding "J")
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        remaining_letters = [letter for letter in alphabet if letter not in seen]

        # Combine key letters with remaining letters to form a 5x5 matrix
        full_matrix = key_letters + remaining_letters
        return [full_matrix[i:i + 5] for i in range(0, 25, 5)]

    def find_letter_coords(self, matrix: list, letter: str) -> tuple:
        """
        Finds the row and column coordinates of a letter in the matrix.
        """
        DataMatrix = len(matrix)
        for row in range(DataMatrix):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
        raise ValueError(f"Letter '{letter}' not found in the matrix")

    def playfair_encrypt(self, plain_text: str, matrix: list) -> str:
        """
        Encrypts plaintext using the Playfair cipher.
        """
        plain_text = plain_text.replace("J", "I").upper().replace(" ", "")
        processed_text = self._prepare_text(plain_text)

        # Encrypt pairs of letters
        encrypted_text = ""
        for i in range(0, len(processed_text), 2):
            pair = processed_text[i:i + 2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                # Same row: Shift right
                encrypted_text += matrix[row1][(col1 + 1) % 5]
                encrypted_text += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                # Same column: Shift down
                encrypted_text += matrix[(row1 + 1) % 5][col1]
                encrypted_text += matrix[(row2 + 1) % 5][col2]
            else:
                # Rectangle rule: Swap columns
                encrypted_text += matrix[row1][col2]
                encrypted_text += matrix[row2][col1]

        return encrypted_text

    def playfair_decrypt(self, cipher_text: str, matrix: list) -> str:
        """
        Decrypts ciphertext using the Playfair cipher.
        """
        cipher_text = cipher_text.upper().replace(" ", "")

        # Decrypt pairs of letters
        decrypted_text = ""
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i + 2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                # Same row: Shift left
                decrypted_text += matrix[row1][(col1 - 1) % 5]
                decrypted_text += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                # Same column: Shift up
                decrypted_text += matrix[(row1 - 1) % 5][col1]
                decrypted_text += matrix[(row2 - 1) % 5][col2]
            else:
                # Rectangle rule: Swap columns
                decrypted_text += matrix[row1][col2]
                decrypted_text += matrix[row2][col1]

        # Remove padding and filler "X"
        return self._clean_decrypted_text(decrypted_text)

    def _prepare_text(self, text: str) -> str:
        """
        Prepares the plaintext by handling duplicate letters and padding.
        """
        processed_text = ""
        i = 0
        while i < len(text):
            processed_text += text[i]
            if i + 1 < len(text) and text[i] == text[i + 1]:
                processed_text += "X"  # Add filler for duplicates
            i += 1

        # Add padding if the length is odd
        if len(processed_text) % 2 != 0:
            processed_text += "X"

        return processed_text

    def _clean_decrypted_text(self, text: str) -> str:
        """
        Cleans the decrypted text by removing filler "X" where appropriate.
        """
        cleaned_text = ""
        i = 0
        while i < len(text) - 1:
            if text[i + 1] == "X" and (i + 2 >= len(text) or text[i] == text[i + 2]):
                # Skip filler "X" if it was inserted between duplicate letters
                cleaned_text += text[i]
                i += 2
            else:
                cleaned_text += text[i]
                i += 1

        # Add the last character if it wasn't processed
        if i == len(text) - 1:
            cleaned_text += text[i]

        return cleaned_text


if __name__ == "__main__":
    cipher = PlayFairCipher()
    key = "KEYWORD"
    matrix = cipher.create_playfair_matrix(key)

    print("\nMatrix:")
    for row in matrix:
        print(" ".join(row))

    # Test with plaintext
    plaintext = "BALLOON"
    encrypted = cipher.playfair_encrypt(plaintext, matrix)
    decrypted = cipher.playfair_decrypt(encrypted, matrix)

    print(f"Original: {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
