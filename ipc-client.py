import socket


def main():
    try:
        # Connect to the server running on localhost, port 12345
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect(("localhost", 12345))
            print("Connected to server.")

            # Create input and output streams for communication
            in_stream = client_socket.makefile("r")
            out_stream = client_socket.makefile("w")

            # Send and receive messages
            while True:
                message = input(
                    "Enter message to send to server (or type 'exit' to quit): "
                )
                out_stream.write(message + "\n")
                out_stream.flush()

                if message.lower() == "exit":
                    break

                print("process 1:", in_stream.readline().strip())

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
