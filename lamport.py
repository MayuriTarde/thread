
import csv

clock = {
    "P1": 0,
    "P2": 0,
    "P3": 0
}

messages = {}
events = []

def read_data():
    data = []
    with open("lamport.csv", "r") as file:
        reader = csv.DictReader(file, skipinitialspace=True)
        for task in reader:
            data.append(task)
    return data

data = read_data()

for task in data:
    event = task["event_id"]
    process = task["process_id"]
    action = task["event_type"]
    target = task["message_to"]

    if action == "SEND":
        clock[process] += 1
        messages[(process, target)] = clock[process]

    elif action == "RECEIVE":
        received = messages[(target, process)]
        clock[process] = max(clock[process], received) + 1

    else:
        clock[process] += 1

    events.append((event, clock[process]))

    print(event, process, "Clock:", clock[process])

print("\nFinal Causal Order")

events.sort(key=lambda x: x[1])

for event in events:
    print(event[0], "Timestamp:", event[1])
