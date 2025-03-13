
from Lap2.cipher.caesar.caesar_cipher import CaesarCipher
from flask import Flask, request, jsonify
from Lap2.cipher.vigenere.vigenere_cypher import VigenereCipher
from Lap2.cipher.railfence.railfence_cypher import RailFenceCipher
from Lap2.cipher.playfair.playfair_cipher import PlayFairCipher
from Lap2.cipher.transposition.transposition_cipher import TranspositionCipher
# Initialize Flask app and CaesarCipher instance
app = Flask(__name__)
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence = RailFenceCipher()
playfair = PlayFairCipher()
transposition = TranspositionCipher()


#Route for encrypting text
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text =data['plain_text']

    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt(plain_text,key)
    return jsonify({'encrypted_message': encrypted_text})
@app.route("/api/caesar/dencrypt", methods=["POST"])
def caesar_dencrypt():
    data = request.json
    plain_text =data['plain_text']

    key = int(data['key'])
    dencrypted_text = caesar_cipher.decrypt(plain_text,key)
    return jsonify({'encrypted_message': dencrypted_text})

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
    return jsonify({'dencrypted_text ':dencrypted_text})

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
    return jsonify({'dencrypted_text ':dencrypted_text})


@app.route("/api/playfair/create_matrix", methods = ["POST"])
def playfair_create_matrix():
    data = request.json
    key = data['key']
    encrypted_text = playfair.create_playfair_matrix(key)
    return jsonify({'create_matrix ':encrypted_text})
@app.route("/api/playfair/encrypt", methods = ["POST"])
def playfair_encrypt():
    data = request.json
    plaintext = data['plain_text']
    key = data['key']
    matrix = playfair.create_playfair_matrix(key)
    encrypted_text = playfair.playfair_encrypt(plaintext,matrix)
    return jsonify({'encrypted_text ':encrypted_text})
@app.route("/api/playfair/dencrypt", methods = ["POST"])
def playfair_dencrypt():
    data = request.json
    plaintext = data['plain_text']
    key = data['key']
    matrix = playfair.create_playfair_matrix(key)
    dencrypted_text = playfair.playfair_encrypt(plaintext,matrix)
    return jsonify({'dencrypted_text ':dencrypted_text})


@app.route("/api/transition/encrypt", methods = ["POST"])
def transition_encrypt():
    data = request.json
    plaintext = data.get('plain_text')
    key = int(data.get('key'))

    encrypted_text = transposition.encrypt(plaintext,key)
    return jsonify({'encrypted_text ':encrypted_text})
@app.route("/api/transition/dencrypt", methods = ["POST"])
def transition_dencrypt():
    data = request.json
    plaintext = data.get('plain_text')
    key = int(data.get('key'))
    dencrypted_text = transposition.decrypt(plaintext, key)
    return jsonify({'dencrypted_text ':dencrypted_text})











if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

