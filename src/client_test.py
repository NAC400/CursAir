import socket
import os

# Load environment variables or use default values
SERVER_HOST = os.getenv('SERVER_HOST', 'localhost')
SERVER_PORT = int(os.getenv('SERVER_PORT', 9999))

def send_message(message):
    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to server
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        print(f"[*] Connected to {SERVER_HOST}:{SERVER_PORT}")

        # Send data to server
        client_socket.sendall(message.encode('utf-8'))
        print(f"[*] Sent: {message}")

        # Receive response from server
        response = client_socket.recv(1024).decode('utf-8')
        print(f"[*] Received: {response}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the socket
        client_socket.close()

if __name__ == '__main__':
    # Example usage: sending a message to the server
    message_to_send = "Hello, server!"
    send_message(message_to_send)
