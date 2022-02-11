import re
import string
from collections import Counter

pat = '(?=[A-Z])'
s = 'camelCaseString'
ans = re.split(pat, s)
print(ans)

def f(s):
    pat = '(?<=.)(?=[A-Z])'
    ans = re.split(pat, s)
    print(ans)
    t = ''.maketrans(string.ascii_uppercase, string.ascii_lowercase)
    res = '_'.join(ans)
    return res.translate(t)

def to_snake_case(s):
    pat = '(?<!^)(?=[A-Z])'
    ans = re.sub(pat, s, '_')
    return ans.lower()

a = f('HackerEarth')
print(a)


# Find number fathest from 0 (if tie then take smaller val)
def f2(A):
    ''' O(n) '''
    pos = []
    neg = []
    for n in A:  # O(n)
        if n > 0:
            pos.append(n)
        else:
            neg.append(n)

    def find_ans(cntr, rev=True):
        for k in (sorted(cntr.keys(), reverse=rev)):
            if cntr[k] == 1:
                return k 
        return 0
    
    pos_cnts = Counter(pos)       # O(n)
    pos_max = find_ans(pos_cnts)  # O(n)

    neg_cnts = Counter(neg)
    neg_max = find_ans(neg_cnts, False)

    return pos_max if pos_max + neg_max > 0 else neg_max

a = f2([1,2,3,4,5])
print(a)