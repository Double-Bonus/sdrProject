import argparse
import socket

IP = '192.168.19.142'
PORT = 5000
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def send_file(filename):
    """ Starting a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Connecting to the server. """
    client.connect(ADDR)

    try:
        """ Opening and reading the file data. """
        with open(filename, "rb") as file:
            data = file.read()

        """ Sending the filename to the server. """
        client.send(filename.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER]: {msg}")

        """ Sending the file data to the server. """
        client.send(data)
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER]: {msg}")

    except FileNotFoundError:
        print(f"[ERROR]: File '{filename}' not found.")

    """ Closing the connection from the server. """
    client.close()
    print("[CLIENT] Connection closed.")


def main():
    parser = argparse.ArgumentParser(description='Send files to a server.')
    parser.add_argument('filename', metavar='FILENAME', type=str, help='the name of the file to send')
    args = parser.parse_args()

    send_file(args.filename)


if __name__ == "__main__":
    main()