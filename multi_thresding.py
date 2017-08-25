from multiprocessing import Pool


def function_i(i, j):
    print ("Now i=%d and j=%d" % (i, j))


pool = Pool(processes=6)

for i in range(1000000):
    for j in range(100):
        pool.apply_async(function_i, args=(i, j))

pool.close()
pool.join()
