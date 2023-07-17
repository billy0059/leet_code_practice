class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # After "1 to len(nums)-1" times rotation, the list would have two portions:
        # Left and Right.
        # The minimum of the Left portion would be bigger or euqal to the maximum of the Right portion
        # Use above condition and apply binary search for this problem.
        l, r = 0, len(nums)-1

        while l<=r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[r]: # mid is in left portion
                if target > nums[mid] or target < nums[l]: # target is in the right hand side
                    l = mid+1
                else: # target is in the left hand
                    r = mid-1
            else: #mid is in the right portion
                if target < nums[mid] or target > nums[r]: # target is in the left hand side
                    r = mid-1
                else:
                    l = mid+1
        return -1