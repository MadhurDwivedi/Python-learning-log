import threading 
import time

# Indicates some task being done
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

# calculating time
time1 = time.perf_counter()

# Normal code
func(4)
func(2)
func(1)


# same code using threads
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])
t1.start()
t2.start()
t3.start()

# calculating time
time2 = time.perf_counter()
print(time2 - time1)