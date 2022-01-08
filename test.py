# def quick_sort(s, start, end):
#     l = start
#     r = end
#     pivot = s[l]
#     while l < r:
#         while s[r] >= pivot and l < r:
#             r -= 1
#
#         s[l] = s[r]
#         while s[l] < pivot and l < r:
#             l += 1
#
#         s[r] = s[l]
#         s[l] = pivot
#         quick_sort(s, start, l - 1)
#         quick_sort(s, l + 1, end)
#     return

# 最好不要这样写，这样选取左边pivot容易越界
# def quick_sort(s, start, end):
#     l = start
#     r = end
#     pivot = s[r]
#     while l < r:
#         while l<r and s[l] < pivot:
#             l+=1
#         s[r] = s[l]
#         while l < r and s[r] >= pivot:
#             r -= 1
#         s[l] = s[r]
#         s[l] = pivot
#         quick_sort(s, start, l - 1)
#         quick_sort(s, l + 1, end)
#     return

# 标准写法
import bisect
import heapq
from collections import deque
import numpy


def partition(n, s, e):
    i = s - 1
    pivot = n[e]
    for j in range(s, e):
        if n[j] <= pivot:
            i += 1
            n[i], n[j] = n[j], n[i]
    n[i + 1], n[e] = n[e], n[i + 1]
    return i + 1


def quick_sort(n, s, e):
    if s < e:
        pi = partition(n, s, e)
        quick_sort(n, s, pi - 1)
        quick_sort(n, pi + 1, e)


if __name__ == '__main__':
    
    # a = [[999,[999,999]],[777,[777,1]],[888,[888,888]],[999,[999,999]],[9,[999,999]]]
    # heapq.heapify(a,key=lambda x:(x[0],x[1][0]))
    # while a:
    #     print(heapq.heappop(a))
    # a = [4, 2, 4, 1, 5, 6, 3, 4, 3, 122]
    #
    # b = [5,4,4]
    # quick_sort(b, 0, b.__len__() - 1)
    # print(b)
    # print(quick_sort(a,0,a.__len__()-1))

    # 测试用时
    import datetime


    def fastPower(num, power,mod):
        res = 1
        while power:
            if power & 1:
                res = (res * num) % mod
            res = (res ** 2) % mod
            power >>= 1
        return res
    starttime = datetime.datetime.now()
    a = 1
    b = 0
    time = 5
    mod = 10 ** 9 + 7
    for i in range(2 ** time):
        a = [4, 2, 4, 1, 5, 6, 3, 4, 3, 122]
        # quick_sort(a,0,a.__len__()-1)
        # b = a.
        # a.reverse()
        # b = a
        # 0:00:02.650512

        # a = 3
        # b = 2
        # c = max(a,b)
        # for c in a:
        #     b = c + 1
        c = (((2**32))**((2**20)))%mod
    endtime = datetime.datetime.now()
    print('1:',endtime - starttime)

    starttime = datetime.datetime.now()
    d = True
    e = False
    for i in range(2 ** time):
        a = [4, 2, 4, 1, 5, 6, 3, 4, 3, 122]
        # b = len(a)
        # b = a[::-1]
        # sorted(a,key=lambda x:x)
        # 2.597392

        # a = 3
        # b = 2
        # c = a if a>b else b
        # l = len(a)
        # for i in range(l):
        #     b = a[i] + 1
        c = fastPower((2**32),(2**20),mod)
    endtime = datetime.datetime.now()
    print('2:',endtime - starttime)



    # def foo():
    #     print("starting...")
    #     for _ in range(10):
    #         res = yield 4
    #         print("res:",res)
    # g = foo()
    # print(next(g))
    # a = numpy.fromiter(g,dtype=int)
    # print('ok')
    # import collections

# import bisect
#
# L = [1, 3, 3, 6, 6, 6, 8, 12, 15, 6,6,6,6,6,6,6,6,6,6,6,6,6,]
# x = 6
# x_insert_point = bisect.bisect_left(L, x)  # 在L中查找x，x存在时返回x左侧的位置，x不存在返回应该插入的位置..这是3存在于列表中，返回左侧位置１
# print(x_insert_point)
#
# x_insert_point = bisect.bisect_right(L, x)
#
# print(x_insert_point)
# bisect.insort(L,5)
# print(L)

# from itertools import groupby
# li = ['a','b','c','.','aa','bb','cc','.','aaa','bbb','ccc']
# [list(g) for k,g in groupby(li,lambda x:x=='.') if not k]

# deq = deque([3,3])
# deq.popleft()
# deq.popleft()
# deq.popleft()

# from collections import OrderedDict
#
# a = OrderedDict({1:2,3:4,5:6})
# a.setdefault(0,0)
# b = a.popitem(last = False)
# print(a[0])
# print('ok')

# def a():
#     a = []
#     print(a)
#     print('a')
#     def b():
#         a.append(1)
#         # 这个地方只能用append才会调用a
#         # 如果用a = xx是新命名一个局部变量
#         print('b')
#     b()
#     print(a)
#     print('a')
# a()

# # 升序采用大顶堆，降序采用小顶堆
# from heapq import *

# a = [[1,1,3],[1,1,2]]
# for x,y,v in a:
#     print(x,y,v)

# 切割字符串，万一用得到
# s1 = [[k] + list(x) for k, x in groupby(list(s1), key=lambda x: x.isdigit())]
# s2 = [[k] + list(x) for k, x in groupby(list(s2), key=lambda x: x.isdigit())]
# b = {1,2,3}
# a = [[9,{8:2}],[7,{7:7}],[1, {7:7}],[9, {7:7}],[9, {7:7}]]
# # heapq.heapify(a)
# # while a:
# #     print(heapq.heappop(a))
# # a.sort()
# # bisect.insort_left(a,[9,9])
# # print(a)
# a.sort(key = lambda x:x[0])
# print(a)
# bisect.insort(a,[4,{1:3}])
# print(a)
# from sortedcontainers import SortedList
# sl = SortedList(['e', 'a', 'c', 'd', 'b'])
# print(sl)
# # sl.add(123)
# print(sl.bisect('c'))
# sl *= 10_000_000
# print(sl.count('c'))

# # sl[-3:]
# # ['e', 'e', 'e']
# from sortedcontainers import SortedDict
# sd = SortedDict({'c': 3, 'a': 1, 'b': 2})
# # print(sd['f'])
# # a=sd["f"] = 1
# # print(a)
# # print(sd.get('f'))
# print(sd.peekitem(-1))
# # sd
# # SortedDict({'a': 1, 'b': 2, 'c': 3})
# # sd.popitem(index=-1)
# # ('c', 3)
# # from sortedcontainers import SortedSet
# # ss = SortedSet('abracadabra')
# # ss
# # SortedSet(['a', 'b', 'c', 'd', 'r'])
# # ss.bisect_left('c')
