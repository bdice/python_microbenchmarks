import time
import timeit

setups = {
    "property": """
class MyClass:
    @property
    def __protocol__(self):
        time.sleep(0.00001)
        return True

obj = MyClass()""",
    "method": """
class MyClass:
    def __protocol__(self):
        time.sleep(0.00001)
        return True

obj = MyClass()""",
    "none": """
class MyClass:
    pass

obj = MyClass()""",
}

tests = {
    "eafp": """
try:
    obj.__protocol__
except AttributeError:
    pass
    """,
    "lbyl": """hasattr(obj, "__protocol__")""",
    "gentle-lbyl": (
        """"__protocol__" in obj.__dir__() or hasattr(obj, "__protocol__")"""
    ),
}

results = {}
for setup_name, setup_stmt in setups.items():
    for test_name, test_stmt in tests.items():
        test_name = f"{setup_name}, {test_name}"
        times = timeit.repeat(
            setup=setup_stmt,
            stmt=test_stmt,
            repeat=10,
            number=1000,
            globals={"time": time},
        )
        avg_time = sum(times) / len(times)
        results[test_name] = avg_time

for test_name, result in sorted(results.items(), key=lambda x: x[1]):
    print(f"{test_name:>18}: {result:03g}")
