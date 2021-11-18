from threading import Thread
import os
import time

def mult_numbers():
    for i in range(100):
        i+i
        print(i)
if __name__ == '__main__':
    threads = []
    num_threads = 20
#create threads
for i in range(num_threads):
    t = Thread(target=mult_numbers)
    threads.append(t)
#start
for t in threads:
    t.start()
#join
for t in threads:
    t.join()
print('end')                    