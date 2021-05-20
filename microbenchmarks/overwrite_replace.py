import os
import timeit

setup = """data = str(os.urandom(10000))
with open('tmpfile', 'w') as f:
  f.write(data)
"""

tests = {
    "Overwrite": """with open('tmpfile', 'w') as f:
  f.write(data)
""",
    "os.write": """f = os.open('tmpfile', os.O_WRONLY)
os.write(f, data.encode('utf-8'))
os.close(f)
""",
    "Replace": """with open('tmpfile~', 'w') as f:
  f.write(data)
os.replace('tmpfile~', 'tmpfile')
""",
}

for test_name, test_stmt in tests.items():
    times = timeit.repeat(
        setup=setup, stmt=test_stmt, repeat=10, number=100, globals={"os": os}
    )
    print(test_name + ":", sum(times) / len(times))
