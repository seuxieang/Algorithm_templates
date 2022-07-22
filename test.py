import inspect
import re
from collections import Counter, defaultdict
from typing import List

from tqdm import tqdm

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        c = Counter(nums)
        res = 0
        ind = 0
        now = {}
        for k in c:
            now[k] = 1
        c = list(c.items())
        c.sort()
        d = defaultdict(bool)
        for i in range(2,c[-1][0]+1):
            for j in range(2,i):
                if (not i%j) and (not  defaultdict[i]):
                    continue
                d[i] = True
            for k in range(len(numsDivide)):
                if numsDivide[k]%i:
                    break
            if c[ind][0] == i and k==len(numsDivide)-1:
                return res
            elif c[ind][0] <= i:
                res += c[ind][1]
                ind += 1
        return -1



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
