import os
import timeit

"""Getting the first item."""

setup = """iterable = range(1_000)"""
setup = """iterable = ["a", "b"]"""

tests = {
    "getitem0": """iterable[0]""",
    "next_iter": """next(iter(iterable))""",
}

results = {}
for test_name, test_stmt in tests.items():
    times = timeit.repeat(
        setup=setup, stmt=test_stmt, repeat=100, number=10000, globals={}
    )
    avg_time = sum(times) / len(times)
    results[test_name] = avg_time

for test_name, result in sorted(results.items(), key=lambda x: x[1]):
    print(f"{test_name:>18}: {result:03g}")
