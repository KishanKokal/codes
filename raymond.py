class Node:
    def __init__(self, id, holder):
        self.id = id
        self.holder = holder
        self.q = []


def request(holder, req):
    n = list[holder - 1]
    n.q.append(req)
    print("Queue of", n.id, ":", n.q)
    if n.holder != n.id:
        request(n.holder, n.id)
    else:
        give_token(n.id)


def give_token(nid):
    n = list[nid - 1]
    next = n.q.pop(0)
    n.holder = next
    if next != nid:
        give_token(next)
    else:
        print_function()


def print_function():
    for n in list:
        print("id:", n.id, "Holder:", n.holder)


if __name__ == "__main__":
    list = []
    n1 = Node(1, 1)
    n2 = Node(2, 1)
    n3 = Node(3, 1)
    n4 = Node(4, 2)
    n5 = Node(5, 2)
    n6 = Node(6, 3)
    n7 = Node(7, 3)
    n8 = Node(8, 3)
    list.extend([n1, n2, n3, n4, n5, n6, n7, n8])

    while True:
        print(
            "Enter the ID of the node requesting access to the critical section (1-8), or 'exit' to quit:"
        )
        input_val = input()
        if input_val.lower() == "exit":
            break

        try:
            node_id = int(input_val)
            if node_id < 1 or node_id > 8:
                print("Invalid node ID. Please enter a number between 1 and 8.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid node ID or 'exit'.")
            continue

        request(node_id, node_id)
