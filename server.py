import socket
# from datetime import datetime here


# core variable declaration is done here to make it globally accessible by functions
HOST = '127.0.0.1'
PORT = 8080

# @joshua


def create_server():
    pass

# @safia


def start_server():
    pass

# @salma


def accept_client(server_socket):
    """
    Blocks until a new client connects, then registers it and
    kicks off a thread to handle it.
    """
    try:
        client_socket, client_address = server_socket.accept()
        print(f"[NEW CONNECTION] {client_address} connected.")

        add_client(client_socket, client_address)
        start_client_thread(client_socket, client_address)

        return client_socket, client_address
    except OSError as e:
        # Happens e.g. if the server_socket is closed while accept() is blocking
        print(f"[ACCEPT ERROR] {e}")
        return None
   

# @roland


def add_client():
    pass


def remove_client():
    pass

# reginald


def get_clients():
    pass

# @sylvester


def start_client_thread():
    pass


# @rexfordayensu
from datetime import datetime

# @rex
def get_current_datetime():
    # Get the current local date and time
    now = datetime.now()
    
    # Format them cleanly as strings (or you can return raw date/time objects)
    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    
    # return a tuple of date and time
    return (current_date, current_time)

# ignore for now


def format_datetime():
    pass

# @will-cypher


def create_message():
    pass

# @ohenewa-a


def periodic_push():
    pass

# @tracy


def send_to_client():
    pass


# @reginald
def main():
    pass


if __name__ == "__main__":
    main()
