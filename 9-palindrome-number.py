# https://leetcode.com/problems/palindrome-number/description/
# idea: Change the number to string, continuing to compare the first and last character till middle one
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x % 10 == 0 or x < 0:
            return False
        num_str = str(x)
        for i in range(len(num_str) // 2):
            if num_str[i] != num_str[-i-1]:
                return False
        return True