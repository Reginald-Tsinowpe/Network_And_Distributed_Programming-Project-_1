import socket

HOST = '127.0.0.1'
PORT = 8080

client_socket = None


def create_client():
    global client_socket

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return client_socket


# @geraldley
def connect_to_server():
    try:
        client_socket.connect((HOST, PORT))
        print("Connected to server.")
    except Exception:
        handle_connection_error()


# @jona-kis
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024)

            if not message:
                handle_disconnect()
                break

            display_message(message.decode())

        except:
            handle_disconnect()
            break


# @sedem-edward
def display_message(message):
    print(f"Received -> {message}")


# @victor
def handle_connection_error():
    print("Unable to connect to server.")


# @joshua
def handle_disconnect():
    print("Disconnected from server.")
    client_socket.close()


# @victor
def main():
    create_client()
    connect_to_server()
    receive_messages()


if __name__ == "__main__":
    main()
