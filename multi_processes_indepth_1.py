from multiprocessing import Process , Value ,Array , Lock
import os
import time

def add_number(numbers,lock):
    for i in range(100):
        lock.acquire()
        time.sleep(0.01)
        for i in range(len(numbers)):
            numbers[i] += 1    
        lock.release()

if __name__ == '__main__':
    lock = Lock()
    shared_Array = Array('d',[0.0,100.0,200.0])
    print ('number in the begining is: ',shared_Array[:])
    p1 = Process(target=add_number,args=(shared_Array,lock))
    p2 = Process(target=add_number,args=(shared_Array,lock))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print ('number at the end is: ',shared_Array[:])           