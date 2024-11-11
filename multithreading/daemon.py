import threading
import time

def main():
    print(f"This is the main thread")

def counter(thread_name:str):
    count = 0 
    while True:
        count += 1
        print(f"count in {thread_name} = {count}")
        time.sleep(1)
        if count>10:
            break

t1 = threading.Thread(target=counter,daemon=True,args=('t1',))
t2 = threading.Thread(target=counter,daemon=True,args=('t2',))

t1.start()
t2.start()

main()