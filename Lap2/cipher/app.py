from flask import Flask, render_template, request
from Lap2.cipher.caesar import CaesarCipher
from Lap2.cipher.vigenere import VigenereCipher
from Lap2.cipher.playfair import PlayFairCipher
app = Flask(__name__)  # Đổi "__name__" thành __name__

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')
@app.route("/play_fair")
def playfair():
    return render_template('play_fair.html')
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/encrypt", methods=['POST'])  # Đúng đường dẫn
def caesar_encrypt():
    text = request.form["InputPlainText"]
    key = int(request.form["InputKeyPlain"])
    Caesar = CaesarCipher()
    encrypt_text = Caesar.encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted_text: {encrypt_text}"


@app.route("/decrypt", methods=['POST'])  # Đổi route decrypt
def caesar_decrypt():
    text = request.form['InputCipherText']
    key =int(request.form['InputKeyCipher'])
    Caesar = CaesarCipher()
    decrypt_text = Caesar.decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypt_text: {decrypt_text}"@app.route("/decrypt", methods=['POST'])  # Đổi route decrypt

@app.route("/vigenere/encrypt", methods=['POST'])  # Đúng đường dẫn
def vigenere_encrypted():
    text = request.form["InputPlainText"]
    key = request.form["InputKeyPlain"]
    vigenere = VigenereCipher()
    encrypt_text = vigenere.vigenere_encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted_text: {encrypt_text}"
@app.route("/vigenere/dencrypt", methods= ['POST'])
def vigenere_decrypted():
    text = request.form['InputCipherText']
    key =request.form['InputKeyCipher']
    vigenere = VigenereCipher()
    decrypt_text = vigenere.vigenere_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypt_text: {decrypt_text}"

@app.route("/play_fair/encrypt", methods=['POST'])  # Đúng đường
def playfairencrypt():
    text = request.form["InputPlainText"]
    key = request.form["InputKeyPlain"]
    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)
    encrypt_text = playfair.playfair_encrypt(text,matrix)
    return f"text: {text}<br/>key: {key}<br/>encrypted_text: {encrypt_text}<br/>matrix: {matrix}"
@app.route("/play_fair/dencrypt", methods= ['POST'])
def playfairdecrypt():
    text = request.form['InputCipherText']
    key =request.form['InputKeyCipher']
    play_fair = PlayFairCipher()
    encrypted_text = playfair.create_playfair_matrix(key)
    decrypt_text = play_fair.playfair_decrypt(text,encrypted_text)
    return f"text: {text}<br/>key: {key}<br/>decrypt_text: {decrypt_text}"

@app.route("/playfair/create_matrix", methods = ["POST"])
def playfair_create_matrix():
    key =request.form['InputKeyCipher']
    play_fair = PlayFairCipher()
    encrypted_text = playfair.create_playfair_matrix(key)
    return f"Key: {key}<br/>Matrix: {encrypted_text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)