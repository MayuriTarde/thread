import csv

def read_data():
    data =[]
    with open ("task2.csv","r") as file:
        reader = csv.DictReader(file)
        for task in reader:
            data.append(task)
    return data

data = read_data()
alive = []

for node in data:
    if node["is_alive"].upper()=="TRUE":
        alive.append(int(node["node_id"]))

print("coordinator fail")
initiator = min(alive)
print("node",initiator,"start the election algo")
for node_id in alive:
    if initiator< node_id:
        print("election message sent to node",node_id)
        print("node",node_id,"replies Ok")

leader = max(alive)
print("node",leader,"become new leader")

for node_id in alive:
    print("coordinator message is sent to node",node_id)
print("new leader is node",leader)


