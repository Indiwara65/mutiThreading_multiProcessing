# Multi Threading
## Control Flow
* in multithreading the control flow is swiched between threads automatically every GIL release or
* can be triggered manually by using time.sleep() where the control is handed over to a different thread when the execution reaches time.sleep()

## Deamon Thread
* A deamon thread is a thread which runs in the background and stops when all other threads stops executing.
* A thread can be defined as a deamon thread by setting deamon=True when defining the thread.
* eg - threading.Thread(target=function, deamon=True)

## Awiat
* Threads can be awiated where until they are executed and finished all other threads will not start.
* This can be done using .join() function after starting a thread.
*eg :
    * t1 = threading.Thread(traget=function1)
    * t2 = threading.Thread(target=function2)
    * t3 = threading.Thread(target=function3)
    * t1.start()
    * t2.start()
    * t1.join()
    * t2.join()
    * t3.start()
    * main()
* In the above exaple t3 thrad and main() function will not be run until the t1 and t2 threads are completed.