import bisect


def binarysearch(alist, item, left_most):
    """
    注意返回的是该元素的右下标（与bisect不一样）(left一样,right不一样)
    :param alist: 排好序的列表
    :param item:  查找元素
    :return: 排好序列表序号靠前的元素
    """
    if len(alist) == 0:
        return -1
    left, right = 0, len(alist) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if alist[mid] == item:
            if left_most:
                # bisect_left
                right = mid
            else:
                #bisect_right
                left = mid
        elif alist[mid] < item:
            left = mid
        elif alist[mid] > item:
            right = mid
    if left_most:
        if alist[left] == item:
            return left
        if alist[right] == item:
            return right
    else:
        if alist[right] == item:
            return right
        if alist[left] == item:
            return left
    return -1


def bSearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1
    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid
    # Post-processing:
    # End Condition: left + 1 == right
    if nums[left] == target: return left
    if nums[right] == target: return right
    return -1

if __name__ == '__main__':
    a = [1, 2, 2, 2, 2, 2, 4, 5, 6, 7, 8, 9, 10, 12]
    # a = [2,2]
    find = 1
    b = binarysearch(a, find, True)
    print(b)

    b = binarysearch(a, find, False)
    print(b)

    print(bisect.bisect_left(a, find),a[bisect.bisect_left(a, find)])
    print(bisect.bisect_right(a,find),a[bisect.bisect_right(a, find)])