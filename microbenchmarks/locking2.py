# Based on snippet from https://bugs.python.org/issue3001
from threading import Lock, RLock

REPEATS = 1000000

def do_nothing():
    pass

def RLockSpeed():
    import time, threading

    t = time.time()
    result = {}
    for i in range(REPEATS):
        do_nothing()
    result["empty loop"] = time.time() - t
    l = threading.Lock()
    t = time.time()
    for i in range(REPEATS):
        l.acquire()
        do_nothing()
        l.release()
    result["Lock"] = time.time() - t
    t = time.time()
    for i in range(REPEATS):
        with l:
            do_nothing()
    result["Lock_context"] = time.time() - t
    l = threading.RLock()
    t = time.time()
    for i in range(REPEATS):
        l.acquire()
        do_nothing()
        l.release()
    result["RLock"] = time.time() - t
    t = time.time()
    for i in range(REPEATS):
        with l:
            do_nothing()
    result["RLock_context"] = time.time() - t
    return result


if __name__ == "__main__":
    print(RLockSpeed())
