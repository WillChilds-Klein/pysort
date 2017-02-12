import sys
import time
from random import randint
from math import floor
from collections import Counter


def main():
    nums = sys.argv[1:]
    infile = None
    if nums[0] == '-f':
        infile = nums[1]
        with open(infile) as f:
            nums = f.readlines()
    try:
        nums = [int(num.rstrip()) for num in nums]
    except:
        raise Exception('Please specify a list of integers!')
    qs_millis, qs_sorted = time_sort(qs, nums)
    ms_millis, ms_sorted = time_sort(ms, nums)
    ns_millis, ns_sorted = time_sort(ns, nums)
    bs_millis, bs_sorted = time_sort(bs, nums)
    print 'QSRT: {} ms \t {}'.format(qs_millis, qs_sorted if not infile else '')
    print 'MSRT: {} ms \t {}'.format(ms_millis, ms_sorted if not infile else '')
    print 'NSRT: {} ms \t {}'.format(ns_millis, ns_sorted if not infile else '')
    print 'BSRT: {} ms \t {}'.format(bs_millis, bs_sorted if not infile else '')


def time_sort(func, nums):
    start = time.time() * 1000
    sorted_nums = func(list(nums))    # sort copy of list to not overwrite nums
    end = time.time() * 1000
    return (end - start), validate(nums, sorted_nums)


def validate(nums, sorted_nums):
    if len(nums) != len(sorted_nums):
        raise Exception('sorted list not same length as original!')
    if Counter(nums) != Counter(sorted_nums):
        raise Exception('sorted list and original do not contain same elements!')

    prev = sorted_nums.pop(0)
    for item in sorted_nums:
        if prev > item:
            raise Exception('sorted list out of order!')
    return sorted_nums


def qs(nums):
    if nums == []: return []
    return qs([num for num in nums[1:] if num < nums[0]]) + nums[:1] + \
           qs([num for num in nums[1:] if num >= nums[0]])


def ms(nums):
    if len(nums) == 1 or nums == []: return nums
    p = int(floor(len(nums) / 2))
    return merge(ms(nums[:p]), ms(nums[p:]))


def merge(left, right):
    nums = []
    while left or right:
        if left and right:
            nums.append(left.pop(0) if left[0] < right[0] else right.pop(0))
        elif left:
            nums.append(left.pop(0))
        elif right:
            nums.append(right.pop(0))
    return nums


def bs(nums):
    while True:
        swapped = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                swapped = True
        if not swapped:
            return nums


def ns(nums):
    while True:
        swapped = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                nums = insert(nums[i], nums)
                swapped = True
        if not swapped:
            return nums


def insert(val, nums):
    return [num for num in nums if num <= val] + \
           [num for num in nums if num > val]


if __name__ == '__main__':
    main()
