import os
import timeit
from collections import OrderedDict
from textwrap import dedent

"""LRU cache implemented with OrderedDict vs. dict."""

setup = """\
class LastUpdatedOrderedDict(OrderedDict):
    'Store items in the order the keys were last added'

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.move_to_end(key)

class LastUpdatedDict:
    'Store items in the order the keys were last added'
    def __init__(self):
        self._cache = {}

    def __getitem__(self, key):
        return self._cache[key]

    def __setitem__(self, key, value):
        if key in self._cache:
            self._cache[key] = self._cache.pop(key)
        else:
            self._cache[key] = value
"""

tests = {
    "OrderedDict": """\
        d = LastUpdatedOrderedDict()
        for i in range(100):
            d[i] = i
        for i in range(100):
            d[i]
        for i in range(100):
            d[i] = i
        for i in range(100):
            d[i]
    """,
    "dict": """\
        d = LastUpdatedDict()
        for i in range(100):
            d[i] = i
        for i in range(100):
            d[i]
        for i in range(100):
            d[i] = i
        for i in range(100):
            d[i]
    """,
}

results = {}
for test_name, test_stmt in tests.items():
    times = timeit.repeat(
        setup=dedent(setup).rstrip(),
        stmt=dedent(test_stmt).rstrip(),
        repeat=100,
        number=100,
        globals={"OrderedDict": OrderedDict},
    )
    avg_time = sum(times) / len(times)
    results[test_name] = avg_time

for test_name, result in sorted(results.items(), key=lambda x: x[1]):
    print(f"{test_name:>18}: {result:03g}")
