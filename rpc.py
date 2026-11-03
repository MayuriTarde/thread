
import csv

def processData(value):
    return value * 2

def calculateSquare(value):
    return value * value

def calculateCube(value):
    return value * value * value

def read_data():
    data = []
    with open("rpc_calls_41.csv", "r") as file:
        reader = csv.DictReader(file)
        for task in reader:
            data.append(task)
    return data

data = read_data()

for task in data:
    call_id = task["call_id"]
    client = task["client_name"]
    method = task["method_name"]
    value = int(task["param_value"])

    print("\n[DISPATCH]")
    print(client, "invoking", method)

    print("[SERVER EXECUTION]")

    if method == "processData":
        result = processData(value)

    elif method == "calculateSquare":
        result = calculateSquare(value)

    elif method == "calculateCube":
        result = calculateCube(value)

    else:
        print("Method not found")
        continue

    print("Processing parameter:", value)
    print("[RETURN]")
    print("Call ID:", call_id, "Result:", result)
