import socket


def main():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("localhost", 1200))

        print(" \n \t************* CLIENT PROCESS STARTED ********************** ")
        print(
            "\n ********* PLEASE ENTER THE VALUES OF Number 1 AND Number 2 TO PASS THEM TO SERVER PROCESS******** \n"
        )

        a = int(input("Enter Number 1: "))
        print("Number 1 ====>", a)
        client_socket.sendall(str(a).encode())

        b = int(input("Enter Number 2: "))
        print("Number 2 ====>", b)
        client_socket.sendall(str(b).encode())

        data = client_socket.recv(1024)
        result = int(data.decode())
        print(
            "\n.............CLIENT PROCESS HAS RECEIVED RESULT FROM SERVER...............\n"
        )
        print("\n THE ADDITION OF", a, "AND", b, "IS", result)

    except Exception as e:
        print("Exception is", e)

    finally:
        client_socket.close()


if __name__ == "__main__":
    main()
