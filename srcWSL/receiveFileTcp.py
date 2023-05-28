import socket
 
IP = '192.168.19.142'
PORT = 5000
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
 
def main():
    print("[STARTING] Server is starting.")
    """ Starting a TCP socket. """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
    """ Bind the IP and PORT to the server. """
    server.bind(ADDR)
 
    """ Server is listening, i.e., the server is now waiting for the client to connect. """
    server.listen()
    print("[LISTENING] Server is listening.")
 
    while True:
        """ Server has accepted the connection from the client. """
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")
 
        """ Receiving the filename from the client. """
        filename = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the filename.")
        print(f"[FILENAME] {filename}")
        file = open(filename, "wb")
        conn.send("Filename received.".encode(FORMAT))
 
        """ Receiving the file data from the client. """
        while True:
            data = conn.recv(SIZE)
            if not data:
                break
            file.write(data)
        print(f"[RECV] Receiving the file data.")
        conn.send("File data received".encode(FORMAT))
 
        """ Closing the file. """
        file.close()
 
        """ Closing the connection from the client. """
        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")
 
if __name__ == "__main__":
    main()
