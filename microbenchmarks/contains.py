import os
import timeit

setup = """data_list = ['left', 'right', 'up', 'down']
data_tuple = ('left', 'right', 'up', 'down')
data_set = {'left', 'right', 'up', 'down'}
"""

tests = {
    "front_list": """'left' in data_list""",
    "front_tuple": """'left' in data_tuple""",
    "front_set": """'left' in data_set""",
    "back_list": """'down' in data_list""",
    "back_tuple": """'down' in data_tuple""",
    "back_set": """'down' in data_set""",
}

results = {}
for test_name, test_stmt in tests.items():
    times = timeit.repeat(
        setup=setup, stmt=test_stmt, repeat=100, number=100000, globals={}
    )
    avg_time = sum(times) / len(times)
    results[test_name] = avg_time

for test_name, result in sorted(results.items(), key=lambda x: x[1]):
    print(f"{test_name:>18}: {result:03g}")
