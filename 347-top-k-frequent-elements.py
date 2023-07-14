class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create an array, which "the index is the occur times" that the number shows in the given list
        occur_times_array = [[] for i in range(len(nums)+1)] # There is at least a value occurs one time if
                                                             # the given list is non-empty.

        # Utilize a map, which the key is the number, value is the occur times of the number
        val_occur_times_map = collections.defaultdict(int)
        for num in nums:
            val_occur_times_map[num] += 1
        for key in val_occur_times_map:
            occur_times_array[val_occur_times_map[key]].append(key)

        ret = []
        i = len(occur_times_array) - 1
        while k>0:
            if occur_times_array[i] != []:
                k -= len(occur_times_array[i])
                for num in occur_times_array[i]:
                    ret.append(num)
            i-=1
        return ret
