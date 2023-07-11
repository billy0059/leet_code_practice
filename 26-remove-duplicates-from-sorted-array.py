'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
'''
from typing import Optional
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        tmp = nums[0]
        i = 1
        while i < len(nums):
            if tmp == nums[i]:
                #print(nums[i])
                del nums[i]
            else:
                tmp = nums[i]
                i += 1
        return len(nums)

def main():
    input=[1,1,2,2,2,3,3,3,4,5,6,6]
    solution = Solution()
    print(solution.removeDuplicates(input))


if __name__ == '__main__':
    main()