class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if nums[i] > nums[i+1], then nums[i+1] is the result
        l, r = 0, len(nums)-1
        ret_min = sys.maxsize
        # [4,5,6,7,0,1,2]
        #  0 1 2 3 4 5 6
        while l<=r: # We need to check the last possible value, which is r=l
            mid = l + (r-l)//2
            if nums[mid] <= nums[r]: # mid might be the answer, compare it with the current minimum
                ret_min = min(nums[mid], ret_min)
                r = mid-1 # continue finding if there is smaller value
            elif nums[mid] > nums[r]: # mid is still in rotated result, we do not need any thing behind mid
                l = mid+1
        return ret_min