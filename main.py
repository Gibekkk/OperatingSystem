import threading
import timeit
import random

start = timeit.default_timer()
data = range(10**9)
find = random.randint(0, len(data)-1)
# find = data[-1]
# print(data, ",", find)
threadCount = 10
threads = []

def search(find, data):
    for d in data:
        if d == find:
            print("Found!")
            break

for i in range(0, threadCount):
    if i == threadCount - 1:
        searchData = data[(len(data) // threadCount) * i : len(data)]
    else:
        searchData = data[(len(data) // threadCount) * i : (len(data) // threadCount) * (i + 1) - 1]
    # print(searchData)
    thread = threading.Thread(target = search, args = (find, searchData), name = f"thread{i}")
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

stop = timeit.default_timer()
print('Time: ', stop - start)  