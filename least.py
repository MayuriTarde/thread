import csv

w = ["worker_1", "worker_2", "worker_3"]

load = {
    "worker_1": 0,
    "worker_2": 0,
    "worker_3": 0
}

def read_data():
    data = []
    with open("task_5.csv", "r") as file:
        reader = csv.DictReader(file, skipinitialspace=True)
        for task in reader:
            data.append(task)
    return data

data = read_data()

print("Load Balancing using Least Connections")

for task in data:

    worker = min(w, key=lambda x: load[x])

    task["assigned_worker"] = worker
    task["status"] = "ASSIGNED"

    load[worker] += 1

    print(task["job_id"], "assigned to", worker)

print("\nLoad Summary")

for worker in w:
    print(worker, "connections:", load[worker])