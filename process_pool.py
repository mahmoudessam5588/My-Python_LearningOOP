from multiprocessing import Pool
"""process pool is used to manage multiple processes that controls a pool of workers process to which chips to be submitted and manage aviable processes for you and split it as data in smaller chunks which can be processed in parallel with other different processes"""
def cube(number):
    return number * number * number
if __name__ == '__main__':
    numbers = range(10)
    pool = Pool()
    # map ,apply , join ,close
    #pool.apply(cube,numbers[0])
    result =  pool.map(cube,numbers)
    pool.close()
    pool.join()
    print(result)