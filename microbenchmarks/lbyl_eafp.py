import timeit

hit = """data = {'foo': 0, 'bar': 0}"""
miss = """data = {'baz': 0, 'bar': 0}"""

lbyl = """if 'foo' in data:
  data['foo'] += 1
else:
  data['bar'] += 1
"""

eafp = """try:
  data['foo'] += 1
except KeyError:
  data['bar'] += 1
"""

hit_lbyl_time = timeit.timeit(setup=hit, stmt=lbyl, number=1000000)
hit_eafp_time = timeit.timeit(setup=hit, stmt=eafp, number=1000000)
miss_lbyl_time = timeit.timeit(setup=miss, stmt=lbyl, number=1000000)
miss_eafp_time = timeit.timeit(setup=miss, stmt=eafp, number=1000000)

print("Hit, LBYL:", hit_lbyl_time)
print("Hit, EAFP:", hit_eafp_time)
print("Miss, LBYL:", miss_lbyl_time)
print("Miss, EAFP:", miss_eafp_time)
