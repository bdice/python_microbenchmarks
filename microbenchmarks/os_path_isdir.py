import os
import timeit

setup = """path =  '/home'"""

tests = {
    "exists": """os.path.exists(path)""",
    "isdir": """os.path.isdir(path)""",
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
