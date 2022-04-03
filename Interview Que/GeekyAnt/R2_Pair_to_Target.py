'''
Que :- Array Provided, Find Pair of Index that Sum up to target vals 
       Given that :- 
         - only 1 such pair exists in array
         - no duplicates in array
         - array is not sorted
'''

import itertools as it

a = [2, 11, 15, 7]  # inp arr
t = 18  # target

# S1 sort the arr (O(nlogn))
#a.sort()

# S2. Discard candidates  ( O(n))
#na = set(it.takewhile(lambda x: x <= t, a))
na = {e for e in a if e <= t}

# S3. 
e1, e2 = -1, -1
for e in na:
    r = t-e
    if r in na:
        e1, e2 = e, r
        
i1, i2 = a.index(e1), a.index(e2)

print(i1, i2)