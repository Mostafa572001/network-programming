import socket

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server is listening on {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connection established from {addr}")

        while True:
            data = conn.recv(1024)  # Receive data (up to 1024 bytes)
            if not data:
                break
            print(f"Received data from client: {data.decode()}")

        conn.close()

if __name__ == "__main__":
    HOST = "127.0.0.1"  # localhost
    PORT = 12345  # Arbitrary port number

    start_server(HOST, PORT)
