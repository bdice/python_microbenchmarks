import os
import timeit
from textwrap import dedent

"""Splitting keys for nested dict access."""

setup = """\
    data = {"a": {"b": {"c": 0}}}
    dotted_key = "a.b.c"
"""

tests = {
    "one_direct_access": """\
        keys = dotted_key.split(".")
        v = data[keys[0]]
        for n in keys[1:]:
            v = v[n]
    """,
    "recurse_all": """\
        keys = dotted_key.split(".")
        v = data
        for n in keys:
            v = v[n]
    """,
    "dotted_get": """\
        def dotted_get(mapping, key):
            "Fetch a value from a nested mapping using a dotted key."
            if mapping is None:
                return None
            tokens = key.split(".")
            if len(tokens) > 1:
                return dotted_get(mapping.get(tokens[0]), ".".join(tokens[1:]))
            return mapping.get(key)
        dotted_get(data, dotted_key)
    """,
    "dotted_get2": """\
        def dotted_get(mapping, key):
            "Fetch a value from a nested mapping using a dotted key."
            tokens = key.split(".")
            v = mapping
            for token in tokens:
                if v is None:
                    return None
                v = v.get(token)
            return v
        dotted_get(data, dotted_key)
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
