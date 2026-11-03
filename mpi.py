
import csv
import threading

B = [
    [1, 2, 0, 1],
    [0, 1, 3, 2],
    [2, 0, 1, 1],
    [1, 1, 0, 2]
]

result = []

def read_data():
    data = []
    with open("matrix_38.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append([
                int(row["col_0"]),
                int(row["col_1"]),
                int(row["col_2"]),
                int(row["col_3"])
            ])
    return data

def multiply(row):
    ans = []

    for j in range(4):
        total = 0

        for k in range(4):
            total += row[k] * B[k][j]

        ans.append(total)

    result.append(ans)
    print("Worker calculated:", ans)

data = read_data()

thread = []

print("Master scattering rows")

for row in data:
    t = threading.Thread(target=multiply, args=(row,))
    thread.append(t)
    t.start()

for t in thread:
    t.join()

print("\nMaster gathering results")
print("Final Matrix:")

for row in result:
    print(row)
