import os
import timeit

setup = """data = ['/home/user/projects/signac_project', 'abcdef1234567890']
def funcjoin(*paths):
    return os.sep.join(paths)
"""

tests = {
    "join": """os.sep.join(data)""",
    "funcjoin": """funcjoin(*data)""",
    "concat": """data[0] + os.sep + data[1]""",
    "pathjoin": """os.path.join(*data)""",
    "fstring": """f'{data[0]}{os.sep}{data[1]}'""",
    "format": """'{data[0]}{sep}{data[1]}'.format(data=data, sep=os.sep)""",
    "format_positional": """'{1}{0}{2}'.format(os.sep, *data)""",
}

results = {}
for test_name, test_stmt in tests.items():
    times = timeit.repeat(
        setup=setup, stmt=test_stmt, repeat=100, number=100, globals={"os": os}
    )
    avg_time = sum(times) / len(times)
    results[test_name] = avg_time

for test_name, result in sorted(results.items(), key=lambda x: x[1]):
    print(f"{test_name:>18}: {result:03g}")
