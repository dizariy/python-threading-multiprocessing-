import multiprocessing 
import time 

def main ():
    #creating RLock and Barrier objects 
    locker = multiprocessing.RLock()
    barrier = multiprocessing.Barrier(5)
    
    list = []
    
#cycle with 10 processes running 
    for i in range(10):
        pr = multiprocessing.Process(target = test, args = (locker,barrier,), name= f'process-{i}')
        list.append(pr)
        pr.start()

#checking list of processes with join()
    for i in list:
        i.join()

    print('All processes completed successfully !')



#function with RLock and Barrier objects 
def test(lock, bar): 
    with lock: 
        print(f'function start Process: {multiprocessing.current_process().name}')

    #wait for 5 processes to reach this part of code 
    bar.wait()
    print(f' {multiprocessing.current_process().name} : reached the end of the function')

    time.sleep(1) 


# entry point
if __name__ == "__main__": 
    main()