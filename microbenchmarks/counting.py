import os
import timeit

"""Counting an iterator by consuming it."""

setup = """iterable = range(1_000)"""

tests = {
    "enumerate": """i = 0
for i, _ in enumerate(iterable, 1):
    pass""",
    "sum": """sum(1 for _ in iterable)""",
    "direct_count": """i = 0
for _ in iterable:
    i += 1"""
}

results = {}
for test_name, test_stmt in tests.items():
    times = timeit.repeat(
        setup=setup, stmt=test_stmt, repeat=100, number=100, globals={}
    )
    avg_time = sum(times) / len(times)
    results[test_name] = avg_time

for test_name, result in sorted(results.items(), key=lambda x: x[1]):
    print(f"{test_name:>18}: {result:03g}")
