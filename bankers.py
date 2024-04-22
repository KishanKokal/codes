def is_safe(processes, avail, maxm, allot):
    need = []
    for i in range(len(processes)):
        need.append([0] * len(avail))
        for j in range(len(avail)):
            need[i][j] = maxm[i][j] - allot[i][j]

    finish = [0] * len(processes)
    safe_seq = []
    work = avail[:]

    while True:
        found = False
        for i in range(len(processes)):
            if finish[i] == 0:
                if all(need[i][j] <= work[j] for j in range(len(avail))):
                    for j in range(len(avail)):
                        work[j] += allot[i][j]
                    safe_seq.append(i)
                    finish[i] = 1
                    found = True
                    break
        if not found:
            break

    return all(finish), safe_seq


def main():
    n = int(input("Enter number of processes: "))
    m = int(input("Enter number of resources: "))

    print("Enter Allocation Matrix:")
    allocation = [list(map(int, input().split())) for _ in range(n)]

    print("Enter Max Matrix:")
    max_matrix = [list(map(int, input().split())) for _ in range(n)]

    print("Enter Available Resources:")
    available = list(map(int, input().split()))

    processes = [i for i in range(n)]

    safe, sequence = is_safe(processes, available, max_matrix, allocation)

    if safe:
        print("System is in safe state.")
        print("Safe sequence is:", [i + 1 for i in sequence])
    else:
        print("System is in unsafe state.")
        for i, process in enumerate(processes):
            if process not in sequence:
                print("Resources cannot be granted for process", process + 1)

    for i in sequence:
        print("Resources granted for process", i + 1, "successfully.")
        print("Available resources after process", i + 1, ":")
        available = [avail + alloc for avail, alloc in zip(available, allocation[i])]
        print(*available)


if __name__ == "__main__":
    main()
