import bisect
import heapq
import inspect
import re
from collections import Counter, defaultdict, deque
from functools import cmp_to_key, lru_cache
from typing import List
from itertools import accumulate, combinations, permutations, product, combinations_with_replacement
from sortedcontainers import SortedDict

import string

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n =













if __name__ == '__main__':
    s = Solution()
    for _, attr in inspect.getmembers(s):
        if inspect.ismethod(attr):
            argcount = attr.__code__.co_argcount -1
            with open('input.txt', 'r') as f:
                while True:
                    args = []
                    for i in range(argcount):
                        v = f.readline()
                        if not v:
                            exit(0)
                        args.append(eval(v))
                    print(attr(*args))

