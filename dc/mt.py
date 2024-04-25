from threading import Thread
import time


class Threads(Thread):
    def __init__(self):
        super().__init__(name="User Threads")
        print("User thread is created", self)
        self.start()

    def run(self):
        try:
            for i in range(8):
                print("Printing the count of Child Thread", i)
                time.sleep(0.8)
        except InterruptedException as e:
            print("User thread interrupted")
        print("Child thread run is over")


class Multithreading:
    def main(self):
        th = Threads()
        try:
            while th.is_alive():
                print("Parent thread will run till the Child thread is alive")
                time.sleep(1.5)
        except InterruptedException as e:
            print("Parent thread interrupted")
        print("Parent thread's run is over")


if __name__ == "__main__":
    m = Multithreading()
    m.main()
