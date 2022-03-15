import socket
import threading

host = "0.0.0.0"
port = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f'[*] Listening on {host}:{port}')

    while True:
        client, address = server.accept()
        print(f"Client: {client}")
        print(f"Address: {address}")
        print(f"[*] Accepted connections from {address[0]}:{address[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(4096)
        print(f"[*] Recieved {request.decode()}")
        sock.send(b'ACK')

if __name__ == '__main__':
    main()