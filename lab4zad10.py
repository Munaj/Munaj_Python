import threading
import time

lis = []

def nalej(n):
    lis.append(n)
    
        
def pij(n):
    print(lis[n])

    

for i in range(6):
    x = threading.Thread(target = nalej,args=[i,])
    x.start()

    x.join()

    y = threading.Thread(target = pij,args=[i,])
    y.start()
    