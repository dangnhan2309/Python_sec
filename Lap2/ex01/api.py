from cipher.caesar.caesar_cipher import CaesarCipher
from flask import Flask, request, jsonify

# Initialize Flask app and CaesarCipher instance
app = Flask(__name__)
caesar_cipher = CaesarCipher()


# Route for encrypting text
@app.route("/api/caesar/encrypt", methods=['POST'])
def caesar_encrypt():
    data = request.json
    plain_text = data.get('plain_text', '')
    key = int(data.get('key', 0))
    encrypted_text = caesar_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})


# Route for decrypting text
@app.route("/api/caesar/dencrypt", methods=['POST'])
def caesar_decrypt():
    data = request.json
    cipher_text = data.get('cipher_text', '')
    key = int(data.get('key', 0))
    decrypted_text = caesar_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

