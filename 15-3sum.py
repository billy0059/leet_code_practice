class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        '''  This solution would hit TLE
        ret_list = []
        for i in range(len(nums)):
            target = -nums[i]
            # find two of rest elements that the sum=target
            value_index_map = collections.defaultdict(list)
            for j in range(len(nums[i+1:])):
                value_index_map[nums[i+1:][j]].append(j)
            #print(value_index_map)
            for j in range(len(nums[i+1:])):
                if (target - nums[i+1:][j]) in value_index_map and value_index_map[(target - nums[i+1:][j])] != [j]:
                    if sorted([nums[i], nums[i+1:][j], target-nums[i+1:][j]]) not in ret_list:
                        ret_list.append(sorted([nums[i], nums[i+1:][j], target-nums[i+1:][j]]))
        return ret_list
        '''

        # Sort the input list first, and iterate the list,
        # make every number (num[i]) in the list become the "target" of "two sum II",
        # and make "rest of the list" (num[i+1:]) into "two sum II" problem, with the
        # target -num[i].
        # Remember to skip the same target if we have done it.
        # Remember to skip the same second value in the result if we have added it.
        ret = []
        sort_nums = sorted(nums) # nlogn
        i = 0
        while i<len(sort_nums)-2:
            if i>0:
                sort_nums
                while sort_nums[i] == sort_nums[i-1] and i<len(sort_nums)-2: # Skip the same "target" for "two sum"
                    i+=1
            # Now the problem turns to "two sum II"
            target = -sort_nums[i]
            l = i+1
            r = len(sort_nums)-1
            while l<r:
                if sort_nums[l] + sort_nums[r] == target:
                    ret.append([sort_nums[i], sort_nums[l], sort_nums[r]])
                    l+=1
                    while sort_nums[l] == sort_nums[l-1] and l<r: # Skip the same second val in the result
                        l+=1
                elif sort_nums[l] + sort_nums[r] > target:
                    r-=1
                else:
                    l+=1
            i+=1
        return ret
