class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        if target > nums[-1] or target < nums[0]:
            return -1
        elif len(nums) == 1:
            return 0 if nums[0] == target else -1
        if nums[0] == target:
            return 0
        if nums[len(nums)-1] == target:
            return len(nums) -1

        l, r = 0, len(nums)-1
        while (r-l) > 1:
            if target > nums[(l+r)//2]:
                l = (l+r)//2
            elif target < nums[(l+r)//2]:
                r = (l+r)//2
            else:
                return (l+r)//2
        return -1
        '''
        # More concise way to do is to have a mid ((l+r)//2)
        # If target > nums[mid], then the left bound goes to mid + 1, sinde the index <= mid would never be the answer.
        # If target < nums[mid], then the right bound goes to mid - 1, sinde the index >= mid would never be the answer.
        # This way could also take care of edge cases, which the len(nums) <=3
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1