import timeit

import numpy as np

setup = """\
data_array = np.random.rand(1000)
data_list = data_array.tolist()
"""

tests = {
    "float": """[isinstance(x, float) for x in data_list]""",
    "np.floating": """[isinstance(x, np.floating) for x in data_list]""",
    "float, np.floating": (
        """[isinstance(x, (float, np.floating)) for x in data_list]"""
    ),
    "np.floating, float": (
        """[isinstance(x, (np.floating, float)) for x in data_list]"""
    ),
    "float or np.floating": (
        """[(isinstance(x, float) or isinstance(x, np.floating)) for x in data_list]"""
    ),
}

results = {}
for test_name, test_stmt in tests.items():
    times = timeit.repeat(
        setup=setup, stmt=test_stmt, repeat=100, number=100, globals={"np": np}
    )
    avg_time = sum(times) / len(times)
    results[test_name] = avg_time

for test_name, result in sorted(results.items(), key=lambda x: x[1]):
    print(f"{test_name:>18}: {result:03g}")
