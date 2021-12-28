import threading
import time

def count(n):
    for i in range(1,n+1):
        print(threading.get_ident())
        time.sleep(0.3)
        
def count2(n):
    for i in range(1,n+1):
        print(threading.get_ident())
        time.sleep(1)
        

x = threading.Thread(target = count, args = (5,))
x.start()

y = threading.Thread(target = count2, args = (5,))
y.start()


