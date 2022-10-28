import threading
import time 

def main():
#creating pool object and set max number of threads connections
    max_connections = 5
    pool = threading.BoundedSemaphore(max_connections)

    list = []
#cycle with 10 threads running 
    for i in range(10):
        thr = threading.Thread(target = test, args = (pool,), name =f'thread-{i+1}')
        list.append(thr)
        thr.start()
#checking list of processes with join()
    for i in list:
        i.join()
    
    print('All threads completed successfully !')


def test(pool): 
    with pool: 
        print(f'{threading.current_thread().name} : reached the end of the function')
        time.sleep(2)
    
#entry point
if __name__ == "__main__": 
    main()