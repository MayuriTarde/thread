
import csv

def read_data():
    data = []
    with open("berkeley.csv", "r") as file:
        reader = csv.DictReader(file)
        for task in reader:
            data.append(task)
    return data

data = read_data()

times = []

print("Polled node times")

for task in data:
    node = task["node_id"]
    time = int(task["clock_time_sec"])
    faulty = task["is_faulty"]

    print(node, ":", time)

    if faulty == "FALSE":
        times.append(time)
    else:
        print(node, "is faulty and discarded")

average = sum(times) / len(times)

print("\nAverage time:", average)

print("\nClock adjustment")

for task in data:
    node = task["node_id"]
    time = int(task["clock_time_sec"])

    adjustment = average - time

    print(node, "adjustment:", adjustment, "seconds")
