class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        # nums    = [1,   2, 3, 4, 5] --> Given input
        # prefix  = [1,   1, 2, 6,24] --> prefix[i]  is the product of nums[0:i] (not including i)
        # postfix = [120,60,20, 5, 1] --> postfix[i] is the product of nums[i+1:] (i+1 ~)
        # Result  = [120,60,40,30,24] --> Result[i] = prefix[i] * postfix[i]
        prefix  = [1 for i in range(len(nums))]
        postfix = [1 for i in range(len(nums))]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):  # destination set to -1 for 0
            postfix[i] = postfix[i+1] * nums[i+1]

        return [i*j for i, j in zip(prefix, postfix)]
        '''
        ############################################
        # Follow up: space complexity to O(1)
        ############################################
        ret = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            ret[i] = ret[i-1] * nums[i-1]
        postfix = nums[-1]
        for i in range(len(nums)-2, -1, -1): # from end-1 to start, do multiplication
            ret[i] = postfix * ret[i]
            postfix *= nums[i]
        return ret