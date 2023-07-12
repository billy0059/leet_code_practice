class Solution:
    def rob(self, nums: List[int]) -> int:
        # Dynamic programming
        # Create an array rob[], where rob[i] represents the most amount of money we can
        # steal with "i" in the end of the stolen list (does mean that we have to steal it)
        # rob[i] = max(rob[i-2] + nums[i], rob[i-1]) -- This is the dp formula
        # e.g.,
        # nums = [2, 7, 9, 3, 1]
        # rob  = [2, 7,11,11,12]
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        rob = [0] * len(nums)
        rob[0] = nums[0]
        rob[1] = max(rob[0], nums[1])
        ret_max_amount = max(rob[0], rob[1])

        for i in range(2, len(nums)):
            rob[i] = max(rob[i-2] + nums[i], rob[i-1])
            ret_max_amount = rob[i] if rob[i] > ret_max_amount else ret_max_amount

        return ret_max_amount