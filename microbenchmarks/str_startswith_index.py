import timeit

setup = """s1 = "[0, 1, 2, 3]"
s2 = "0, 1, 2, 3"
"""

tests = {
    "str.startswith hit": """s1.startswith("[")""",
    "str.__getitem__ hit": """s1[0] == "[" """,
    "str.startswith miss": """s2.startswith("[")""",
    "str.__getitem__ miss": """s2[0] == "[" """,
}

results = {}
for test_name, test_stmt in tests.items():
    times = timeit.repeat(
        setup=setup, stmt=test_stmt, repeat=10, number=100000, globals={}
    )
    avg_time = sum(times) / len(times)
    results[test_name] = avg_time

for test_name, result in sorted(results.items(), key=lambda x: x[1]):
    print(f"{test_name:>18}: {result:03g}")
