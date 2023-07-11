# https://leetcode.com/problems/maximum-subarray/description/
# Use a dynamic programming approach
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Create an array dp[], 
        # dp[i] represents the max value of "the sum of a contiguous subarray the ends with index i"
        # e.g., input array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        #                dp = [-2, 1, -2, 4,  3, 5, 6,  1, 5]
        
        maxSum = nums[0]
        currentSum = nums[0]
        
        for i in range(1, len(nums)):
            currentSum = max(nums[i], nums[i] + currentSum) # (index itself) or (previous max result + itself)
            if currentSum > maxSum:
                maxSum = currentSum
        return maxSum