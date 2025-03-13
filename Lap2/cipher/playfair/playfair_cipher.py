class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key: str) -> list:
        """
        Creates a 5x5 Playfair cipher matrix from the given key.
        """
        # Replace "J" with "I" in the key and convert to uppercase
        key = key.replace("J", "I").upper()

        # Create a set of the key and remove duplicates while preserving order
        key_set = []
        for letter in key:
            if letter not in key_set:
                key_set.append(letter)

        # Define the alphabet (excluding 'J')
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

        # Add the remaining letters of the alphabet to the matrix
        remaining_letters = [letter for letter in alphabet if letter not in key_set]
        matrix = key_set + remaining_letters

        # Create a 5x5 matrix
        playfair_matrix = [matrix[i:i + 5] for i in range(0, len(matrix), 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix: list, letter: str) -> tuple:
        """
        Finds the row and column coordinates of a letter in the Playfair cipher matrix.
        """
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
    def playfair_encrypt(self, plain_text: str, matrix: list) -> str:
        # Replace 'J' with 'I' and convert text to uppercase
        plain_text = plain_text.replace("J", "I").upper().replace(" ", "")
        encrypted_text = ""

        # Add padding if the plaintext length is odd
        if len(plain_text) % 2 != 0:
            plain_text += "X"

        for i in range(0, len(plain_text), 2):
            pair = plain_text[i:i + 2]
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
                # Rectangle: Swap columns
                encrypted_text += matrix[row1][col2]
                encrypted_text += matrix[row2][col1]

        return encrypted_text

    def playfair_decrypt(self, cipher_text: str, matrix: list) -> str:
        # Convert the cipher text to uppercase
        cipher_text = cipher_text.upper().replace(" ", "")
        decrypted_text = ""

        # Decrypt the pairs of characters
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i + 2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                # Same row: Move to the left
                decrypted_text += matrix[row1][(col1 - 1) % 5]
                decrypted_text += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                # Same column: Move up
                decrypted_text += matrix[(row1 - 1) % 5][col1]
                decrypted_text += matrix[(row2 - 1) % 5][col2]
            else:
                # Rectangle: Swap columns
                decrypted_text += matrix[row1][col2]
                decrypted_text += matrix[row2][col1]

        # Process the decrypted text to remove padding
        banro = ""
        for i in range(0, len(decrypted_text) - 1, 2):
            # If a pair contains 'X' inserted during encryption, exclude it
            if decrypted_text[i] == decrypted_text[i + 1] and decrypted_text[i + 1] == "X":
                banro += decrypted_text[i]
            else:
                banro += decrypted_text[i] + decrypted_text[i + 1]

        # Handle the last character (to remove 'X' if it was added for padding)
        if decrypted_text[-1] == "X" and len(decrypted_text) % 2 != 0:
            banro += decrypted_text[-2]
        else:
            banro += decrypted_text[-2] + decrypted_text[-1]

        return banro

    # Demo usage
if __name__ == "__main__":
    cipher = PlayFairCipher()
    key = input("Enter the cipher key: ")
    playfair_matrix = cipher.create_playfair_matrix(key)

    print("\nPlayfair Cipher Matrix:")
    for row in playfair_matrix:
        print(" ".join(row))
