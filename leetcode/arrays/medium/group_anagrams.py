#! https://leetcode.com/problems/group-anagrams/


from collections import defaultdict
from typing import DefaultDict, List
from itertools import groupby
from operator import itemgetter


# def get_anagram_id(s):
#     return sum(map(ord, s))


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    strs_with_ids = zip(map(sorted, strs), strs)
    return [[t[1] for t in g[1]] for g in groupby(sorted(strs_with_ids, key=itemgetter(0)), key=itemgetter(0))]


def groupAnagrams2(strs: List[str]) -> List[List[str]]:
    # Better Soln
    d = defaultdict(list)
    for s in strs:
        d[''.join(sorted(s))].append(s)
    return d.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

strs = ["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"]

ans = groupAnagrams2(strs)


print(*ans)
