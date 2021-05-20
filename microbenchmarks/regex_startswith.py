import hashlib
import timeit

m = hashlib.sha256()
m.update(b"some string")
md5 = m.hexdigest()
print("MD5:", md5)

setup = """import re
pattern = re.compile("^61d.*")
"""

tests = {
    "str.startswith": """md5.startswith("61d")""",
    "pattern.fullmatch": """pattern.fullmatch(md5)""",
    "pattern.match": """pattern.match(md5)""",
    "pattern.search": """pattern.search(md5)""",
    "re.fullmatch": """re.fullmatch(pattern, md5)""",
    "re.match": """re.match(pattern, md5)""",
    "re.search": """re.search(pattern, md5)""",
}

results = {}
for test_name, test_stmt in tests.items():
    times = timeit.repeat(
        setup=setup, stmt=test_stmt, repeat=10, number=100000, globals={"md5": md5}
    )
    avg_time = sum(times) / len(times)
    results[test_name] = avg_time

for test_name, result in sorted(results.items(), key=lambda x: x[1]):
    print(f"{test_name:>18}: {result:03g}")
