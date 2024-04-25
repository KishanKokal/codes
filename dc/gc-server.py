import socket
import threading


# Set up the server
def main():
    # Set up the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8080))
    server_socket.listen(5)
    print("Group Chat Server is running...")

    # Set to store connected client sockets and their names
    connected_clients = {}

    # Function to handle client connections
    def client_handler(client_socket, client_name):
        try:
            while True:
                message = client_socket.recv(1024).decode()
                if not message:
                    break
                elif message == "exit":
                    break
                elif message.startswith("/whisper"):
                    handle_whisper(message)
                else:
                    broadcast(client_name + ": " + message)
        except Exception as e:
            print("Error:", e)
        finally:
            client_socket.close()
            del connected_clients[client_name]
            broadcast_from_server(client_name + " has left the chat.")

    # Function to broadcast a message to all clients
    def broadcast(message):
        for name, sock in connected_clients.items():
            sock.sendall(message.encode())

    # Function to handle whisper messages
    def handle_whisper(message):
        parts = message.split(" ", 2)
        if len(parts) == 3:
            recipient = parts[1].strip()
            whisper_message = parts[2].strip()
            if recipient in connected_clients:
                connected_clients[recipient].sendall(
                    f"(whisper from {client_name}): {whisper_message}".encode()
                )
            else:
                connected_clients[client_name].sendall(
                    f"Recipient '{recipient}' is not connected.".encode()
                )
        else:
            connected_clients[client_name].sendall(
                "Invalid whisper command. Usage: /whisper recipient message".encode()
            )

    # Function to handle server messages
    def server_message_handler():
        try:
            while True:
                server_message = input()
                broadcast_from_server("[host]: " + server_message)
        except Exception as e:
            print("Error:", e)

    # Function to broadcast a message from the server
    def broadcast_from_server(message):
        for name, sock in connected_clients.items():
            sock.sendall(message.encode())

    # Thread to handle server messages
    threading.Thread(target=server_message_handler, daemon=True).start()

    # Main loop to accept client connections
    while True:
        client_socket, client_address = server_socket.accept()
        client_name = client_socket.recv(1024).decode()
        print(f"New client connected: {client_name}")
        connected_clients[client_name] = client_socket
        broadcast_from_server(f"{client_name} has joined the chat.")
        broadcast_from_server("New member has joined !!")
        threading.Thread(
            target=client_handler, args=(client_socket, client_name), daemon=True
        ).start()


if __name__ == "__main__":
    main()
