import socket
import threading
import time
from datetime import datetime

HOST = '127.0.0.1'
PORT = 8080

clients = []
server_socket = None


# @joshua
def create_server():
    global server_socket

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))

    return server_socket


# @safia
def start_server():
    server_socket.listen()
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        accept_client(server_socket)


# @salma
def accept_client(server_socket):
    """
    Blocks until a new client connects.
    """
    try:
        client_socket, client_address = server_socket.accept()
        print(f"[NEW CONNECTION] {client_address} connected.")

        add_client(client_socket)
        start_client_thread(client_socket)

        return client_socket, client_address

    except OSError as e:
        print(f"[ACCEPT ERROR] {e}")
        return None


# @roland
def add_client(client_socket):
    clients.append(client_socket)


def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)
    client_socket.close()


# @reginald
def get_clients():
    return clients


# @sylvester
def start_client_thread(client_socket):
    thread = threading.Thread(
        target=periodic_push,
        args=(client_socket,),
        daemon=True
    )
    thread.start()


# @rexfordayensu
def get_current_datetime():
    now = datetime.now()

    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")

    return current_date, current_time


# ignore for now
def format_datetime(date, time_):
    return f"Date: {date} | Time: {time_}"


# @will-cypher
def create_message():
    date, time_ = get_current_datetime()
    return format_datetime(date, time_)


# @ohenewa-a
def periodic_push(client):
    try:
        while True:
            message = create_message()
            send_to_client(client, message)
            time.sleep(10)
    except:
        remove_client(client)


# @tracy
def send_to_client(client, message):
    client.sendall(message.encode())


# @reginald
def main():
    create_server()
    start_server()


if __name__ == "__main__":
    main()
