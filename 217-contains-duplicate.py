# https://leetcode.com/problems/contains-duplicate/description/
# Do not use a list in this case, lookups are faster in dictionaries!
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        val_times_map = {} #Use dict for lookup!
        for num in nums:
            if num in val_times_map.keys():
                return True
            val_times_map[num] = 1
        return False

# Lookups are faster in dictionaries because Python implements them using hash tables. 
# If we explain the difference by Big O concepts, 
# dictionaries have constant time complexity, O(1) while lists have linear time complexity, O(n).