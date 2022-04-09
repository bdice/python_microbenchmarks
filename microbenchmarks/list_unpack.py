import os
import timeit
from textwrap import dedent

"""Constructing a list."""

setup = """\
    data = tuple(range(1000))
"""

tests = {
    "list_construct": """\
        list(data)
    """,
    "list_unpack": """\
        [*data]
    """,
}

results = {}
for test_name, test_stmt in tests.items():
    times = timeit.repeat(
        setup=dedent(setup).rstrip(),
        stmt=dedent(test_stmt).rstrip(),
        repeat=1000,
        number=1000,
        globals={},
    )
    avg_time = sum(times) / len(times)
    results[test_name] = avg_time

for test_name, result in sorted(results.items(), key=lambda x: x[1]):
    print(f"{test_name:>18}: {result:03g}")
