import heapq


def siftdown(elems, e, begin, end):  # 向下筛选
    i, j = begin, begin * 2 + 1  # j为i的左子结点
    while j < end:
        if j + 1 < end and elems[j] > elems[j + 1]:  # 如果左子结点大于右子结点
            j += 1  # 则将j指向右子结点
        if e < elems[j]:  # j已经指向两个子结点中较小的位置，
            break  # 如果插入元素e小于j位置的值，则为3者中最小的
        elems[i] = elems[j]  # 能执行到这一步的话，说明j位置元素是三者中最小的，则将其上移到父结点位置
        i, j = j, j * 2 + 1  # 更新i为被上移为父结点的原来的j的位置，更新j为更新后i位置的左子结点
    elems[i] = e  # 如果e已经是某个子树3者中最小的元素，则将其赋给这个子树的父结点
    # 或者位置i已经更新到叶结点位置，则将e赋给这个叶结点。


def heap_sort(elems):
    end = len(elems)
    for i in range(end // 2 - 1, -1, -1):  # 构造堆序。
        siftdown(elems, elems[i], i, end)
    for i in range((end - 1), 0, -1):  # 进行堆排序.i最后一个值为1，不需要到0
        # print(elems)
        e = elems[i]  # 将末尾元素赋给e
        elems[i] = elems[0]  # 交换堆顶与最后一个元素
        siftdown(elems, e, 0, i)
    return (elems)

print(heap_sort([5,6,8,1,2,4,9]))
#
# arr = [2, 3, 5, 1, 54, 23, 132]
# heapq.heapify(arr)
# print(arr)
# print([heapq.heappop(arr) for _ in range(len(arr))])  # 堆排序结果
