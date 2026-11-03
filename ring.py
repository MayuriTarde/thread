
import csv

def read_data():
    data = []
    with open("ring.csv", "r") as file:
        reader = csv.DictReader(file, skipinitialspace=True)
        for task in reader:
            data.append(task)

    return data

data = read_data()
nodes = {}

for node in data:
    nodes[int(node["node_id"])] = node

alive = []
visited = []

for node in data:
    if node["is_active"].upper() == "TRUE":
        alive.append(int(node["node_id"]))

print("Coordinator failed")
print("Ring algo started")

current = min(alive)

while current not in visited:
    visited.append(current)
    print("Token passed to node", current)

    next_node = int(nodes[current]["next_node_id"])

    while next_node not in alive:
        next_node = int(nodes[next_node]["next_node_id"])

    current = next_node

leader = max(alive)

print("Election completed")
print("New leader is node", leader)
