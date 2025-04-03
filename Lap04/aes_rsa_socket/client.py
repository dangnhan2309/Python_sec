from crypto.Cipher import AES, PKCS1_OAEP
from crypto.PublicKey import RSA
from crypto.Random import get_random_bytes
from crypto.Util.Padding import pad, unpad
import socket
import threading

# Kết nối với server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Tạo khóa RSA cho client
client_key = RSA.generate(2048)

# Nhận khóa công khai của server
server_public_key = RSA.import_key(client_socket.recv(2048))

# Gửi khóa công khai của client cho server
client_socket.send(client_key.publickey().export_key(format='PEM'))

# Nhận và giải mã khóa AES
encrypted_aes_key = client_socket.recv(2048)
cipher_rsa = PKCS1_OAEP.new(client_key)
aes_key = cipher_rsa.decrypt(encrypted_aes_key)

# Hàm mã hóa tin nhắn
def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

# Hàm giải mã tin nhắn
def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    ciphertext = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode()

# Nhận tin nhắn từ server
def receive_messages():
    while True:
        try:
            encrypted_message = client_socket.recv(1024)
            if not encrypted_message:
                print("Server đã đóng kết nối.")
                break
            decrypted_message = decrypt_message(aes_key, encrypted_message)
            print("Received:", decrypted_message)
        except Exception as e:
            print(f"Lỗi khi nhận tin nhắn: {e}")
            break

# Khởi động luồng nhận tin nhắn
receive_thread = threading.Thread(target=receive_messages, daemon=True)
receive_thread.start()

# Gửi tin nhắn
while True:
    message = input("Enter message ('exit' to quit): ")
    encrypted_message = encrypt_message(aes_key, message)
    client_socket.send(encrypted_message)
    if message.lower() == "exit":
        break

# Đóng kết nối
client_socket.close()
