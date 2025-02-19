import socket
import os
import pyautogui  # Requires installation: pip install pyautogui

SERVER_HOST = os.getenv('SERVER_HOST', 'localhost')
SERVER_PORT = int(os.getenv('SERVER_PORT', 9999))

def send_mouse_event(event_type, x, y):
    try:
        # Create socket connection
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        
        # Send mouse event data to server
        data = f"{event_type}:{x}:{y}"
        client_socket.sendall(data.encode('utf-8'))
        print(f"[*] Sent mouse event ({event_type}) to {SERVER_HOST}:{SERVER_PORT}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client_socket.close()

if __name__ == '__main__':
    # Example: Send mouse click at (100, 100)
    send_mouse_event('click', 100, 100)
