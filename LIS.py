import bisect


def lengthOfLIS(nums):
    d = []

    # strict
    for n in nums:
        if not d or n > d[-1]:
            d.append(n)
        else:
            loc = bisect.bisect_left(d, n)
            d[loc] = n

    # # non strict
    # for n in nums:
    #     if not d or n >= d[-1]:
    #         d.append(n)
    #     else:
    #         loc = bisect.bisect_right(d, n)
    #         d[loc] = n

    return len(d)

if __name__ == '__main__':
    print(lengthOfLIS([7,1,1,2,2,3,9,4]))