import socket
import threading
import time

HOST = '127.0.0.1'
PORT = 65432

def request_date(client_id):
    """Connects to the server, receives the date, and prints it."""
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))
        
        # Receive data from the server (up to 1024 bytes)
        data = client.recv(1024).decode('utf-8')
        print(f"[CLIENT {client_id}] Received -> {data.strip()}")
        
        client.close()
    except ConnectionRefusedError:
        print(f"[CLIENT {client_id}] Error: Could not connect to server. Is it running?")

def add_clients(count=5):
    """
    Spins up multiple client connections simultaneously to test 
    how the multi-threaded server handles concurrent requests.
    """
    print(f"[SIMULATION] Creating {count} parallel clients...")
    threads = []
    
    for i in range(1, count + 1):
        # Create a thread for each distinct client request
        t = threading.Thread(target=request_date, args=(i,))
        threads.append(t)
        t.start()
        # Tiny delay just so console logs don't completely scramble over each other
        time.sleep(0.1)

    # Wait for all client tasks to finish
    for t in threads:
        t.join()
        
    print("[SIMULATION] All clients handled successfully.")

if __name__ == "__main__":
    # Run the client simulation with 5 concurrent clients
    add_clients(count=5)