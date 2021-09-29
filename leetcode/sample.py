from collections import defaultdict
import itertools as it

# Sorted
l = [(1, 0), (1, 2), (2, 0), (2, 3)]

d_l2 = defaultdict(int)

for e in l:
    d_l2[e[0]] = max(d_l2[e[0]], e[1])

print(d_l2)


