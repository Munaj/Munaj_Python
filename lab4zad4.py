import time
from threading import Timer

def display(msg):
    print(msg + " " + time.strftime("%H:%M:%S"))

def run_once():
    display("Run once")
    t= Timer(5, display,["Timeout"])
    t.start()

run_once()
for i in range(10):
    x = 10-i
    print(str(x)+" "+ time.strftime("%H:%M:%S") )
    time.sleep(1)