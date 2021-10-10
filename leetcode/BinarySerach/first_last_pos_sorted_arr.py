# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


from typing import List

'''
Idea -> just don't stop in Binary Search, once index is found. Be Greedy 😉
'''

def searchRange(nums: List[int], target: int) -> List[int]:
    def bs(arr, target, leftMost=True):
        '''
          s = first-most <= target
          e = last-most >= target
        '''
        s, e = 0, len(arr) - 1
        ans = -1
        while s <= e:
            mid = s + ((e - s) // 2)
            if target > arr[mid]:
                s = mid + 1
            elif target < arr[mid]:
                e = mid - 1
            else:
                ans = mid   # Don't stop here, Just Search More ...
                if leftMost:
                    e = mid - 1
                else:
                    s = mid + 1
        return ans

    left = bs(nums, target, leftMost=True)
    right = bs(nums, target, leftMost=False) if left != -1 else -1
    return [left, right]


nums = [5, 7, 7, 8, 8, 10]
target = 8

nums = [5,7,7,8,8,10]
target = 6

nums = []
target = 0

ans = searchRange(nums, target)
print(ans) 
