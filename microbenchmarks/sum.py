import numpy as np
import hashlib
import timeit

setup = """data = np.random.rand(1000) > 0.5"""

tests = {
    "sum": """sum(data)""",
    "np.sum": """np.sum(data)""",
}

results = {}
for test_name, test_stmt in tests.items():
    times = timeit.repeat(
        setup=setup, stmt=test_stmt, repeat=10, number=100, globals={"np": np}
    )
    avg_time = sum(times) / len(times)
    results[test_name] = avg_time

for test_name, result in sorted(results.items(), key=lambda x: x[1]):
    print(f"{test_name:>18}: {result:03g}")
