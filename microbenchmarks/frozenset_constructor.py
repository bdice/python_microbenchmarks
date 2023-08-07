import hashlib
import os
import timeit

setup = ""

tests = {
    "from_list": """frozenset(
    [
        # These are all protected keys that are inherited from data type classes.
        "_data",
        "_name",
        "_suspend_sync_",
        "_load",
        "_sync",
        "_root",
        "_validators",
        "_all_validators",
        "_load_and_save",
        "_suspend_sync",
        "_supports_threading",
        "_LoadSaveType",
        "registry",
        # These keys are specific to the JSON backend.
        "_filename",
        "_write_concern",
    ]
)
""",
    "from_tuple": """frozenset(
    (
        # These are all protected keys that are inherited from data type classes.
        "_data",
        "_name",
        "_suspend_sync_",
        "_load",
        "_sync",
        "_root",
        "_validators",
        "_all_validators",
        "_load_and_save",
        "_suspend_sync",
        "_supports_threading",
        "_LoadSaveType",
        "registry",
        # These keys are specific to the JSON backend.
        "_filename",
        "_write_concern",
    )
)
""",
    "from_set": """frozenset(
    {
        # These are all protected keys that are inherited from data type classes.
        "_data",
        "_name",
        "_suspend_sync_",
        "_load",
        "_sync",
        "_root",
        "_validators",
        "_all_validators",
        "_load_and_save",
        "_suspend_sync",
        "_supports_threading",
        "_LoadSaveType",
        "registry",
        # These keys are specific to the JSON backend.
        "_filename",
        "_write_concern",
    }
)
""",
}

for test_name, test_stmt in tests.items():
    times = timeit.repeat(
        setup=setup,
        stmt=test_stmt,
        repeat=100,
        number=10000,
        globals={"os": os, "hashlib": hashlib},
    )
    print(test_name + ":", sum(times) / len(times))
