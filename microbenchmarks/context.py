# From https://stackoverflow.com/questions/26152934/why-the-staggering-overhead-50x-of-contextlib-and-the-with-statement-in-python
import contextlib
import timeit


def work_pass():
    pass


def work_fail():
    1 / 0


def simple_catch(fn):
    try:
        fn()
    except Exception:
        pass


@contextlib.contextmanager
def catch_context():
    try:
        yield
    except Exception:
        pass


def with_contextlib_contextmanager(fn):
    with catch_context():
        fn()


class ManualContextManager:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True


def with_manual_contextmanager(fn):
    with ManualContextManager():
        fn()


preinstantiated_manual_contextmanager = ManualContextManager()


def with_preinstantiated_manual_contextmanager(fn):
    with preinstantiated_manual_contextmanager:
        fn()


setup = "from __main__ import simple_catch, work_pass, work_fail, with_contextlib_contextmanager, with_manual_contextmanager, with_preinstantiated_manual_contextmanager"
tests = [
    "simple_catch(work_pass)",
    "simple_catch(work_fail)",
    "with_contextlib_contextmanager(work_pass)",
    "with_contextlib_contextmanager(work_fail)",
    "with_manual_contextmanager(work_pass)",
    "with_manual_contextmanager(work_fail)",
    "with_preinstantiated_manual_contextmanager(work_pass)",
    "with_preinstantiated_manual_contextmanager(work_fail)",
]

results = {}
for test_stmt in tests:
    times = timeit.repeat(
        setup=setup, stmt=test_stmt, repeat=100, number=10000, globals={}
    )
    avg_time = sum(times) / len(times)
    results[test_stmt] = avg_time

for test_name, result in sorted(results.items(), key=lambda x: x[1]):
    print(f"{test_name:>18}: {result:03g}")
