import os
import timeit

setup = """def funcjoin(*paths):
    return os.sep.join(paths)
"""

tests = {
    "join": """os.sep.join((os.path.expanduser("~"), "abcdef1234567890"))""",
    "funcjoin": """funcjoin(os.path.expanduser("~"), "abcdef1234567890")""",
    "concat": """os.path.expanduser("~") + os.sep + 'abcdef1234567890'""",
    "pathjoin": """os.path.join(os.path.expanduser("~"), "abcdef1234567890")""",
    "expanduser": """os.path.expanduser(os.path.join("~", "abcdef1234567890"))""",
}

results = {}
for test_name, test_stmt in tests.items():
    times = timeit.repeat(
        setup=setup, stmt=test_stmt, repeat=100, number=1000, globals={"os": os}
    )
    avg_time = sum(times) / len(times)
    results[test_name] = avg_time

for test_name, result in sorted(results.items(), key=lambda x: x[1]):
    print(f"{test_name:>18}: {result:03g}")
