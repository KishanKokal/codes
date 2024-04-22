import socket


def main():
    try:
        # Create a server socket listening on port 12345
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind(("localhost", 12345))
            server_socket.listen(5)
            print("Server is running...")

            # Wait for client connection
            client_socket, client_address = server_socket.accept()
            print("Client connected.")

            # Create input and output streams for communication
            in_stream = client_socket.makefile("r")
            out_stream = client_socket.makefile("w")

            # Send and receive messages
            while True:
                message = in_stream.readline().strip()
                if not message:
                    break
                print("process 2:", message)

                response = input("Enter message to send to client: ")
                out_stream.write(response + "\n")
                out_stream.flush()

                # Read next message from the client
                print("Waiting for next message from client...")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
