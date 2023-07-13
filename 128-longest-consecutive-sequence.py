class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Idea: Crease a set for reference:
        # 1. If the number could be the start number (num-1 is not in the set)
        # 2. If the start number has next consecutive number, if yes, ret_longest_len++
        # Because the time complexity of operations on set() is O(1), we could make this
        # solution in O(n)
        nums_set = set(nums) # Create a set for later reference
        ret_longest_len = 0
        for num in nums:
            if (num-1) not in nums_set: # If the number could be the first one in a consecutive number
                tmp_longest_len = 0
                consecutive = num
                while consecutive in nums_set: # If the next consecutive number is in the set, go on for it!
                    tmp_longest_len += 1
                    consecutive += 1
                    ret_longest_len = max(ret_longest_len, tmp_longest_len)
        return ret_longest_len