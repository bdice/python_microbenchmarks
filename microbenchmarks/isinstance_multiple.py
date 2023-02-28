import os
import timeit
from textwrap import dedent

"""Multiple isinstance checks."""

setup = """\
    class A():
        pass

    data = "asdf"
"""

tests = {
    "separate_early": """\
        isinstance(data, str) or isinstance(data, float) or isinstance(data, A)
    """,
    "separate_late": """\
        isinstance(data, float) or isinstance(data, A) or isinstance(data, str)
    """,
    "together_early": """\
        isinstance(data, (str, float, A))
    """,
    "together_late": """\
        isinstance(data, (float, A, str))
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
