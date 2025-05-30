import multiprocessing as mp

def demoFunc(targetDict):
    targetDict[1] = '1'
    targetDict['2'] = 2
    targetDict['a'] = 'a'
#словарь должен быть в глобальной области


if __name__ == '__main__':
    with mp.Manager() as manager:
        myDict = manager.dict()


        p = mp.Process(target=demoFunc, args=(myDict,))
        p.start()
        p.join()

        print(myDict)