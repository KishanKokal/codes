import socket
import threading


def main():
    # Get client's name
    client_name = input("Enter your name: ")

    try:
        # Connect to the server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect(("localhost", 8080))
            print("Connected to server.")

            # Send client's name to the server
            writer = client_socket.makefile("w")
            writer.write(client_name + "\n")
            writer.flush()

            # Start a thread to read messages from the server
            reader_thread = threading.Thread(
                target=client_reader, args=(client_socket,)
            )
            reader_thread.start()

            # Send messages to the server
            while True:
                message = input()
                writer.write(message + "\n")
                writer.flush()
                if message == "exit":
                    break

    except Exception as e:
        print("Error:", e)


def client_reader(client_socket):
    try:
        # Read messages from the server
        with client_socket.makefile("r") as reader:
            while True:
                message = reader.readline().strip()
                if not message:
                    break
                print(message)

    except Exception as e:
        print("Error:", e)
    finally:
        print("Disconnected from the server.")


if __name__ == "__main__":
    main()
