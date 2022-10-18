#learning how to do multiprocessing
import multiprocessing
import time
start = time.perf_counter()
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)
    print("Done sleeping")

#####old ways
# processes = []
# for _ in range(10):
#     p =  multiprocessing.Process(target= do_something, args = [1.5])
#     p.start()
#     processes.append(p)
#
# for p in processes:
#     p.join()



def do_something(seconds):
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)

    return f"Done sleeping... {seconds}"


#####new way to be able to work with threading ####
import concurrent.futures

with concurrent.futures.ProcessPoolExecutor() as executor:
    # f1 = executor.submit(do_something, 1)
    # f2 = executor.submit(do_something, 1)
    # print(f1.result())
    # print(f2.result())
    secs = [1,2,3,4,5]
    #Method 1
    # results = [executor.submit(do_something, sec) for sec in secs]
    #Method 2: Note that the order is the same order as the output.
    results = executor.map(do_something,secs)
    for f in concurrent.futures.as_completed(results):
        print(f.result())
finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} second(s)')



