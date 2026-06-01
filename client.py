import socket


HOST = '127.0.0.1'
PORT = 8080


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    # receive
    # decode
    # output

    sock.close()


if __name__ == "__main__":
    main()
