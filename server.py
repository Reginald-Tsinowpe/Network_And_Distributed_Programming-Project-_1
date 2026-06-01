import socket
# from datetime import datetime here


# core variable declaration is done here to make it globally accessible by functions
HOST = '127.0.0.1'
PORT = 8080


# this is the main function of the script - its entry point. execution starts here
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen()
    print("sever started and listening")
    conn, addr = sock.accept()
    # now get the date and send to the connected address

    sock.close()


if __name__ == "__main__":
    main()
