import socket
import os
import pyautogui  # Requires installation: pip install pyautogui

SERVER_HOST = os.getenv('SERVER_HOST', 'localhost')
SERVER_PORT = int(os.getenv('SERVER_PORT', 9999))

def receive_mouse_events():
    try:
        # Create socket connection
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((SERVER_HOST, SERVER_PORT))
        server_socket.listen(5)
        print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")

            # Receive mouse event data
            data = client_socket.recv(1024).decode('utf-8')
            event_type, x, y = data.split(':')
            x, y = int(x), int(y)
            
            # Simulate mouse event on server
            if event_type == 'click':
                pyautogui.click(x, y)
                print(f"[*] Simulated mouse click at ({x}, {y})")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        server_socket.close()

if __name__ == '__main__':
    receive_mouse_events()
