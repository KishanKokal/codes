import socket

# Define host and port
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the address
    s.bind((HOST, PORT))
    # Listen for incoming connections
    s.listen()
    print("Server is listening for connections...")
    # Accept a connection from the client
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        while True:
            # Receive data from the client
            data = conn.recv(1024)
            if not data:
                break
            print("Received:", data.decode())
            # Send a response back to the client
            conn.sendall(data)
