import time
import random


class Node:
    def __init__(self, node_id, clock_time):
        self.node_id = node_id
        self.clock_time = clock_time

    def synchronize_clock(self, master_time):
        self.clock_time = master_time


def master(node_list):
    # Request time from all nodes
    node_times_before = {}
    for node in node_list:
        node_times_before[node.node_id] = node.clock_time
        print("Master Node ===> ", node.node_id)
        print(f"{node.node_id} time: {node.clock_time} ===> Master Node")

    print("=" * 10)

    # Calculate average time
    average_time = sum(node_times_before.values()) / len(node_list)

    # Send synchronization message to all nodes
    for node in node_list:
        print(f"Master Node time: {average_time} ===> ", node.node_id)
        node.synchronize_clock(average_time)

    print("=" * 10)

    # Print before and after synchronization times for all nodes
    print("Before synchronization:")
    for node_id, time_before in node_times_before.items():
        print(f"Node {node_id} time: {time_before}")

    print("\nAfter synchronization:")
    for node in node_list:
        print(f"Node {node.node_id} time: {node.clock_time}")

    print("\nMaster node synchronized all nodes to time:", average_time)


if __name__ == "__main__":
    # Initialize master and nodes
    master_node = Node("Master", 0)
    nodes = [Node(f"Node-{i}", random.uniform(0, 10)) for i in range(1, 6)]

    # Simulate master node requesting and synchronizing time
    master(nodes)
