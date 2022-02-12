import os
import timeit
from textwrap import dedent

"""Counting an iterator by consuming it."""

setup = """\
    data = {"a": {"b": {"c": 0}}}
    keys = "a.b.c".split(".")
"""

tests = {
    "one_direct_access": """\
        v = data[keys[0]]
        for n in keys[1:]:
            v = v[n]
    """,
    "recurse_all": """\
        v = data
        for n in keys:
            v = v[n]
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
