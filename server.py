import socket
import threading
from datetime import datetime

# Server Configuration
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Arbitrary non-privileged port

def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")
    try:
        # Get current date and time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"Server Time: {current_time}\n"
        
        # Send the date string encoded in bytes
        client_socket.sendall(message.encode('utf-8'))
    except Exception as e:
        print(f"[ERROR] Handling client {client_address}: {e}")
    finally:
        client_socket.close()
        print(f"[DISCONNECTED] {client_address} disconnected.")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Allow immediate reuse of the port after stopping the server
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server.bind((HOST, PORT))
    server.listen()
    print(f"[STARTING] Date Server is listening on {HOST}:{PORT}...")

    try:
        while True:
            client_socket, client_address = server.accept()
            # Handle each client connection in a separate thread
            thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            thread.start()
    except KeyboardInterrupt:
        print("\n[SHUTTING DOWN] Server is stopping safely.")
    finally:
        server.close()

if __name__ == "__main__":
    start_server()