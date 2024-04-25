def print_load(servers, processes):
    each = processes // servers
    extra = processes % servers
    total = 0
    for i in range(servers):
        if extra > 0:
            total = each + 1
            extra -= 1
        else:
            total = each
        print(f"Server {chr(ord('A') + i)} has {total} Processes")


def main():
    servers = int(input("Enter the number of servers: "))
    processes = int(input("Enter the number of Processes: "))
    while True:
        print_load(servers, processes)
        print(
            "1. Add Servers\n2. Remove Servers\n3. Add Processes\n4. Remove Processes\n5. Exit"
        )
        choice = int(input("Enter your choice: "))
        if choice == 1:
            servers += int(input("How many more servers?: "))
        elif choice == 2:
            servers -= int(input("How many servers to remove?: "))
        elif choice == 3:
            processes += int(input("How many more Processes?: "))
        elif choice == 4:
            processes -= int(input("How many Processes to remove?: "))
        elif choice == 5:
            return
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
