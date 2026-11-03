
import csv

clock = {
    "P1": [0, 0, 0],
    "P2": [0, 0, 0],
    "P3": [0, 0, 0]
}

position = {
    "P1": 0,
    "P2": 1,
    "P3": 2
}

message = {}
events = []

def read_data():
    data = []
    with open("vector_events_6.csv", "r") as file:
        reader = csv.DictReader(file)
        for task in reader:
            data.append(task)
    return data

data = read_data()

for task in data:
    event = task["event_id"]
    process = task["process_id"]
    action = task["event_action"]
    target = task["target_process"]

    index = position[process]

    if action == "SEND":
        clock[process][index] += 1
        message[(process, target)] = clock[process].copy()

    elif action == "RECEIVE":
        received = message[(target, process)]

        for i in range(3):
            clock[process][i] = max(clock[process][i], received[i])

        clock[process][index] += 1

    events.append((event, clock[process].copy()))
    print(event, process, "Clock:", clock[process])

print("\nEvent Comparison")

for i in range(len(events)):
    for j in range(i + 1, len(events)):

        e1, v1 = events[i]
        e2, v2 = events[j]

        less = all(v1[k] <= v2[k] for k in range(3))
        greater = all(v1[k] >= v2[k] for k in range(3))

        if less and v1 != v2:
            print(e1, "causally precedes", e2)

        elif greater and v1 != v2:
            print(e2, "causally precedes", e1)

        else:
            print(e1, "and", e2, "are concurrent")
