import hashlib
import os
import timeit

setup = """data = str(os.urandom(10000))"""

tests = {
    "encode": """m = hashlib.md5()
m.update(data.encode("utf-8"))
m.hexdigest()
""",
    "bytes": """m = hashlib.md5()
m.update(bytes(data, "utf-8"))
m.hexdigest()
""",
}

for test_name, test_stmt in tests.items():
    times = timeit.repeat(
        setup=setup, stmt=test_stmt, repeat=100, number=100, globals={"os": os, "hashlib": hashlib}
    )
    print(test_name + ":", sum(times) / len(times))
