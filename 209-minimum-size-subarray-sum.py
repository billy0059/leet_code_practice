class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Sliding window problem, valid condition: sum of window >= target
        target_win = [-1, -1]
        target_len = sys.maxsize
        l = 0
        win_sum = 0
        for r in range(len(nums)):
            win_sum += nums[r]
            if win_sum >= target: # Valid, try to find minimum window
                while win_sum - nums[l] >= target:
                    win_sum -= nums[l]
                    l += 1
                if r-l+1 < target_len: # Found minimum window for this right bound, compare the result with previous one
                    target_win = [l, r]
                    target_len = r-l+1
        l, r = target_win
        return (r-l+1) if target_win!=[-1, -1] else 0 # Return the window size if target_win != [-1, -1]