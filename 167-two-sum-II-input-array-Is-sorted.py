class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l<r:
            if numbers[l] > 0 and target > 0:
                while numbers[r] > target:
                    r -= 1
            if numbers[r] < 0 and target < 0:
                while numbers[l] < target:
                    l += 1
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
        return []
