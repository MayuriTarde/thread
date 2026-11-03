import csv

# w is list of all workers
#worker is single selected worker
w = ["Worker_1", "Worker_2", "Worker_3"]

# Load of each worker
load = {
    "Worker_1": 0,
    "Worker_2": 0,
    "Worker_3": 0
}

# Read CSV
def read_data():
    data = []
    with open("workload_5.csv", "r") as f:
        reader = csv.DictReader(f)
        for task in reader:
            data.append(task)
    return data

# Main program
data = read_data()

print("Load Balancing using Round Robin")

for i, task in enumerate(data):

    worker = w[i % len(w)]

    task["assigned_worker"] = worker
    task["status"] = "ASSIGNED"

    load[worker] += int(task["compute_units"])

    print(task["job_id"], "assigned to", worker)

# Display worker loads
print("\nWorker Load Summary")

for worker in w:
    print(worker, "Load:", load[worker])

print("\nAll tasks assigned successfully")