
import csv

def read_data():
    data = []
    with open("cristian.csv", "r") as file:
        reader = csv.DictReader(file)
        for task in reader:
            data.append(task)
    return data

data = read_data()

for task in data:
    client = task["client_id"]

    t0 = float(task["t0_send_ms"])
    server = float(task["t_server_ms"])
    t1 = float(task["t1_recv_ms"])

    rtt = t1 - t0

    estimated = server + (rtt / 2)

    offset = estimated - t1

    adjusted_time = t1 + offset

    print("\nClient:", client)
    print("RTT:", rtt, "ms")
    print("Estimated Server Time:", estimated, "ms")
    print("Clock Offset:", offset, "ms")
    print("Adjusted Client Time:", adjusted_time, "ms")
