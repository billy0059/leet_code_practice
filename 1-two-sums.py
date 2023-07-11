# https://leetcode.com/problems/two-sum/description/
# Solution is in a "hashmap way", not brute-force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_index_map = {}
        for i in range(len(nums)):
            find_in_map = target - nums[i]
            if find_in_map in val_index_map.keys():
                return [val_index_map[find_in_map], i]
            else:
                val_index_map[nums[i]] = i
        return []