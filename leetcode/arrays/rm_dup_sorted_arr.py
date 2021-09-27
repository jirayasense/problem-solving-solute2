from typing import List


def removeDuplicates(nums: List[int]) -> int:
    l = len(nums)
    if l < 1:
        return
    start = 0
    lead = 1

    while lead < l-1:
        while nums[start] == nums[lead]:
            if lead == l:
                break
            lead += 1
        else:
            start += 1
            lead += 1
            nums[start], nums[lead] = nums[lead], nums[start]
            continue

    return start+1


if __name__ == '__main__':
    pass
