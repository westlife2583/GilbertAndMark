import twstock
import multiprocessing
import threading
import time
import datetime
import elasticsearch

allStock = []
stocklist1 = []
stocklist2 = []
stocklist3 = []
stocklist4 = []

def stockQuery(code):
    print(twstock.realtime.get(code))

def stockQueryMultiProcess(stocklist, num):
    threads = []
    for stock in stocklist:
        threads.append(threading.Thread(target=stockQuery, args=(stock,)))
        threads[len(threads) - 1].start()
        print(num)

    for query in threads:
        query.join()


for i in twstock.codes.keys():
    if len(i) is 4:
        allStock.append(i)
        #stock = twstock.realtime.get(i)
        #print(stock)

x = int(len(allStock)/4)

print(len(allStock))
print(len(allStock)/4)
print(int(len(allStock)/4))

stocklist1 = allStock[:x]
stocklist2 = allStock[x+1:x*2]
stocklist3 = allStock[x*2+1:x*3]
stocklist4 = allStock[x*3+1:]

#print(stocklist1)
#print(stocklist2)
#print(stocklist3)
#print(stocklist4)

#stocklist1 = allStock[:len(allStock)/4]


#Multi-processing
"""
if __name__ == '__main__':
    multiprocessing.freeze_support()
    multiprocessing.set_start_method('spawn')
    processes = []
    while 1:
        processes.append(multiprocessing.Process(target=stockQueryMultiProcess, args=(stocklist1,1)))
        processes.append(multiprocessing.Process(target=stockQueryMultiProcess, args=(stocklist2,2)))
        processes.append(multiprocessing.Process(target=stockQueryMultiProcess, args=(stocklist3,3)))
        processes.append(multiprocessing.Process(target=stockQueryMultiProcess, args=(stocklist4,4)))
        for pro in processes:
            pro.start()

        for pro in processes:
            pro.join()

        time.sleep(5)
"""

# Multi-Thread
"""
while 1:
    #print(twstock.codes.keys())
    threads = []
    i = 0
    print(datetime.datetime.now())
    for stock in allStock:
        threads.append(threading.Thread(target = stockQuery, args = (stock,)))
        threads[len(threads)-1].start()
        print(i)
        i += 1

    for query in threads:
        query.join()

    print(datetime.datetime.now())
    time.sleep(5)
"""

while(1):
    now = time.localtime(time.time())
    #if now.tm_hour >= 9:
    #    if now.tm_hour <= 12:
    #        break;
    #    if now.tm_hour <= 13 and now.tm_min <= 31:
    #        break;
    #print(allStock)
    stock = twstock.realtime.get(['1258', '1259'])
    print(stock)
    time.sleep(5)


"""
while(1):x
    stock = twstock.realtime.get('6488')
    print(stock)
    time.sleep(5)
"""
