import numpy as np
import timeit

setups = {
    "hit": """data = np.float64(0.1234)""",
    "miss": """data = float(0.1234)""",
}

tests = {
    "eafp": """
try:
    data.dtype
except AttributeError:
    pass
    """,
    "lbyl": """if hasattr(data, "dtype"): data.dtype""",
}

results = {}
for setup_name, setup_stmt in setups.items():
    for test_name, test_stmt in tests.items():
        test_name = f"{setup_name}, {test_name}"
        times = timeit.repeat(
            setup=setup_stmt, stmt=test_stmt, repeat=10, number=100000, globals={"np": np}
        )
        avg_time = sum(times) / len(times)
        results[test_name] = avg_time

for test_name, result in sorted(results.items(), key=lambda x: x[1]):
    print(f"{test_name:>18}: {result:03g}")
