import socket
import os
import pyautogui  # Requires installation: pip install pyautogui

SERVER_HOST = os.getenv('SERVER_HOST', 'localhost')
SERVER_PORT = int(os.getenv('SERVER_PORT', 9999))

def send_key_press(key):
    try:
        # Create socket connection
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        
        # Send key press data to server
        client_socket.sendall(key.encode('utf-8'))
        print(f"[*] Sent key press '{key}' to {SERVER_HOST}:{SERVER_PORT}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client_socket.close()

if __name__ == '__main__':
    # Example: Send 'A' key press
    send_key_press('a')
