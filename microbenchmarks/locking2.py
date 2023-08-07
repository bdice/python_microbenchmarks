# Based on snippet from https://bugs.python.org/issue3001

REPEATS = 1000000


def do_nothing():
    pass


def RLockSpeed():
    import threading
    import time

    t = time.time()
    result = {}
    for i in range(REPEATS):
        do_nothing()
    result["empty loop"] = time.time() - t
    lock = threading.Lock()
    t = time.time()
    for i in range(REPEATS):
        lock.acquire()
        do_nothing()
        lock.release()
    result["Lock"] = time.time() - t
    t = time.time()
    for i in range(REPEATS):
        with lock:
            do_nothing()
    result["Lock_context"] = time.time() - t
    lock = threading.RLock()
    t = time.time()
    for i in range(REPEATS):
        lock.acquire()
        do_nothing()
        lock.release()
    result["RLock"] = time.time() - t
    t = time.time()
    for i in range(REPEATS):
        with lock:
            do_nothing()
    result["RLock_context"] = time.time() - t
    return result


if __name__ == "__main__":
    print(RLockSpeed())
