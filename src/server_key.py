import socket
import os
import pyautogui  # Requires installation: pip install pyautogui

SERVER_HOST = os.getenv('SERVER_HOST', 'localhost')
SERVER_PORT = int(os.getenv('SERVER_PORT', 9999))

def receive_key_presses():
    try:
        # Create socket connection
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((SERVER_HOST, SERVER_PORT))
        server_socket.listen(5)
        print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")

            # Receive key press data
            key = client_socket.recv(1024).decode('utf-8')
            
            # Simulate key press on server
            pyautogui.press(key)
            print(f"[*] Simulated key press '{key}' on server")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        server_socket.close()

if __name__ == '__main__':
    receive_key_presses()
