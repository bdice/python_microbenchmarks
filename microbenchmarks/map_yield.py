import timeit

data = """data = list(range(100000))"""

for_yield = """def values(data):
  for x in data:
    yield (x,)

for x in values(data):
  pass
"""

yield_from_map = """def values(data):
  yield from map(lambda x: (x,), data)

for x in values(data):
  pass
"""

time1 = timeit.timeit(setup=data, stmt=for_yield, number=1000)
time2 = timeit.timeit(setup=data, stmt=yield_from_map, number=1000)

print("for: yield:", time1)
print("yield from map:", time2)
