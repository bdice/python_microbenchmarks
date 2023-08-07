import hashlib
import timeit

import numpy as np

setup = """\
data_array = np.random.rand(1000)
data_list = data_array.tolist()
"""

tests = {
    "sum array": """sum(data_array)""",
    "np.sum array": """np.sum(data_array)""",
    "sum list": """sum(data_list)""",
    "np.sum list": """np.sum(data_list)""",
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
