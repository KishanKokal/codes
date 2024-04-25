def main():
    ns = int(input("Enter number of sites: "))
    ncs = int(input("Enter number of sites which want to enter critical section: "))

    ts = [0] * ns
    request = []
    mp = {}

    for _ in range(ncs):
        timestamp = int(input("\nEnter timestamp: "))
        site = int(input("Enter site number: "))
        ts[site - 1] = timestamp
        request.append(site)
        mp[timestamp] = site

    print("\nSites and Timestamp:\n")
    for i in range(len(ts)):
        print(i + 1, ts[i])

    for i in range(len(request)):
        print("\nRequest from site:", request[i])
        for j in range(len(ts)):
            if request[i] != (j + 1):
                if ts[j] > ts[request[i] - 1] or ts[j] == 0:
                    print(j + 1, "Replied")
                else:
                    print(j + 1, "Deferred")

    print()
    c = 0
    for timestamp, site in mp.items():
        print("Site", site, "entered Critical Section", "at timestamp", timestamp)


if __name__ == "__main__":
    main()
