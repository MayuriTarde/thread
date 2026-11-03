import csv
import time
import threading

completed_task=[]
lock=threading.Lock()

def read_data():
    data =[]
    with open("task.csv","r") as file:
      reader = csv.DictReader(file)
      for task in reader:
         data.append(task)
    return data

def work(task):
   task_id=task["task_id"]
   worker= task["thread_name"]
   delay = int(task["burst_ms"])

   print(worker,"started",task_id)
   time.sleep(delay/1000)
   lock.acquire()
   print(worker,"acquire lock")
   completed_task.append(task_id)
   task["status"]="COMPLETED"

   print(task_id,"completed")
   lock.release()
   print(worker,"release lock"  )

data = read_data()
thread= []

for task in data:
   t= threading.Thread(target=(work),args=(task,))
   thread.append(t)
   t.start()

for t in thread:
   t.join()

print("all thread completed")
print("completed_task",completed_task)
