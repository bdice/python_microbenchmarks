import os
import timeit
from textwrap import dedent
import numpy as np

"""Compute edges from a faces (vertex indices)."""

setup = """\
    # Dodecahedron faces:
    # shp = coxeter.families.PlatonicFamily().get_shape("Dodecahedron")
    # faces = [f.tolist() for f in shp.faces()]
    faces = [[13, 0, 8], [0, 13, 15], [11, 10, 1], [6, 2, 10], [6, 13, 2], [13, 6, 15], [18, 4, 10, 2], [1, 10, 4], [15, 14, 0], [5, 11, 1], [4, 12, 1], [16, 12, 4], [1, 12, 5], [7, 14, 15], [4, 18, 16], [18, 8, 16], [8, 18, 2, 13], [17, 19, 5], [5, 12, 17], [11, 3, 7], [11, 5, 19, 3], [19, 9, 14, 3], [3, 14, 7], [0, 9, 8], [14, 9, 0], [9, 19, 17], [10, 11, 7, 15, 6], [8, 9, 17, 12, 16]]
"""

tests = {
    "option1": """\
        edges = []
        [
            edges.append((i, j))
            for face in faces
            for i, j in zip(face, np.roll(face, -1))
            if (j, i) not in edges
        ]
    """,
    "option2": """\
        double_edges = [
            (i, j) for face in faces for i, j in zip(face, np.roll(face, -1))
        ]
        edges = []
        [
            edges.append((i, j)) or (i, j)
            for (i, j) in double_edges
            if (j, i) not in edges
        ]
    """,
    "option3": """\
        # "Roll your own" definition of roll to avoid array copies in np.roll.
        # This gives a significant performance boost.
        def roll1(it):
            yield from it[1:]
            yield it[0]

        # This avoids allocating an unused result for the list comprehension
        # which is a small but measurable difference.
        edges = []
        for face in faces:
            for i, j in zip(face, roll1(face)):
                if (j, i) not in edges:
                    edges.append((i, j))
    """,
}

results = {}
for test_name, test_stmt in tests.items():
    times = timeit.repeat(
        setup=dedent(setup).rstrip(),
        stmt=dedent(test_stmt).rstrip(),
        repeat=100,
        number=10,
        globals={"np": np},
    )
    avg_time = sum(times) / len(times)
    results[test_name] = avg_time

for test_name, result in sorted(results.items(), key=lambda x: x[1]):
    print(f"{test_name:>18}: {result:03g}")
