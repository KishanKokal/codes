from datetime import datetime


class Berkley:
    def diff(self, h, m, s, nh, nm, ns):
        dh = h - nh
        dm = m - nm
        ds = s - ns
        diff = (dh * 60 * 60) + (dm * 60) + ds
        return diff

    def average(self, diff, n):
        total = sum(diff)
        average = total / (n + 1)
        print("The average of all time differences is", average)
        return average

    def sync(self, diff, n, h, m, s, nh, nm, ns, average):
        for i in range(n):
            diff[i] += average
            dh = int(diff[i]) // (60 * 60)
            diff[i] %= 60 * 60
            dm = int(diff[i]) // 60
            diff[i] %= 60
            ds = int(diff[i])
            nh[i] += dh
            if nh[i] > 23:
                nh[i] %= 24
            nm[i] += dm
            if nm[i] > 59:
                nh[i] += 1
                nm[i] %= 60
            ns[i] += ds
            if ns[i] > 59:
                nm[i] += 1
                ns[i] %= 60
            if ns[i] < 0:
                nm[i] -= 1
                ns[i] += 60

        h += int(average) // (60 * 60)
        if h > 23:
            h %= 24
        m += int(average) // (60 * 60 * 60)
        if m > 59:
            h += 1
            m %= 60
        s += int(average) % (60 * 60 * 60)
        if s > 59:
            m += 1
            s %= 60
        if s < 0:
            m -= 1
            s += 60

        print("The synchronized clocks are:\nTime Server --->", h, ":", m, ":", s)
        for i in range(n):
            print("Node", (i + 1), "--->", nh[i], ":", nm[i], ":", ns[i])


def main():
    b = Berkley()
    now = datetime.now()
    print("Enter number of nodes:")
    n = int(input())
    h = now.hour
    m = now.minute
    s = now.second
    nh = []
    nm = []
    ns = []

    for i in range(n):
        print("Enter time for node", (i + 1))
        nh.append(int(input("Hours: ")))
        nm.append(int(input("Minutes: ")))
        ns.append(int(input("Seconds: ")))

    for i in range(n):
        print("Time Server sent time", h, ":", m, ":", s, "to node", (i + 1))

    diff = [b.diff(h, m, s, nh[i], nm[i], ns[i]) for i in range(n)]
    for i in range(n):
        print(
            "Node", (i + 1), "sent time difference of", int(diff[i]), "to Time Server."
        )

    average = b.average(diff, n)
    b.sync(diff, n, h, m, s, nh, nm, ns, average)


if __name__ == "__main__":
    main()
