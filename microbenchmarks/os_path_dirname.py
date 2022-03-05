import os
import timeit

setup = """path =  '/home/user/mydir'"""

tests = {
    "dirname": """os.path.dirname(path)""",
    "join": """os.path.join(path, "..")""",
    "abs-dirname": """os.path.abspath(os.path.dirname(path))""",
    "abs-join": """os.path.abspath(os.path.join(path, ".."))""",
}

results = {}
for test_name, test_stmt in tests.items():
    times = timeit.repeat(
        setup=setup, stmt=test_stmt, repeat=10, number=100000, globals={"os": os}
    )
    avg_time = sum(times) / len(times)
    results[test_name] = avg_time

for test_name, result in sorted(results.items(), key=lambda x: x[1]):
    print(f"{test_name:>18}: {result:03g}")
