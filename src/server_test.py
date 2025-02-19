import socket

# Server configuration
SERVER_HOST = '0.0.0.0'  # Listen on all network interfaces
SERVER_PORT = 9999

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the host and port
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    
    # Listen for incoming connections (max backlog of 5 connections)
    server_socket.listen(5)
    print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

    while True:
        # Wait for a connection
        client_socket, client_addr = server_socket.accept()
        print(f"[*] Accepted connection from {client_addr[0]}:{client_addr[1]}")

        # Handle client requests in a separate thread or process
        # For simplicity, let's just print received data for now
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received: {data}")

        # Optionally, parse data and perform actions (e.g., move mouse, type keystrokes)

        # Close client socket
        client_socket.close()

if __name__ == '__main__':
    start_server()
