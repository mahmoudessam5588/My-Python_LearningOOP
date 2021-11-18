from multiprocessing import Lock, Process
from multiprocessing import Queue
import os
import time

def square(numbers,queue,lock):
    for i in numbers:
        lock.acquire()
        queue.put(i*i)
        lock.release()
   
def minus_negative(numbers,queue,lock):
      for i in numbers:
        lock.acquire()
        queue.put(-1*i)
        lock.release()

if __name__ == '__main__':
    numbers = range(1,10)
    q = Queue()
    lock = Lock()
    p1 = Process(target=square,args=(numbers,q,lock))
    p2 = Process(target=minus_negative,args=(numbers,q,lock))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
while not q.empty():
    print(q.get())    
    