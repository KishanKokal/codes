import socket


def main():
    print("\n **** INTERPROCESS COMMUNICATION ****\n")
    print("\n *** SERVER PROCESS STARTED ***\n")
    print(
        "\n * SERVER IS READY AND WAITING TO RECEIVE DATA FROM CLIENT PROCESS ON PORT 1200"
    )

    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("localhost", 1200))
        server_socket.listen(1)

        client_socket, client_address = server_socket.accept()
        print(
            "\n * Client is connected with IP address",
            client_address[0],
            "and port Number",
            client_address[1],
        )

        with client_socket:
            data = client_socket.recv(1024)
            a = int(data.decode())
            print("\n SERVER RECEIVED")
            print("\n Number 1 ====>", a)

            data = client_socket.recv(1024)
            b = int(data.decode())
            print("\n Number 2 ====>", b)

            c = a + b
            client_socket.sendall(str(c).encode())
            print(
                "\n SERVER PROCESS HAS EXECUTED REQUESTED PROCESS AND SENT RESULT",
                c,
                "TO THE CLIENT \n",
            )

    except Exception as e:
        print("Exception:", e)


if __name__ == "__main__":
    main()
