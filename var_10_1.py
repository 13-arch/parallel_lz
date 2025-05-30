from threading import Thread, Event
from time import sleep, time


event = Event()


def worker(name: str):   
   event.wait()
   print(f"Worker: {name}")


event.clear()


workers = [Thread(target=worker, args=(f"potok {i}",)) for i in range(10)]
for w in workers:
   w.start()

print("Main thread")

event.set()
