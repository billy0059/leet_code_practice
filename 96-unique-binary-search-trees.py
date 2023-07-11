'''
https://leetcode.com/problems/unique-binary-search-trees/
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
'''

class Solution:
    def numTrees(self, n: int) -> int:
        #Dynamic programming.
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1): #(1~n)
            for j in range(0, i): #(0~(i-1))
                dp[i] += dp[j] * dp[i - j - 1] #f(0)*f(n-1) + f(1)*f(n-2) + ... + f(n-1)*f(0)
        return dp[n]

def main():
    n=3
    solution = Solution()
    print(solution.numTrees(n))


if __name__ == '__main__':
    main()