
from Lap2.cipher.caesar.caesar_cipher import CaesarCipher
from flask import Flask, request, jsonify
from Lap2.cipher.vigenere.vigenere_cypher import VigenereCipher
from Lap2.cipher.railfence.railfence_cypher import RailFenceCipher
# Initialize Flask app and CaesarCipher instance
app = Flask(__name__)
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence = RailFenceCipher()


#Route for encrypting text
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text =data['plain_text']

    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt(plain_text,key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/vigenere/encrypt", methods = ["POST"])
def vigenere_encrypt():
    data = request.json
    plaintext = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plaintext,key)
    return jsonify({'encrypted_text ':encrypted_text})

@app.route("/api/vigenere/dencrypt", methods = ["POST"])
def vigenere_dencrypt():
    data = request.json
    cipher_text = data['plain_text']
    key = data['key']
    dencrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text,key)
    return jsonify({'encrypted_text ':dencrypted_text})

@app.route("/api/railfence/encrypt", methods = ["POST"])
def railfence_encrypt():
    data = request.json
    plain_text = data['plain_text']

    key = int(data['key'])
    encrypted_text = railfence.rail_fence_encrypt(plain_text,key)
    return jsonify({'encrypted_text ':encrypted_text})
@app.route("/api/railfence/dencrypt", methods = ["POST"])
def railfence_dencrypt():
    data = request.json
    plain_text = data['plain_text']

    key = int(data['key'])
    dencrypted_text = railfence.rail_fence_decrypt(plain_text,key)
    return jsonify({'encrypted_text ':dencrypted_text})



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

