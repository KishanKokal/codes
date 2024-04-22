class Pro:
    def __init__(self, id):
        self.id = id
        self.act = True


class Bully:
    def __init__(self):
        self.TotalProcess = 0
        self.process = []

    def main(self):
        object = Bully()
        numProcesses = int(input("Total number of processes: "))
        object.initialize(numProcesses)
        object.election()

    def initialize(self, num_processes):
        print("No of processes", num_processes)
        self.TotalProcess = num_processes
        self.process = [Pro(i) for i in range(self.TotalProcess)]

    def election(self):
        process_to_fail = int(input("Enter the process number to fail: "))
        if process_to_fail < 0 or process_to_fail >= self.TotalProcess:
            print("Invalid process number. Please enter a valid process number.")
            return

        print("Process no", self.process[process_to_fail].id, "fails")
        self.process[process_to_fail].act = False

        initialized_process = int(input("Enter the process initiating the election: "))
        print("Election Initiated by", initialized_process)
        init_by = initialized_process

        for i in range(init_by, self.TotalProcess - 1):
            if self.process[i].act:
                print("Process", i, "passes Election(", i, ")", "to", i + 1)
            else:
                print("Process", i - 1, "passes Election(", i - 1, ")", "to", i + 1)

        if self.process[self.TotalProcess - 1].act:
            coordinator_id = self.TotalProcess - 1
        else:
            coordinator_id = self.TotalProcess - 2

        print("Process", coordinator_id, "is the process with max ID")
        for j in range(coordinator_id):
            if self.process[j].act:
                print(
                    "Process",
                    coordinator_id,
                    "passes Coordinator(",
                    coordinator_id,
                    ") message to process",
                    self.process[j].id,
                )


if __name__ == "__main__":
    Bully().main()
