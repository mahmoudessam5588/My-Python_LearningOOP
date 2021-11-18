from multiprocessing import process
from multiprocessing.context import Process
import os
import time


def multi_numbers():
    for i in range(100):
        i+i
        print(i)


processes = []
process_count = os.cpu_count()

# create process
for i in range(process_count):
    p = Process(target=multi_numbers)
    processes.append(p)
# start
for p in processes:
    p.start()
# join
for p in processes:
    p.join()
print('end main')
