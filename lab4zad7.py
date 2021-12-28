import threading
import time

def count(n):
    s = 1
    for i in range(1,n+1):
        s += i*3
        print("Thread(1): ",threading.get_ident() , "Value: ",s)
        if s % 2 == 0 :
            time.sleep(2)
        
def count2(n):
    s = 0
    for i in range(1,n+1):
        s += i
        print("Thread(2): ",threading.get_ident() , "Value: ",s)
        if s % 2 == 0 :
            time.sleep(2.1)

           

x = threading.Thread(target = count, args = (5,))
x.start()

y = threading.Thread(target = count2, args = (5,))
y.start()


