def main():
    numProcesses = int(input("Enter the number of processes: "))
    numResources = int(input("Enter the number of resources: "))

    # Input allocation matrix
    print("Enter the allocation matrix:")
    allocationMatrix = []
    for i in range(numProcesses):
        row = list(map(int, input().split()))
        allocationMatrix.append(row)

    # Input max matrix
    print("Enter the max matrix:")
    maxMatrix = []
    for i in range(numProcesses):
        row = list(map(int, input().split()))
        maxMatrix.append(row)

    # Input available resources
    print("Enter the available resources:")
    availableResources = list(map(int, input().split()))

    isFinished = [0] * numProcesses
    safeSequence = []
    needMatrix = [
        [maxMatrix[i][j] - allocationMatrix[i][j] for j in range(numResources)]
        for i in range(numProcesses)
    ]

    for k in range(numProcesses):
        for i in range(numProcesses):
            if isFinished[i] == 0:
                flag = 0
                for j in range(numResources):
                    if needMatrix[i][j] > availableResources[j]:
                        flag = 1
                        break
                if flag == 0:
                    safeSequence.append(i)
                    for y in range(numResources):
                        availableResources[y] += allocationMatrix[i][y]
                    isFinished[i] = 1

    flag = 1
    for i in range(numProcesses):
        if isFinished[i] == 0:
            flag = 0
            print("The system is not safe.")
            break

    if flag == 1:
        print("SAFE Sequence:", end=" ")
        for i in range(numProcesses - 1):
            print("P%d ->" % safeSequence[i], end=" ")
        print("P%d" % safeSequence[numProcesses - 1])


if __name__ == "__main__":
    main()
