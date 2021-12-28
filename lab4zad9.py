import threading
import time

lis = []

def count():
    for i in range(1,5):
        lis.append(i)
        #napełnianie 
        time.sleep(0.2)
    
        
def count2():
    for i in range(0,4):
        print(lis[i])

    

x = threading.Thread(target = count)
x.start()

x.join()

y = threading.Thread(target = count2)
y.start()



