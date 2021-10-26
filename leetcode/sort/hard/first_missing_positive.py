# https://leetcode.com/problems/first-missing-positive/

from typing import List


def cyclic_sort_m(arr):
    '''for given +ve integer element Make element move to its correct position '''
    i, l = 0, len(arr)
    while i < l:
        correct_idx = arr[i] - 1  # correct idx of current element
        if (0 <= correct_idx < l) and (arr[correct_idx] != arr[i]): 
            # move element to its correct index
            arr[i], arr[correct_idx] = arr[correct_idx], arr[i]  # Swap
        else: # i.e correct idx of +ve int already holds correct element
            i += 1

def firstMissingPositive(nums: List[int]) -> int:
    cyclic_sort_m(nums)
    l = len(nums)
    for i in range(l):
        if nums[i] != i+1:  # property i.e arr[i] = i+1, after cyclic sort
            return i+1
    return l+1  # all integer element are at proper location so next int will be smallest one to be missing
 
nums = [1,2,0]
nums = [3,4,-1,1]
nums = [7,8,9,11,12]
print(firstMissingPositive(nums))