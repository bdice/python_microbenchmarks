import timeit
from threading import Lock, RLock

setup = """l = Lock()
r = RLock()
def func():
    pass
"""

tests = {
    "func": """func(); func()""",
    "lock": """l.acquire(); l.release()""",
    "rlock": """r.acquire(); r.release()""",
    "lock_context": """with l: pass""",
    "rlock_context": """with r: pass""",
}

results = {}
for test_name, test_stmt in tests.items():
    times = timeit.repeat(
        setup=setup,
        stmt=test_stmt,
        repeat=10,
        number=1000000,
        globals={"Lock": Lock, "RLock": RLock},
    )
    avg_time = sum(times) / len(times)
    results[test_name] = avg_time

for test_name, result in sorted(results.items(), key=lambda x: x[1]):
    print(f"{test_name:>18}: {result:03g}")
