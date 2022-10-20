#

## Sequential
#           1 second                1 second
#       |            |          |
#func()                 func()

#Threading

#IO bound -> waiting for input to works e.g reading and writing
#CPU bound-> crunching numbers

#For threading -> IO bound is faster
#For core -> CPU bound is faster

#Threading
#        1 second
#       |
#func()        1 second
#              |
#        func()
#running concurrently




# import threading
# import time
# start = time.perf_counter()
# def do_something(seconds):
#     print(f'Sleeping {seconds} second(s)')
#     time.sleep(seconds)
#     print("Done sleeping")
# t1 = threading.Thread(target = do_something)
# t2 = threading.Thread(target = do_something)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join() # complete before it continue on. without this will continue to run the stuff below.
#
# finish = time.perf_counter()
#
# print(f'Finished in {round(finish-start,2)} second(s)')