import socket
import ssl
import threading

# Server information
server_address = ('localhost', 12345)

# List of connected clients
clients = []

def handle_client(client_socket):
    # Add client to the list
    clients.append(client_socket)
    print("Connected to:", client_socket.getpeername())

    try:
        # Receive and send data
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print("Received:", data.decode('utf-8'))

            # Send data to all other clients
            for client in clients:
                if client != client_socket:
                    try:
                        client.send(data)
                    except:
                        clients.remove(client)

    except:
        clients.remove(client_socket)

    finally:
        print("Disconnected:", client_socket.getpeername())
        clients.remove(client_socket)
        client_socket.close()

# Create socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(5)

print("Server is waiting for connection...")

# Listen for connections
while True:
    client_socket, client_address = server_socket.accept()

    # Create SSL context
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="./certificates/server-cert.crt",
                            keyfile="./certificates/server-key.key")

    # Establish SSL connection
    ssl_socket = context.wrap_socket(client_socket, server_side=True)

    # Start a thread for each client
    client_thread = threading.Thread(target=handle_client, args=(ssl_socket,))
    client_thread.start()
