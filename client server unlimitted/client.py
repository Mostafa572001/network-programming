import socket

def start_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to server on {host}:{port}")

    while True:
        message = input("Enter message to send (or type 'exit' to quit): ")
        if message.lower() == "exit":
            break

        client_socket.sendall(message.encode())  # Send message to server

    client_socket.close()

if __name__ == "__main__":
    HOST = "127.0.0.1"  # localhost
    PORT = 12345  # Same port as the server

    start_client(HOST, PORT)
