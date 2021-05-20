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


def with_catch(fn):
    with catch_context():
        fn()


class ManualCatchContext(object):
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True


def manual_with_catch(fn):
    with ManualCatchContext():
        fn()


preinstantiated_manual_catch_context = ManualCatchContext()


def manual_with_catch_cache(fn):
    with preinstantiated_manual_catch_context:
        fn()


setup = "from __main__ import simple_catch, work_pass, work_fail, with_catch, manual_with_catch, manual_with_catch_cache"
commands = [
    "simple_catch(work_pass)",
    "simple_catch(work_fail)",
    "with_catch(work_pass)",
    "with_catch(work_fail)",
    "manual_with_catch(work_pass)",
    "manual_with_catch(work_fail)",
    "manual_with_catch_cache(work_pass)",
    "manual_with_catch_cache(work_fail)",
]
for c in commands:
    print(c, ": ", timeit.timeit(c, setup))
