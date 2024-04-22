class BullyAlgo:
    def __init__(self):
        self.coordinator = None
        self.processes = []
        self.crashed_processes = set()

    def election(self):
        print("\nThe Coordinator Has Crashed!")
        while True:
            crash = sum(1 for p in self.processes if p == 0)
            if crash == len(self.processes):
                print("\n*** All Processes Are Crashed ***")
                break
            else:
                print("\nEnter The Initiator")
                init = int(input())
                if (
                    init < 1
                    or init > len(self.processes)
                    or self.processes[init - 1] == 0
                ):
                    print("\nInvalid Initiator")
                    continue

                for i in range(init - 1, len(self.processes)):
                    print("Process", i + 1, "Called For Election")
                print("")
                for i in range(init - 1, len(self.processes)):
                    if self.processes[i] == 0:
                        print("Process", i + 1, "Is Dead")
                    else:
                        print("Process", i + 1, "Is In")

                for i in range(len(self.processes) - 1, -1, -1):
                    if self.processes[i] == 1:
                        self.coordinator = i + 1
                        print("\n*** New Coordinator Is", self.coordinator, "***")
                        return

    def bully(self):
        print("Enter The Number Of Processes:")
        n = int(input())
        self.processes = [1] * n
        self.coordinator = n

        while True:
            print("\n\t1. Crash A Process")
            print("\t2. Recover A Process")
            print("\t3. Display New Coordinator")
            print("\t4. Exit")

            ch = int(input())
            if ch == 1:
                print("\nEnter A Process To Crash")
                cp = int(input())
                if cp > n or cp < 1:
                    print("Invalid Process! Enter A Valid Process")
                elif self.processes[cp - 1] == 1 and self.coordinator != cp:
                    self.processes[cp - 1] = 0
                    print("\nProcess", cp, "Has Been Crashed")
                elif self.processes[cp - 1] == 1 and self.coordinator == cp:
                    self.processes[cp - 1] = 0
                    self.election()
                else:
                    print("\nProcess", cp, "Is Already Crashed")

            elif ch == 2:
                print("\nCrashed Processes Are:")
                for i, p in enumerate(self.processes):
                    if p == 0:
                        print(i + 1)
                print("Enter The Process You Want To Recover")
                rp = int(input())
                if rp < 1 or rp > n:
                    print("\nInvalid Process. Enter A Valid ID")
                elif self.processes[rp - 1] == 0 and rp > self.coordinator:
                    self.processes[rp - 1] = 1
                    print("\nProcess", rp, "Has Recovered")
                    self.coordinator = rp
                    print("\nProcess", rp, "Is The New Coordinator")
                elif len(self.crashed_processes) == n:
                    self.processes[rp - 1] = 1
                    self.coordinator = rp
                    print("\nProcess", rp, "Is The New Coordinator")
                    self.crashed_processes.remove(rp)
                elif self.processes[rp - 1] == 0 and rp < self.coordinator:
                    self.processes[rp - 1] = 1
                    print("\nProcess", rp, "Has Recovered")
                else:
                    print("\nProcess", rp, "Is Not A Crashed Process")

            elif ch == 3:
                print("\nCurrent Coordinator Is", self.coordinator)

            elif ch == 4:
                break

            else:
                print("\nInvalid Entry!")


def main():
    ob = BullyAlgo()
    ob.bully()


if __name__ == "__main__":
    main()
